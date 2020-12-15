import json
import numpy as np
import re
import glob


def editFile(filename):
    f = open(filename, 'r+')
    text = f.read()
    text = re.sub("\'", '\"', text)
    f.seek(0)
    f.write(text)
    f.truncate()
    f.close()


all_files = glob.glob("files/*.txt")
all_files.sort()
# print("all files : ", all_files)

num_files = len(all_files)

json_data_ = []
for file_ in all_files:
    editFile(file_)
    with open(file_) as f:
        json_data_.append(json.load(f))

# print("json data : ", json_data_)

ts_ = []
i = num_files
emp_names_ = []
for data in json_data_:
    emp_name = list(data.keys())[0]
    emp_names_.append(emp_name)
    i -= 1
    ts_.append(data[emp_name].values())

# print("emp name s: ", emp_names_)

def update_time_array(t):
    val = t.split()
    _from = val[0].split(':')
    from_hr = int(_from[0])
    from_mint = int(_from[1][:-2])

    _to = val[2].split(':')
    to_hr = int(_to[0])
    to_mint = int(_to[1][:-2])

    if _from[1][2] == 'A':
        start = from_hr*60 - 540 + from_mint
    else:
        if from_hr != 12:
            start = (from_hr+12)*60 - 540 + from_mint
        else:
            start = (from_hr)*60 - 540 + from_mint

    if _to[1][2] == 'A':
        end = to_hr*60 - 540 + to_mint
    else:
        if to_hr != 12:
            end = (to_hr+12)*60 - 540 + to_mint
        else:
            end = (to_hr)*60 - 540 + to_mint

    new_a = np.arange(start, end, 1)
    return new_a



def populate_time(ts):
    time_s = [0]*481
    for time in ts:
        for t in time:
            a = update_time_array(t)
            time_s = np.array(time_s)
            time_s[a] = 1

    return time_s

time_ = []
for num in range(num_files):
    print ("num : " , num)
    print(ts_[num])
    time_.append(populate_time(ts_[num]))


def print_slots(time):
    for i in range(time.shape[0]):
        if i % 60 == 0:
            print()
        if i % 10 == 0:
            print(time[i], " ", end='')
    print()

def add_to_available_slots(start, end):
    from_hr = 9 + int(start/60)
    from_min = start % 60
    to_hr = 9 + int((end)/60)
    to_min = (end) % 60

    if from_hr >= 12:
        if from_hr != 12:
            from_hr -= 12
        string1 = str(from_hr) + ":" + \
                        str(f"{from_min:02d}") + "PM"
    else:
        string1 = str(from_hr) + ":" + \
                        str(f"{from_min:02d}") + "AM"

    if to_hr >= 12:
        if to_hr != 12:
            to_hr -= 12
        string2 = str(to_hr) + ":" + str(f"{to_min:02d}") + "PM"
    else:
        string2 = str(to_hr) + ":" + str(f"{to_min:02d}") + "AM"

    final = string1 + " - " + string2
    return final

slot_ = []
for num in range(num_files):
    av_slots = list()
    count = 0
    flag = 1
    # found = False
    time = time_[num]
    for i in range(time.shape[0]):
        if time[i] == 0:
            if flag == 1:
                start = i
                flag = 0

            count += 1

        if (time[i] != 0 or i == time.shape[0]-1) and (count > 1):
            # if count > 1:
            end = i
            final = add_to_available_slots(start, end)
            av_slots.append(final)

            count = 0
            flag = 1

    slot_.append(av_slots)


slot = float(input())
slot_min = int(slot*60)
count = 0
flag = 1
found = False
inAll = True
for i in range(time_[0].shape[0]):
    for num in range(num_files):
        if time_[num][i] == 0:
            inAll = True
        else:
            inAll = False
            break
    if inAll == True:
        if flag == 1:
            start = i
            flag = 0

        count += 1
        if count == slot_min:
            found = True
            end = i
            break
    else:
        count = 0
        flag = 1

if found == True:
    final = add_to_available_slots(start, end+1)
else:
    final = "no slot available"
 
val_key = list(json_data_[0].values())[0]
keys = list(val_key.keys())
textData = "Available slot\n"
for num in range(num_files):
    textData += str(emp_names_[num]) +": " + str(slot_[num]) +"\n"
textData +=  "\nSlot Duration: " + str(slot) + " hour\n"
textData += "{'" + str(keys[0]) + "' : ['" + str(final) + "']}"

# print ("text datav : ", textData)
filename = "output.txt"
f = open(filename, 'w+')
f.write(textData)
f.close()
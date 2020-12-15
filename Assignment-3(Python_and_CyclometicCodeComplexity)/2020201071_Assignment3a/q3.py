import json
import numpy as np
import re

def editFile(filename):  
    f = open(filename, 'r+')
    text = f.read()
    text = re.sub("'", '"', text)
    f.seek(0)
    f.write(text)
    f.truncate()
    f.close()

editFile('Employee1.txt')
editFile('Employee2.txt')

with open('Employee1.txt') as f:
    json_data = json.load(f)

with open('Employee2.txt') as f2:
    json_data2 = json.load(f2)

ts1 = json_data["Employee1"].values()
ts2 = json_data2["Employee2"].values()
# print("json data1 : ", ts1)
# print("json data2 : ", ts2)
time_1 = [0]*481
time_2 = [0]*481

def populate_time(ts):
    time_s = [0]*481
    for time in ts:
        for t in time :
            val = t.split()
            _from = val[0].split(':')
            from_hr = int(_from[0])
            from_mint = int(_from[1][:-2])

            _to = val[2].split(':')
            to_hr = int(_to[0])
            to_mint = int(_to[1][:-2])

            if _from[1][2] == 'A':
                start = from_hr*60 -540 + from_mint
            else:
                if from_hr != 12:
                    start = (from_hr+12)*60 -540 + from_mint
                else:
                    start = (from_hr)*60 -540 + from_mint
            
            if _to[1][2] == 'A':
                end = to_hr*60 - 540 + to_mint
            else:
                if to_hr != 12:
                    end = (to_hr+12)*60 - 540 + to_mint
                else:
                    end = (to_hr)*60 - 540 + to_mint

            new_a = np.arange(start, end,1)
            time_s = np.array(time_s)
            time_s[new_a] = 1

    return time_s


time_1 = populate_time(ts1)
time_2 = populate_time(ts2)


def print_slots(time):
    for i in range(time.shape[0]):
        if i%60==0 :
            print()
        if i%10==0:
            print(time[i], " ", end = '')
    print()

def available_slots(time):
    av_slots = list()
    count = 0
    flag=1
    found = False
    for i in range(time.shape[0]):
        if time[i]==0:
            if flag==1:
                start = i
                flag=0

            count += 1

        if time[i]!=0 or i == time.shape[0]-1:
            if count>1:
                end = i
                from_hr = 9 + int(start/60)
                from_min = start%60
                to_hr = 9 + int((end)/60)
                to_min = (end)%60

                if from_hr >= 12:
                    if from_hr!=12:
                        from_hr -= 12
                    string1  = str(from_hr) + ":" + str(f"{from_min:02d}") + "PM"
                else:
                    string1  = str(from_hr) + ":" + str(f"{from_min:02d}") + "AM"

                if to_hr >= 12:
                    if to_hr!=12:
                        to_hr -= 12
                    string2  = str(to_hr) + ":" + str(f"{to_min:02d}") + "PM"
                else:
                    string2  = str(to_hr) + ":" + str(f"{to_min:02d}") + "AM"

                final = string1 + " - " + string2
                av_slots.append(final)

            count=0
            flag=1
    
    return av_slots
   
# print_slots(time_1)
# print()
# print_slots(time_2)

slot1 = available_slots(time_1)
slot2 = available_slots(time_2)
# print("slot1 : ", slot1)
# print("slot2 : ", slot2)

slot = float(input())
slot_min = int(slot*60)
count = 0
flag = 1
found = False
for i in range(time_1.shape[0]):
    if time_1[i]==0 and time_2[i]==0 :
        if flag==1:
            start = i
            flag=0
        
        count += 1
        if count == slot_min:
            found = True
            end = i
            break
    else:
        count = 0
        flag=1

if found==True:
    from_hr = 9 + int(start/60)
    from_min = start%60
    to_hr = 9 + int((end+1)/60)
    to_min = (end+1)%60

    if from_hr >= 12:
        if from_hr!=12:
            from_hr -= 12
        string1  = str(from_hr) + ":" + str(f"{from_min:02d}") + "PM"
    else:
        string1  = str(from_hr) + ":" + str(f"{from_min:02d}") + "AM"

    if to_hr >= 12:
        if to_hr!=12:
            to_hr -= 12
        string2  = str(to_hr) + ":" + str(f"{to_min:02d}") + "PM"
    else:
        string2  = str(to_hr) + ":" + str(f"{to_min:02d}") + "AM"

    final = string1 + " - " + string2

else:
    final = "no slot available"
    print (final)

keys = list(json_data["Employee1"].keys())
textData = "Available slot\nEmployee1: " + str(slot1) +"\nEmployee2: " + str(slot2) + "\n\nSlot Duration: " + str(slot) + " hour\n"
textData += "{'" + str(keys[0]) + "' : ['" + str(final) + "']}"
filename = "output.txt"
f = open(filename, 'w')
f.write(textData)
f.close()
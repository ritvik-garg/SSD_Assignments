import json
from functools import reduce

with open('org.json') as f:
    json_data = json.load(f)

myDict = {}

def convert_to_child_ancestor_dict(json_data):
    for keys, values in json_data.items():
        for value in values:
            if len(value) == 1:
                myDict[value["name"]] = [("1")]
            else:
                myDict[value["name"]] = [(value["parent"])]

convert_to_child_ancestor_dict(json_data)    
# print ( "dict : ", myDict)


def add_all_ancestors(myDict):
    count = 0
    for keys, values in myDict.items():

        if(count!=0):
            i=0
            while 1:
                val = myDict[values[i]][0]
                if val!="1":
                    myDict[keys].append(val)
                    i += 1
                else:
                    break
        count += 1

add_all_ancestors(myDict)
# print ( " new dict : ", myDict)

input_list = input().split()
num_val = int(input_list[0])
emp_id = input_list[1:]

def get_list(list_emp, myDict):
    for i in range(num_val):
        list_emp.append(myDict[emp_id[i]])

list_emp = []
get_list(list_emp, myDict)

found = False

res = list(reduce(lambda i, j: i & j, (set(x) for x in list_emp))) 
res_size = len(res)
level_emp = []
ans = res[0]

def printResult():
    if res_size!=0:
        ans = res[0]
        for i in range(num_val):
            level_emp.append(list_emp[i].index(ans))

        print("common leader: " + ans)
        for i in range(num_val):
            print ("leader " + ans + " is " + str(level_emp[i]+1) + " levels above " + emp_id[i])
    else:
        ans = "no common parent possible"

printResult()
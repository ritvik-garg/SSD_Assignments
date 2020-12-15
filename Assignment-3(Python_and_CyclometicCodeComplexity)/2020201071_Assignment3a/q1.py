import json

with open('org.json') as f:
    json_data = json.load(f)

myDict = {}

for keys, values in json_data.items():
    for value in values:
        if len(value) == 1:
            myDict[value["name"]] = [("1")]
        else:
            myDict[value["name"]] = [(value["parent"])]
        
# print ( "dict : ", myDict)

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

# print ( " new dict : ", myDict)

emp1 = input()
emp2 = input()

list1 = myDict[emp1]
list2 = myDict[emp2]

# print("list1 : ", list1)
# print("list2 : ", list2)
found = False
for i in list1:
    if i in list2:
        found = True
        ans = i
        break

if found == True:
    level_emp1 = list1.index(ans)
    level_emp2 = list2.index(ans)

    print(ans)
    print (ans + " is " + str(level_emp1+1) + " levels above " + emp1)
    print (ans + " is " + str(level_emp2+1) + " levels above " + emp2)
else:
    ans = "no common parent possible"
    print(ans)
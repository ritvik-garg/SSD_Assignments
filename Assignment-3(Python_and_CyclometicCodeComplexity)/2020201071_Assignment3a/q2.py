import re

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

def calculate(d1, m1, y1, d2, m2, y2):
    if m1<=2 :
        years1 = y1-1
    else:
        years1 = y1

    leap_years1 = int(years1//4 - years1//100 + years1//400)

    if m2<=2 :
        years2 = y2-1
    else:
        years2 = y2
    leap_years2 = int(years2//4 - years2//100 + years2//400)

    total_days1 = y1*365 + d1 + leap_years1
    for i in range(m1-1):
        total_days1 += monthDays[i]
    
    total_days2 = y2*365 + d2 + leap_years2
    for i in range(m2-1):
        total_days2 += monthDays[i]
    
    return abs(total_days2 - total_days1)

# print (calculate(10, 9, 2020, 30, 9, 2020))

with open("date_calculator.txt", 'r+') as f:
    line1 = f.readline()
    line1 = line1.replace(',', ' ')
    date1 = line1.split()[1:]
    
    line2 = f.readline()
    line2 = line2.replace(',', ' ')
    date2 = line2.split()[1:]
    
# print ("date1 : ", date1)
# print ("date2 : ", date2)

month_mapping = {"jan":1,"feb":2,"mar":3, "apr":4, "may":5, "jun":6, "jul":7, "aug":8,"sep":9, "oct":10, "nov":11, "dec":12}

def getDate(date):
    if len(date)>1:
        firstIndexOfChar = None
        temp = re.search(r'[a-z]', date[0], re.I) 
        if temp is not None: 
            firstIndexOfChar = temp.start() 
        day = int(date[0][:firstIndexOfChar])
        mon_start = date[1][:3].lower()
        month = int(month_mapping[mon_start])
        year = int(date[2])
    else:
        date = date[0]
        dmy = re.split('\.|-|/',date)
        day = int(dmy[0])
        month = int(dmy[1])
        year = int(dmy[2])

    return (day, month, year)

date1 = getDate(date1)
date2 = getDate(date2)
# print ("date1 : ", date1)
# print ("date2 : ", date2)

d1 = date1[0]
m1 = date1[1]
y1 = date1[2]

d2 = date2[0]
m2 = date2[1]
y2 = date2[2]


diff = calculate(d1, m1, y1, d2, m2, y2)
# print ("diff : ", diff)

text = "Date Difference: " + str(diff) + " Day"
with open("output.txt", "w") as f:
    f.write(text)
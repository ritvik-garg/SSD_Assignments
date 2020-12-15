# Assignment - 3(Part A): Python
### Software Systems Development

##### Question 1:
###### Assumptions : 
+ Code takes two user input.
+ `Input names should exist in the org.json file`. Names which are not mentioned in the json file will throw error.
+ Input element `cannot be root elements name (level-0)`, as the parent of root element is not defined.
###### Explanation :
To find the common leader, a dictionary is created with `key as child` and `value as the list of all ancestors`, that child has. Here, the values in the list are stored such that `value[i+1] is parent of value[i]`, for i>=0.
```
{"child" : ["parent", "grandparent",..]
```
Now, after getting two input(lets say emp1 and emp2), we get their corresponding list of ancestors using our new dictionary. The first common element in the both the list is the common parent for emp1 and emp2.
The level of the common parent from emp1 and emp2 can be found using the index of commmon parent in their corresponing lists.

##### Example of Input/Output :
###### Input:
```
<emp1>
<emp2>
```
###### Output:
```
<xyz>
<xyz> is <number> levels above <emp1>
<xyz> is <number> levels above <emp2>
```
##### Question 2:
###### Assumptions :
+ Following format of dates are allowed :
    + 10th September, 2020
    + DD/MM/YYY
    +  DD-MM-YYYY
    + DD.MM.YYYY
    + 10th Sep, 2020
+ Incase of dates with upperscript with day (`e.g. 7th, 2nd, 31st`), there should not be any space between day and upperscript (`2 nd is not allowed`).
###### Explanation :
For each of the two given input date, the `total number of days till the given date is calculated` considering leap years, and then finally, the difference of those is taken.

##### Example of Input/Output :
###### Input:
`NO USER INPUT REQUIRED`
###### Output:
`'output.txt' file is created` with the format mentioned in the assignment-pdf

##### Question 3:
###### Assumptions :
+ Code `requires user input for slot duration`.
+ Works fine for all slots duration (such that conversion from hour to minute is a valid integer)
###### Explanation :
First, `text file is converted into json readable format`by replacing `'` with `"`, and then used json library to read the json data.  
Two list of size 480 is taken, for maintaiing `busy (or 1)` and `free (or 0)` slots in 9am to 5pm interval (8 hours * 60 minutes = 480) for each of the employee.
Using those two list, available slots for each employee is taken, and also the first common available slot of size equal to slot duration given by the user.


##### Example of Input/Output :
###### Input:
```
<slot_duration>
```
###### Output:
`'output.txt' file is created` with the format mentioned in the assignment-pdf
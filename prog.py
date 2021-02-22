## for colored output
from termcolor import colored
## Reading the file
f = open("airlines.csv")
## reading each line of file
data_air = f.readlines()
## finding the names of columns
cols= data_air[0].strip().split(',')
"""code,rest = data_air[1].strip().split(',',maxsplit=1)
rest_1 = rest.replace(",","--",1)
rest_2 = rest_1.split(",")
print(rest_2)"""
#print(data_air[1])
## records contains all the rows of the data
## count_records store the Name of airport and the frequency
records = []
count_record = {}
for row in data_air[1:]:
    ## spliting each row to achive a structured format
    all_v= row.strip().split(',',maxsplit=1)
    code = all_v[0]
    rem = all_v[1:]
    rest = ",".join(rem)
    rest_1 = rest.replace(",","--",1)
    rest_2 = rest_1.split(",")
    name = rest_2[0].replace("--",",",1)
    rest_2[0] = name.replace('"','')
    final_row = rest_2
    records.append(final_row)

    ## counting the occurence of record
    if(final_row[0] not in count_record):
        count_record[final_row[0]] = 0
    count_record[final_row[0]]+=1
#print(final_row)
print(colored("OUTPUT 1: ",'green'))
print()
print("The list of unique airport names and number of times ")
#print(count_record)
# converting the dictionary to json
import json
json_output_1 = json.dumps(count_record,indent= 4)
print(json_output_1)

## finding the most frequent airport and least frequent airport
total_records= len(records)
max_val =0 
max_key = None
min_key = None
min_val = total_records

for k,v in count_record.items():
    if(min_val > v):
        min_val = v
        min_key = k
    if(max_val < v):
        max_val = v
        max_key =k
print()
print(colored("OUTPUT 2: ",'green'))
print("The airport which was mentioned the most number of times is: ")
print(colored( max_key,'blue'),end=" : ")
print(colored( max_val,'blue'))
print(colored("OUTPUT 3: ",'green'))
print("The airport which was mentioned the least number of times is: ")

print(colored( min_key,'blue'),end=" : ")
print(colored( min_val,'blue'))

# Python program to read
# json file
 
import json
 
# Opening JSON file
f = open('deck_test.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list

mylist=[]

for mylist in data['cards']:
    mylist.append(data['cards'])
    print(mylist)
 
# Closing file
f.close()

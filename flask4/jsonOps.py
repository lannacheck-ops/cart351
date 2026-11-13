# Import json librarry
import json
# Read from file and parse JSON
# jsonFile = open("files/test.json", "r")
# data = json.load(jsonFile)
# print(data)
# print(type(data)) # a list

# json_str = '{"name":"Sabs", "fav_col":"red", "fav_city":"montreal"}'
# # json.loads the s stands for load string not the same as json.load
# data_2 = json.loads(json_str) 
# print(data_2)
# print(type(data_2))#converts to a dict

# data_toSave = {"name":"mandy", "fav_col":"blue", "fav_city":"winnipeg"}
# #convert dictionary to str
# jsonStr = json.dumps(data_toSave, indent=4)
# #open or create if non existent
# fileOpen = open("files/new_sample.json","w")
# fileOpen.write(jsonStr)

# jsonFile = open("files/new_sample_b.json", "w")
# data_toSave_2= {"name":"mandy", "fav_col":"blue", "fav_city":["list",3,4,True,"abc"]}
# json.dump(data_toSave_2,jsonFile, indent =4)

jsonFile = open("files/new_sample_b.json", "r+")
data = json.load(jsonFile)
# print(data['fav_city'])
# print(type(data['fav_city']))
# #go to beginning of file
jsonFile.seek(0)
data['fav_city'].append("another element")
data["newKey"] = 1234
#output to the file
json.dump(data,jsonFile, indent =4)
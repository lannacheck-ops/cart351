# rainbowFile = open("files/rainbow.txt", "r")

# # One character = one byte. The parameter in the paranthesis specifies how many characters are read
# # Read first 10 characters
# out = rainbowFile.read(10)
# # Since I have already have a read method it creates a bookmark at the position it finished reading at then when the read is called again it starts at that same bookarked position
# # So we use seek to start reading the file at the postion we want it to start reading at 
# rainbowFile.seek(0)
# # outAll = rainbowFile.read()
# # print(outAll)
# # By default reads the first line (where the code sees /n)
# # oneLine = rainbowFile.readline()
# # print(oneLine)
# allLines = rainbowFile.readlines()
# # print(allLines)
# # All lines returns a List so u can go thru all the lines using the list syntax
# print(allLines[1])


# Since the file doesnt exist beforehand it creates the file by itself
#sampleFile = open("files/sample_text_rev.txt", "w")
# for i in range(3): 
#     a_name = input("Enter the name of the animal: ") 
#     sampleFile.write(a_name) 
#     # Write overwrites the file it doesnt append 
#     sampleFile.write("\n") 
# # Safe to close it
# sampleFile.close() 
# print("Data is written into the file.") 
# colorList = [] 
# for i in range(3): 
#     a_name = input("Enter the name of a color: ") 
#     colorList.append(a_name + '\n') 
# sampleFile.writelines(colorList) 
# sampleFile.close() 
# print("Data is written into the file.") 

# Appending to th file
sampleFile_a = open("files/sample_text.txt", "a")
nameList = [] 
for i in range(3): 
    a_name = input("Enter the name of someone in your class: ") 
    nameList.append(a_name + '\n') 
# Still use write lines but since we opened it to append it appends to the file
sampleFile_a.writelines(nameList) 
sampleFile_a.close() 
print("Data is written into the file.") 
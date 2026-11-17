## Week 7 Journal

By default, python can only read text files and binary files. We learned that there are different modes to open a file. For example the following code:
st = open("files/sample_text.txt", "w+"), opens a file in write+ mode (the "w+" is the parameter that defines the file opening mode) and in this mode you can read from and write to the file. It creates the file if it does not exist on your system an it will overwrite it if the file is present in your system.

Since python can't read other files by default, we must import a json package to open and use json files in python. Retrieving json files in python turns them into dictionaries or lists. What I find really useful is the json.dump function because it converts a dictionary to a json object and you can save the converted dictionary in a file path of your choice. Ex: jsonFile = open("files/new_sample_b.json", "w"(write only overwrites info in the file)) json.dump(data_toSave_2(dictionary),jsonFile(file path), indent =4 (indentation)). You can only dump to a file path if the way you opened the file was in write mode.

One thing I need to remember in my projects is that when creating a folder to store user data, I must create a file at the root and not in the static folder because the file is not meant to be a client side accessible file.





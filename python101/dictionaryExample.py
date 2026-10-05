class_professors = {'Cart_253_A':'Pippin Bar',
                    'Cart_211':'Brad Todd',
                    'Cart_214':'Joanna Berzowska', 
                    'Cart_215':'Jonathan Lessard'}
# print(type(class_professors))

specialList = {17: [1.6, 2.45], 42: [11.6, 19.4], 101: [0.123, 4.89]}
# print(specialList[17])
# print(class_professors['Cart_253_A'])

#Returns keys as a list
# print(specialList.keys())
# for key in specialList.keys():
#     #printed value associated to that key
#     print(specialList[key])
#Prints the value associated with each key in the dictionary as a list
# print(specialList.values())
# for value in specialList.values():
#     print(value)

#Output of expression below ([(17, [1.6, 2.45]), (42, [11.6, 19.4]), (101, [0.123, 4.89])])
#Item outputs the key and key value together as a group in a list
# print(specialList.items())
# for item in specialList.items():
#     #Return key value of the tupple
#     print(item[0])

# for item in class_professors:
#     #Returns the key 
#     print(item)
#     #Returns the value in the key
#     print(class_professors[item])

# shopping = {
#             'vegetables': [{'spinach':["green", "blue"]}, 'carrots','broccoli','lettuce'],
#             'fruit': ['canteloupe', 'banananas'],
#              'bakery': ['bagels', 'rye bread'],
#             }
# #Returns green (read from left to right)
# print(shopping['vegetables'][0]["spinach"][0])

# shopping_rev = {
#             'vegetables': {"green":["spinach","broccoli","lettuce"],"orange":["carrots"]},
#             'fruit': ['canteloupe', 'banananas'],
#              'bakery': ['bagels', 'rye bread'],
#             }

# shopping_rev["cleaning_items"] = ["dish-soap", "sponges"]
# shopping_rev["cleaning_items"].append("bleach")
# print(shopping_rev)

test_dict = {'a': 1, 'b': 2}
#test_dict['a'] is 1

test_dict['a'] = 100
test_dict['a']
#test_dict['a'] is 100
import json
import ast

def depth(x):
    if type(x) is dict and x:
        return 1 + max(depth(x[a]) for a in x)
    if type(x) is list and x:
        return 1 + max(depth(a) for a in x)
    return 0


#Excecution

file = open("doc.json", "r")
contents = file.read()
dictionary = ast.literal_eval(contents)
depth(dictionary)

print("Length of the json is {}".format(depth(dictionary)))



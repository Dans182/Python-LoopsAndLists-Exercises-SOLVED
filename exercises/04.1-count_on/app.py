my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
new_list = []
#your code go here:

for x in my_list:
    if isinstance(x, dict) or isinstance(x, list):
        new_list.append(x)
        
print(new_list)
my_array = [20, 20, 1, 2]

rep_dict = {}

for item in my_array:
    if (item in rep_dict):
        rep_dict[item] += 1
    else:
        rep_dict[item] = 1


for key, valor in rep_dict.items():
    print(f"{key} : {valor}")
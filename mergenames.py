def unique_names(names1, names2):
    new_Arr = []   
    new_Arr = list(dict.fromkeys(names1 + names2))
    return new_Arr

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))
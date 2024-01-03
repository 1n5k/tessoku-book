list1 = [input() for i in range(2)]
size = int(list1[0].split(" ")[0])
target = int(list1[0].split(" ")[1])
pool = [int(i) for i in list1[1].split(" ")]
flag = "No"
for i in pool:
    if i == target:
        flag = "Yes"
print(flag)

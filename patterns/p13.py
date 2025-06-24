list=[10,2,56,78,59]
max=list[0]
for i in range(len(list)):
    if max<list[i]:
        max=list[i]
print(max)
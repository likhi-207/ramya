list=[2,1,5,1,1,5,3,2]
index=0
for i in range(len(list)):
    if list[i]!=0:
        list[index]=list[i]
        index+=1
for i in range(index,len(list)):
    list[i]=0
print(list)
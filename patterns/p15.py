list=[0,0,1,2,2,5,6]

index=1
for i in range(1,len(list)):
    if list[i-1]!=list[i]:
        list[index]=list[i]
        index+=1
print(list)
        

        
        
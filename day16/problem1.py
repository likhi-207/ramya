arr=[22,34,67,89,89,89,35,90,45,12,10,9,10]
max_freq=0
max_freq_element=0
for i in range(len(arr)):
    count=1
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            count+=1
            if max_freq<count:
                max_freq=count
                max_freq_element=arr[i]
print(f"The number {max_freq_element} appears {max_freq} times.")
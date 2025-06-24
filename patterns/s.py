s="dfa12321afd"
largest="-1"
secondlargest=-1
for i in s:
    if i.isdigit() and i>largest:
        secondlargest=largest
        largest=i
    if i.isdigit() and i<largest and i>secondlargest:
        secondlargest=i
print(largest)
print(secondlargest)
    
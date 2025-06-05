import airthmetic
a=int(input())
while True:
    op=input()
    if op=="=":
        print("end of the calculation",a)
        break
    b=int(input()) 
    if op=="+":
        a=airthmetic.add(a,b)
    elif op=="-":
        a=airthmetic.sub(a,b)
    elif op=="*":
        a=airthmetic.mul(a,b)
    elif op=="/":
        a=airthmetic.div(a,b)
    elif op=="**":
        a=airthmetic.power(a,b)
    elif op=="%":
        a=airthmetic.mod(a,b)
    print(a)
        

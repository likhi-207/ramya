class Node:
    def __init__(self,val=0,nextnode=None):
        self.val=val
        self.next=nextnode
item1=Node(100)
item2=Node(200)
item3=Node(300)
item4=Node(400)

item1.next=item2
item2.next=item3
item3.next=item4
item4.next=None
result=[]
head=item1
current=head
tail=0
length=0
while current!=None:
    result.append(str(current.val))
    length+=1       
    current=current.next
print("=>".join(result))
print(length)

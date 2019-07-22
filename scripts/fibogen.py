def fibo():
    prev=-1
    curr=1
    next=0
    while(True):
        yield next
        prev=curr
        curr=next
        next=prev+curr

l=[]
for num in fibo():
    if(num<100):
        l.append(num)
        #print(num)
    else:
        break



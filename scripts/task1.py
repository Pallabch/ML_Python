#Write a function that accepts a list and returns the minimum and maximum of the list
def listacceptor(a):
    x=max(a),min(a)
    print(type(x))
    return x


lis=[1,2,3,4,56,7,9]
maxx,minn=listacceptor(lis)
print(maxx,minn)


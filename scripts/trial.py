# players=["virat","dhoni"]
# scores=[10,20]
# for player,score in zip(players,scores):
#     print("player {} score {}".format(player,score))

# for idx,tup in enumerate(zip(players,scores)):
#     print(" {}  )player {} score {}".format(idx+1,tup[0],tup[1]))

def add(x,y):
    '''
    This function is used to add two numbers
    '''
    return x+y
def si(p,r,t):
    '''
    This function is used to calculate the simple interest gained
    '''
    return p*r*t/100

def generator():
    n=1
    print("Before first yield")
    yield n
    n+=1
    print("Before second yield")
    yield n
    print("Before 3rd yield")
    n+=1
    yield n

# g=generator()
print(type(generator()))
# a=[1,2,3]

# print(si(50000,9,10))
# print(__doc__.__doc__)  #prints the documentation of the function 



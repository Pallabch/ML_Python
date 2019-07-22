f=open("text.txt")
# for line in a:
#     print(line)

with open("text.txt") as f:
    for line in f:
        print(line)
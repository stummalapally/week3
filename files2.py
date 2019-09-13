import random


f=open("randomnumbers.txt","a")
f.write(str(random.random()) + "\n")
f.close()

with open("randomnumbers2.txt","a") as f:
    f.write(str(random.random()) + "\n")
print("All done")
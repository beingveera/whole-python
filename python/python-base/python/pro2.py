import sys
with open("system.json","w") as run: 
    for i in dir(sys):
        run.write(i)
        run.write("\n")


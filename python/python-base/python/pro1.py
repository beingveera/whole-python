import turtle as t 
with open("run.txt","w") as data:
    for i in dir(t):   
        data.write(i)
        data.write("\n")


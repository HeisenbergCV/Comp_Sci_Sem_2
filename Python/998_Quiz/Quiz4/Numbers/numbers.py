numlist = [6,9,32,28,15,22,3,18]
x = (numlist[1] + numlist[2] + numlist[3] + numlist[4] + numlist[5] + numlist[6] + numlist[7] + numlist[8])/8
x = str(x)
print("The average of the number list is" + x)

AP = 1000000000000000000000000000
p = 0
for i in range(0,7):
        if (AP > numlist[1]):
          AP = numlist[1]
AP = str(AP)
print ("The min is:" + AP)
for z in range(0,7):
    if p < numlist[z]:
         p = numlist[z]
p = str(p)
print("The max is:" + p)
        
    


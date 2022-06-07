value = int(input("please enter line length"))
value1 = input("Do you want a horizontal or a verticle line?")
if(value1 == "horizontal"):
    for y in range (0,value):
        print("*", end=" ")
        
if(value1 == "verticle"):
    for y in range(0,value):
        print("*")
    
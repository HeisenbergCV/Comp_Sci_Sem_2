list1 = ["What do you call it when a group of apes starts a company? Monkey business.", "Why do bees have sticky hair? Because they use a honeycomb.","Why is Peter Pan always flying? Because he Neverlands.", "Which state has the most streets? Rhode Island." , "What kind of car does a sheep like to drive? A lamborghini."]
import random
x = (random.randrange(0,5))

if(x == 0):
    print(list1[0])

elif(x == 1 ):
    print(list1[1])
    
elif(x == 2 ):
    print(list1[2])
    
elif(x == 3 ):
    print(list1[3])
    
elif(x == 4 ):
    print(list1[4])


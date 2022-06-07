resturaunt = ("McDonald's", "Wingstop", "Subway")
ron = ("Burger", "Fries", "McFlury" )
stop = ("Fries", "Wings", "Soda")
way = ("cold cut", "Sub", "Chips")
gru = input("Pick one of the resturaunts: Type x for McDonalds, Type y for Wingstop, Type z for Subway:")
if gru == "x":
    print("McDonalds menu:" + ron)
    if gru == "y":
        print("Wingstop menu:" + stop)
        if gru == "z":
            print("Subway menu:" + way)
            
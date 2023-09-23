def convertor():
    dollars=eval(input("Enter amount in dollars"))

    pounds = convert_from_dollars(dollars)
    print(f"that's {pounds} Pounds")


convert_from_dollars= lambda dollars:dollars*0.032

convertor()
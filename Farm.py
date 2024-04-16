def Welcome_Message():
    print("Welcome to the Old McDonald's Farm! \n Price of Egg: $0.50")

def Price_Of_Egg():
    number_of_eggs = int(input("How many eggs would you like to buy: "))
    total_price = number_of_eggs * 0.50
    print("Total Price: $", total_price)

Welcome_Message()
Price_Of_Egg()

#sudo code
#1. define a function Welcome_Message which includes price of egg
#2. define a function Price_Of_Egg which takes input from user and calculates total price
#4. Call function Welcome_Message
#5. Call function Price_Of_Egg
#5. End
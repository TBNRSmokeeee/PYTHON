                        #lets build a Robot Barista

print("Ohla, Como Estas Bienvenido a NetworkChuck coffee!!!!")
name = input("What is your name?\n")
#'name' is a variable and we set that variable equal whatever the user types in because of the 'input function'
#'input function' is designed to take input from the user-our customers. It will automagically put it into a string 

if name == "Ben" or name == "Partricia" or name == "Loki":
#the double equal sign evaluate if something is True or False
#'or' is a logical operator (they use human logic) and its not the only one eg. 'and' , 'not'
#When we used 1 equal sing when makeing a variable like name were telling the computer it is equal to whatever value the user inputs
#When we use 2 equal signs like we did for 'if' were telling the computer to evaluate it it is true or false

#When the statement evaluate to true, do somthing, if it evaluates to false, do something else. The True and False data are called Boolens, whixh is a data type
    guilty = input("Are you EVIL!!?\n")
    if guilty == "Yes":
        test = int(input("How many good deeds have you done today\n"))
        if test >= 4:
            print("Oh, sooo, your one of those good " + name + "s. Come on in!!")
        else:
            print("Your Not Welcome Here Evil " + name + " !! BEAT IT!!!")
            exit()
    else:
        print("Oh, sooo, your one of those good " + name + "s. Come on in!!")
#if its evaluates to true we kick Ben out. If it does evaluate to false we'll do something
#'if statement' mean what ever come after it is true do something 

#'exit()' basically means STOP, exit the program, were done here

else:print("Hello " + name + ", thank you sooo much for comming in today")
#the way i used the 'else' function before was i put all my scipts under it but the i changed my code layout by using the 'exit()' function whick was shorter and cleaner 

#Pythin cares abour your SPACING     it will change how it evaluates you code or might just end in an error eg. the 'if' and 'esle' are spaced differently for 'strings'

input("How are you today?\n")
drinks = input("What would you like to have from our menu:\n--Frappucino--\n--Espresso--\n--Double--\n--Espresso--\n--Red Eye--\n--Black Eye--\n--Americano--\n--Long Black--\n--Macchiato--\n--Long Macchiato--\n--Cortado--\n--Breve--\n--Cappuccino--\n--Flat White--\n--Cafe Latte--\n--Mocha--\n--Vienna--\n--Affogato--\n--Cafe au Lait--\n--Iced Coffee--\n--Latte--\n")

if drinks == "Frappucino":
    price = 13
elif drinks == "Espresso":
    prince = 6
elif drinks == "Espresso":
    price = 6
elif drinks == "Double Espresso":
    price = 12
elif drinks == "Red Eye":
    price = 5
elif drinks == "Black Eye":
    price = 7
elif drinks == "Americano":
    price = 9
elif drinks == "Long Black":
    price = 3
elif drinks == "Macchiato":
    price = 4
elif drinks == "Long Macchiato":
    price = 5
elif drinks == "Cortado":
    price = 2
elif drinks == "Breve":
    price = 7.50
elif drinks == "Cappuccino":
    price = 8
elif drinks == "Flat White":
    price = 6.50
elif drinks == "Cafe Latte":
    price = 4.60
elif drinks == "Mocha":
    price = 5.50
elif drinks == "Vienna":
    price = 6.15
elif drinks == "Affogato":
    price = 8.60
elif drinks == "Cafe au Lait":
    price = 10.50
elif drinks == "Iced Coffee":
    price = 8
elif drinks == "Latte":
    price = 3.15
else:
    print("Sorry, we don't have that here.")
    exit()

if drinks == "Latte":
    cream = 1.50
    quantity = input("How many cups would you like?\n")
    yes_or_no = input("Would you like us to add to whipped cream to that, its just $1.50 more?\n")
    if yes_or_no == "Yes":
     total_amount = int(quantity) * (price + cream)
     #because python follows the oder of operations i can use the brackets to help callculate the total amount
     print("Ok, your total is: $" + str(total_amount))
     print("We'll have those " + quantity + " " +  drinks + "s ready for you in a moment " + name + ".")
     exit()
    else:
        print("Okay, nevermind.")
        money = price * int(quantity)
        print("Your total is: $" + str(money))
        print("We'll have those " + quantity + "be " + drinks + "s ready for you in a moment " + name + ".")
        exit()

quantity = input("How many cups would you like?\n")
total = price * int(quantity)
#eg. the variable 'quantity' is a string. using 'int()' we make it an integer
#when you use the 'input' function what ever data it ask you for that data is not going to be an integer its going to be a string

print("Ok, your total is: $" + str(total))
#python can add/concatenate a string to a string but not a string to an integer - earlier i did 'print("Thank you, your total is: " + money)' the money value is an integer. I changed it to 'str(money))'

print("We'll have those " + quantity + " "  +  drinks + "s ready for you in a moment " + name + ".")
#you can add more than just strings together 

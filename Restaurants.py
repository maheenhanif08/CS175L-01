#CS 175L
#Maheen Hanif Ghaffar
#Restaurants Project With While Loop

response = "yes"
while response == "yes":
    
    Vegetarian = input("Is anyone in your party a vegetarian? \n").lower()
    Vegan = input("Is anyone in your party a vegan? \n").lower()
    Gluten_Free = input("Is anyone in your party gluten free? \n").lower()

    if Vegetarian == "yes" and Vegan == "yes" and Gluten_Free == "yes":
        print("Here are your restaurant choices: \n  Corner Cafe \n  The Chef's Kitchen")

    elif Vegetarian == "yes" and Vegan == "yes" and Gluten_Free == "no":
        print("Here are your restaurant choices: \n  Corner Cafe \n  The Chef's Kitchen")

    elif Vegetarian == "yes" and Vegan == "no" and Gluten_Free == "no":
        print("Here are your restaurant choices: \n  Main Street Pizza Company \n  Corner Cafe \n  Mama's Fine Italian \n  The Chef's Kitchen")

    elif Vegetarian == "no" and Vegan == "no" and Gluten_Free == "no":
        print("Here are your restaurant choices: \n  Joe's Gourmet Burgers \n  Main Street Pizza Company \n  Corner Cafe \n  Mama's Fine Italian \n  The Chef's kitchen")

    elif Vegetarian == "no" and Vegan == "yes" and Gluten_Free == "yes":
        print("Here are your restaurant choices: \n  Corner Cafe \n  The Chef's Kitchen")

    elif Vegetarian == "no" and Vegan == "no" and Gluten_Free == "yes":
        print("Here are your restaurant choices: \n  Main Street Pizza Company \n  Corner Cafe \n  The Chef's Kitchen")

    elif Vegetarian == "yes" and Vegan == "no" and Gluten_Free == "yes":
        print("Here are your restaurant choices: \n  Main Street Pizza Company \n  Corner Cafe \n  The Chef's Kitchen")

    elif Vegetarian == "no" and Vegan == "yes" and Gluten_Free == "no":
        print("Here are your restaurant choices: \n  Corner Cafe \n  The Chef's Kitchen")

    print("")
    response = input("Enter 'yes' if you want to do another restaurant search {enter 'no' to end}: ").lower()
    print("")
    
    

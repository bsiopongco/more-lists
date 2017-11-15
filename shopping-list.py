"""
Goal: Create code to allow a user to create a shopping list
Minimum requirements:
  * User can enter items which will be stored in the shopping list
  * User can exit item entry mode, which will cause the program to print the contents of the list
Stretch goals:
  * User can delete an item from the list
  * A command user can enter at any time to display the contents of the list

Advice:
  * You want to continue doing this for an unknown number of repetitions - what sort of loop would you use?
  * Remember that break will take you out of a loop, so you could say that if some string were entered - for instance 'exit' - you would do something and exit the loop
  * You're probably going to want to use input() and shopping_list.append()
  * Remember to do this one step at a time.
    * Make sure you can add a single item before you try to loop it.
    * Make sure the loop is working before you worry about how to do more advanced things

There is no automated checking on this one
"""
# Printing message for user
print("Let's make a grocery list!")


# defining grocery_list as a list
grocery_list = []

# defining answer as input question
# add .lower at the end of input to convert string to all lowercase letters
answer = input("Would you like to add something to your list?").lower()


# creating an if statement if answer == yes
if answer == "yes":

# creating a while loop that allows user to add items to list and then prints list out
    while True:

        # item is set as input variable for what user would like to add
        item = input("what would you like to add to your list?")


        # adds item to end of the list and prints the list out
        grocery_list.append(item)
        print(f"{grocery_list}")
        answer = input("would you like to add something else?").lower()
        if answer == "no":
            print("have a nice day!")
            break
else:
    print("have a nice day!")







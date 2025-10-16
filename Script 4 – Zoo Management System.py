# The authentication function prompts the user to enter the admin credntials. 
# Only if entered credentials match with the ones stored in the database, it sets the authenticated boolean to true. 
# Otherwise it is false as they do not have the proper admin permission

# In the zoo_creation_menu function it displays a menu for managing zoo creation.
# Regular users do not have access to this section (the authentication boole will be set to false)
# Admin do have access to this section (the authentication boole will be set to true)

# The get_number function is a validation function. It takes a prompt as a parameter
# When used it asks the user to enter a numeric value.
# It will keep asking for input until the user gives a number. 
# It returns the correct output

# The create_zoo fuction only can be accessed by admins
# The authentication boole must be true to access this so regualr users will be denied.
# An admin can create a new zoo by entering its name.
# After this a zoo management menu options.

# The view_settings function displays the zoo name
# If there is no zoo name it tells the user

# The function manage_user_account creates a menu to manage user accounts
# It has options to Add Admin User, Add User, View Users, Delete User and exit
# Depending on the input it directs to the correct function

# The function add_normal_user allows the admin to add a normal user to the database.
# This function asks for a username and password and saved them to the database.

# The add_admin_user function allows the admin to add an admin user to the database.
# This function asks for a username and password and saved them to the database.
# This requires entering admin username and password.

# The view_users function iterates through a list of users stored in the database excluding the zoo names

# The delete_user lets an admin delete a user by entering their username.

# The add_animal function lets an admin add an animal to the zoo database after creating a zoo.
# It asks for the animal's name and tag number and saves to the database

# The find_animal function finds an animal in the database based on its name. 
# When found it prints the animal and tag number that belongs to it

# The get_alphabetic_string is a validation function.
# It takes a prompt as a parameter
# It will keep asking for user input until it consists of alphabetic characters only.
# It returns the correct output
   
# The get_alphanumeric_string fucntion is a validation function
# It takes a prompt as a parameter
# It will keep asking for user input until it consists of alphanumeric characters only.
# It returns the correct output

# The update_zoo function lets an admin user update zoo settings
# The name of the zoo can be updated
# The location can also be updated

# The delete_zoo function lets an admin user delete the zoo from the database.

# The delete_animal enables the admin to search for an animal
# If an animal is found it can be deleted from the zoo database.
# Otherwise it informs the user it is not found

# The admin_zoo_menu function shows a menu for adding, searching, or deleting animals. 
# This can only be done by admins, depending on the option chosen it goes to the relevant function.

# In the main function it ensures that the filename has been takes as an argument. 
# If there is no admin then it prompts the user to create one
# It opens the first menu and prompts for user input

# Sources: Lab 10, Lecture 11, 16, 17

import shelve
import sys


def authentication(zooDB):
    # Getting admin login details
    admin_username = get_alphabetic_string("Enter admin username: ")
    admin_password = get_alphanumeric_string("Enter admin password: ")
    authenticated = False  # set to false by default

    # checking if they exist
    if admin_username in zooDB and zooDB[admin_username] == admin_password:
        authenticated = True
    else:
        print("Admin authentication required.")  # getting admin details if none exist
        username = get_alphabetic_string("Enter admin username: ")
        password = get_alphanumeric_string("Enter admin password: ")
        if admin_username in zooDB and zooDB[admin_username] == admin_password:
            authenticated = True
        elif username == admin_username and password == admin_password:
            authenticated = True
            print("Authentication success!")
            zooDB[admin_username] = admin_password  # updating database with admin
        else:
            print("Access denied.")
            return False
    return authenticated


def zoo_creation_menu(zooDB, authenticated, ZOO_NAME):
    # If you are not an admin you cannot access this menu
    if not authenticated:
        print("Access denied.")  # print message and leave menu
        return

    print("\nManage Zoo Creation Menu:")
    print("1. Create Zoo")
    print("2. View Settings")
    # Submenu
    if authenticated:  # showing these options if the user is admin
        print("3. Update Zoo")
        print("4. Delete Zoo")
    print("5. Return")

    choice = int(get_number("Select an option: "))

    if choice == 1:
        create_zoo(zooDB, authenticated, ZOO_NAME)
    elif choice == 2:
        view_settings(zooDB, ZOO_NAME)
    elif authenticated and choice == 3:
        update_zoo(ZOO_NAME, authenticated)
    elif authenticated and choice == 4:
        delete_zoo(ZOO_NAME, authenticated)
    elif choice == 5:
        return
    else:
        print("Choose a number from 1-5")


# For validation, it returns a number only as input
def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print("Please enter a numeric value.")

    return number


def create_zoo(zooDB, authenticated, ZOO_NAME):
    # If you are not an admin you cannot access this menu
    if not authenticated:
        print("Access denied.")  # print message and leave menu
        return

    zoo_name = input("Enter the name of the zoo: ")
    zooDB[ZOO_NAME] = zoo_name
    print("Zoo created successfully.")
    admin_zoo_menu(zooDB)


def view_settings(zooDB, ZOO_NAME):
    print("\nView Settings:")
    if ZOO_NAME in zooDB:
        print("Zoo Name:", zooDB[ZOO_NAME])
    else:
        print("Zoo name not set")
    print("Return to top-level menu.")


def manage_user_account(zooDB):
    print("\nManage User Account Menu:")
    print("1. Add Admin User")
    print("2. Add User")
    print("3. View Users")
    print("4. Delete User")
    print("5. Return to menu.")

    choice = int(get_number("Select an option: "))

    if choice == 1:
        add_admin_user(zooDB)
    elif choice == 2:
        add_normal_user(zooDB)
    elif choice == 3:
        view_users(zooDB)
    elif choice == 4:
        delete_user(zooDB)
    elif choice == 5:
        return
    else:
        print("Enter a number from 1-5")


def add_normal_user(zooDB):
    # Checking for correct input by passing to validation functions
    username = get_alphabetic_string("Enter username: ")
    password = get_alphanumeric_string("Enter password: ")

    # Adding to database if inputted correctly
    if username.isalpha():
        zooDB[username] = password  # Source: Lecture 16 - Slide 7
        print("User added successfully.")
    else:
        print("Input Error!\nUsername must contain only characters\n")


def add_admin_user(zooDB):
    # Checking for correct input by passing to validation functions
    admin_username = get_alphabetic_string("Enter admin username: ")
    admin_password = get_alphanumeric_string("Enter admin password: ")

    # Adding to database if inputted correctly
    if admin_username.isalpha() and admin_password.isalnum():
        zooDB[admin_username] = admin_password  # Source: Lecture 16 - Slide 7
        print("Admin user added successfully.")
    else:
        print("Input Error!\nUsername must contain only characters\n"
              "Password must be a mix of characters and numbers.\n")


# Printing the list of users stored in the database
def view_users(zooDB):
    print("\nList of Users:")
    # Iterating through each user in the zoo database
    for key, value in zooDB.items():
        if key != "zoo_name":
            print(key)


def delete_user(zooDB):
    username = input("Enter the username to delete: ")
    # Finding the user in the zoo database
    if username in zooDB:  # Source: Lecture 16 - Slide 7
        del zooDB[username]  # removes name from database
        print(f"User {username} deleted successfully.")
    else:
        print(f"User {username} not found.")
    return


def add_animal(zooDB):
    # Checking for correct input by passing to validation functions
    name = get_alphabetic_string("Enter animal name: ")

    # If the animal name is already found in the database it lets the user know
    if name in zooDB:
        print(zooDB[name] + " belongs to the  " + name)  # Source: Lecture 16 - Slide 7
    else:  # Otherwise it lets the user add the animal to database
        print(name + " has not been entered before.\n Would you like to add this animal? ")
        tagNO = get_alphanumeric_string("Enter tag number: ")  # validating input
        zooDB[name] = tagNO  # saving data to database


def find_animal(zooDB):
    print("\nFind Animal:")
    while True:
        tag = input("Enter the animal tag or finish to exit: ")
        if tag.lower() == 'finish':
            break
        if tag in zooDB:  # Source: Lecture 16 - Slide 7
            print(f"Animal found: tag number {zooDB[tag]}, Name: {tag}")
        else:
            print(f"No animal found with name {tag}.")


# checking that what the user has entered is all alpha string
# If it does not meet the requirements it will keep prompting the user for input until it is correct
def get_alphabetic_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isalpha():
            return user_input
        else:
            print("Invalid input.\nEnter an alphabetic string.\n")


# checking that what the user has entered is a mix of numbers and letters
# If it does not meet the requirements it will keep prompting the user for input until it is correct
def get_alphanumeric_string(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isalnum():
            return user_input
        else:
            print("Invalid input.\nEnter an alphanumeric string.\n")


def update_zoo(zooDB, ZOO_NAME):
    print("\nUpdate Zoo:")
    print("1. Update Zoo Name")
    print("2. Update Location")
    print("3. Return")

    choice = int(get_number("Select an option: "))

    if choice == 1:
        new_zoo_name = get_alphabetic_string("Enter new zoo name: ")
        zooDB[ZOO_NAME] = new_zoo_name  # Source: Lecture 16 - Slide 7
        print("Zoo name updated.")
    elif choice == 2:
        new_location = get_alphabetic_string("Enter the new zoo location: ")
        zooDB['location'] = new_location
        print("Zoo location updated.")
    elif choice == 3:  # exiting
        return
    else:
        print("Invalid choice. Choose a number from 1-3.")


def delete_zoo(zooDB, ZOO_NAME):
    print("\nDelete Zoo:")
    confirmation = input("Are you sure you want to delete the zoo? (yes/no): ")
    print("!!!\t\t\tThis cannot be undone\t\t\t!!!")

    # If input matches yes then delete zoo from database
    if confirmation.lower() == "yes":
        del zooDB[ZOO_NAME]  # Source: Lecture 16 - Slide 7
        print("Zoo deleted successfully.")
    else:  # otherwise don't delete the zoo
        print("Zoo was not deleted.")


def delete_animal(zooDB):
    print("\nDelete Animal:")
    animal_name = get_alphanumeric_string("Enter the name of the animal to delete: ")  # validating input

    # If the name entered matches one in the database then remove it
    if animal_name in zooDB:  # Source: Lecture 16 - Slide 7
        del zooDB[animal_name]  # Deleting the name from the database
        print(f"We are sad to see {animal_name} go!")
        print(f"Animal {animal_name} deleted successfully.")
    # Otherwise tell the user it wasn't found
    else:
        print(f"Animal {animal_name} not found in the database.")


def admin_zoo_menu(zooDB):
    while True:
        print("\nAdmin Zoo Menu:")
        print("1. Add Animal")
        print("2. Search for Animal")
        print("3. Delete Animal")
        print("4. Exit")

        choice = int(get_number("Select an option: "))

        if choice == 1:
            add_animal(zooDB)
        elif choice == 2:
            find_animal(zooDB)
        elif choice == 3:
            delete_animal(zooDB)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Enter a number from 1-4")


def main():
    # Making sure the user enters the file name for the database
    if len(sys.argv) != 2:  # Source: Lecture 17 - Slide 20
        print("Enter the database file name as an argument.\n")
        sys.exit()  # Source: Lab 10 - Question 2

    database_name = sys.argv[1]  # getting the name passed as an argument

    ZOO_NAME = "Yoto Zoo"  # Default zoo name until
    zooDB = {}
    shelfObj = shelve.open(database_name)
    if "zooDB" in shelfObj:
        zooDB = shelfObj["zooDB"]

    # Getting admin details for the first time if no admin user exists
    if "admin" not in zooDB:
        print("Create an admin user.")
        add_admin_user(zooDB)

    # Getting admin details for first time
    authentication_boolean = authentication(zooDB)

    while True:
        print("\nTop-level Menu:")
        print("1. Manage Zoo Creation")
        print("2. Manage User Account")
        print("3. Exit")

        choice = int(get_number("Select an option: "))

        if choice == 1:
            if authentication_boolean:  # Check if user is authenticated
                create_zoo(zooDB, authentication_boolean, ZOO_NAME)
            else:
                print("Access denied.")  # Print message if not authenticated
        elif choice == 2:
            if authentication_boolean:
                manage_user_account(zooDB)
            else:
                print("Access denied.")  # Print message if not authenticated
        elif choice == 3:
            shelfObj["zooDB"] = zooDB
            shelfObj.close()
            print("Data saved. Exiting program...")
            sys.exit(0)
        else:
            print("Invalid choice. Choose a number from 1-3")


if __name__ == "__main__":
    main()

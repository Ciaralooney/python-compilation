# My plan was to get the user input for the list in the main function.
# Then create 2 functions that take this list as a parameter.

# First in the main function the user is asked to enter the list contents.
# The user can choose to stop at anytime.
# After this it will print the list and then the list is sent as a parameter into the check_hash function.

# In the check_hash function it goes through each word in the list.
# If checks if there is a # anywhere in the word and the first char in the word does not equal m.
# If both of these conditions are met then it'll print saying that the word contains hash mark and doesn't start with m.

# The same list is sent as a parameter into the common_char function.
# This function finds common characters present in all words in the list and counts them.
# It prints out the common characters and how many times they are present for every word in the list.

# I have listed my sources as I referenced them throughout my code.

def check_hash(hash_list):

    print("Hash marks and no m check:")
    for word in hash_list:  # Source: Slide 18 - Lecture 13
        # Checking if the word has a # and doesn't start with m
        if '#' in word and word[0] != 'm':
            print(f"{word} contains hash mark and does not start with m")


def common_char(char_list):
    # Creating empty list for common characters
    common_chars = []

    for char in char_list[0]:  # getting all chars from the first word
        char_exists_in_all = True  # assuming the char is in all words initially

        # checking if the character exists in all the other words
        for word in char_list[1:]:  # Source: Slide 9 - Lecture 13
            if char not in word:  # If it's not found it's not common. Break loop
                char_exists_in_all = False
                break
        # if the char is common to all words on not on the list then add it
        if char_exists_in_all and char not in common_chars:
            common_chars.append(char)  # Appending to list

    if common_chars:
        print("\nCommon character check:")
        # Going over each common character
        for char in common_chars:
            print(f"\nCharacter {char} appears in all items")
            # Going over each word
            for word in char_list:
                # Counting how many times the common character is in the list
                count = word.count(char)
                print(f"{word} contains {count} {char}")
    else:
        print("There are no common characters.")  # If loop is broken this is printed


if __name__ == '__main__':

    my_list = []

    # while loop should always be before user input so the input is always checked.
    while True:
        user_input = input("Do you want to add a value to the list? y or n ")
        if user_input == "y":  # if the user input a y
            value = input("Enter a value: ")  # asking the user for a value
            my_list.append(value)  # appending the list with the value
        else:
            break  # break the while loop if they don't want to return anything else

    print(f"Your full list is: {my_list}\n")

    check_hash(my_list)
    common_char(my_list)

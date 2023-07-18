# COP3502C-Lab6
# Author: Alexis Morales
# Author: Maria Moncada
# Date: July 18, 2023


def decode(num):
    # defining each input more than 10,11,12,13
    # increasing the value of 'i'
    if num == 10:
        i = 0
    elif num == 11:
        i = 1
    elif num == 12:
        i = 2
    elif num == 13:
        i = 3
    else:
        i = num
    # if none of the above, 'i' still being the same
    # return the new value of 'i'
    return i


def new_password(password):
    # making the new_password act as a list
    new_password = list()
    for i in password:
        i = int(i) + 3
        # append the value of 'i' to the list
        new_password.append(str(decode(i)))
    # making a new variable for the new password called 'new_pass'
    new_pass = "".join(new_password)
    # return new_pass
    return new_pass


def main():
    new_pass = ""
    old_password = ""
    while True:
        print("\nMenu"
              "\n-------------" 
              "\n1. Encode" 
              "\n2. Decode" 
              "\n3. Quit")
        # display the menu
        option = int(input("Please enter an option: "))
        # ask the user to select an option from the menu
        if option == 1:
            print("Please enter your password to encode:", end=" ")
            old_password = [x for x in input()]
            print("Your password has been encoded and stored!")
            # store the new password without printing it
            new_pass = new_password(old_password)
            # continue the program
            continue

        old_password = "".join(old_password)
        # making the old password a string instead of an int
        if option == 2:
            # print the new password and the old password
            print(
                f"The encoded password is {new_pass}, and the original password is {old_password}."
            )
        if option == 3:
            # break the program
            return


if __name__ == "__main__":
    main()
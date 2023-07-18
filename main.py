# COP3502C-Lab6
# Author: Alexis Morales
# Author: Maria Moncada
# Date: July 18, 2023


def decode(num):
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

    return i


def new_password(password):
    new_password = list()
    for i in password:
        i = int(i) + 3
        new_password.append(str(decode(i)))

    new_pass = "".join(new_password)

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

        option = int(input("Please enter an option: "))

        if option == 1:
            print("Please enter your password to encode:", end=" ")
            old_password = [x for x in input()]
            print("Your password has been encoded and stored!")

            new_pass = new_password(old_password)
            continue

        old_password = "".join(old_password)

        if option == 2:
            print(
                f"The encoded password is {new_pass}, and the original password is {old_password}."
            )
        if option == 3:
            return


if __name__ == "__main__":
    main()
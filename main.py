def decoded(encoded_num):
    decoded_num=""
    for i in str(encoded_num):
        i=int(i)-3
        decoded_num+=str(i)
    return decoded_num


def encoder(u_input):
    e_password = ""
    for i in range(0, len(u_input)):
        encode_letter = int(u_input[i])
        if 0 <= encode_letter <= 6:
            encode_letter += 3
        elif encode_letter == 7:
            encode_letter = 0
        elif encode_letter == 8:
            encode_letter = 1
        elif encode_letter == 9:
            encode_letter = 2
        else:   # This else statement is here in case a non-numeric character is an input
            print("Incorrect value entered - Try again")
            break
        encode_letter = str(encode_letter)
        e_password += encode_letter
    return e_password  # e_password stands for encode password


program = 1     # The variable program is called program because it's what keeps the program running
while program != 0:     # The while loop is made like this so it only ends when option 3 is selected
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")
    user_input = input("Please enter an option:\n")

    if user_input == '1':
        password = input("Please enter your password to encode:\n")
        e_p_word = encoder(password)    # e_p_word stands for encoded password
        print("Your password has been encoded and stored!")

    elif user_input == '2':
        password = input("Please enter your password to decode:\n")
        d_p_word = decoder(password)    # d_p_word stands for decoded password
        print(f"The encoded password is {d_p_word}, and the original password is {password}.")

    elif user_input == '3':
        program = 0     # The variable program is changed to 0 so that the while loop stops

    else:
        # This else statement is here in the case the use inputs an invalid option during menu selection
        print("Invalid Option -- Please Try Again")

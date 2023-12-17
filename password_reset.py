command = input()
main_string = input()
letters_list = []
while main_string != "Done":
    new_command = main_string.split()
    nothing_to_replace = False

    if new_command[0] == "TakeOdd":
        command = command[1::2]
    elif new_command[0] == "Cut":
        index, lenght = new_command[1], new_command[2]
        index, lenght = int(index), int(lenght)
        command = f"{command[:index]}{command[index+lenght:]}"

    elif new_command[0] == "Substitute":
        substring, substitute = new_command[1], new_command[2]
        if substring in command:
            command = command.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            nothing_to_replace = True
    if not nothing_to_replace:
        print(command)
    main_string = input()

print(f"Your password is: {command}")



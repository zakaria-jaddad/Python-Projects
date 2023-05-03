def main():

    string = input("Write A Binary Here : ")
    # checking the length of the string is a valid lenght
    if len(string) % 8 != 0:
        return print("Your Input Is Not A Valid Binary")
    # checking if the sting contin chars 
    for char in string:
        if char != "0" and char != "1":
            return print("Your Input Is Not A Valid Binary 2")
    # making a loop for iterating every 8 digits
    counter = 0 #for the iteration in the string 
    time = len(string) // 8
    BINARY = [] # to store the final resualt
    for i in range(time):
        result = 0
        for j in range(7, -1, -1):
            result += int(string[counter]) * pow(2, j)
            counter += 1
        BINARY.append(chr(result))

    result = ''.join(BINARY)
    print(result)



if __name__ == "__main__":
    main()
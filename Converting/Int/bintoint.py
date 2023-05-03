def main():
    print("Welcom To The Binary Converter")
    print("Youre Binary Will Be Converted To Integer")
    numbers = input("Give An Int : ")

    # checking 
    for number in numbers:
        if number != "0" and number != "1":
            return print("Your Input Is Not A Valid Binary Code")
    # reversing the list 
    numbers = numbers[::-1]

    # counter for the power 
    counter = 0
    # result
    result = 0

    for i in numbers:
        result += int(i) * pow(2, counter)
        counter += 1

    print(result)



if __name__ == "__main__":
    main()
def main():
    # GLOBAL VARIBELS 
    FINAL_RESULT = []


    # getting the input or the number

    numbers = (input("Give AN Emote Or What Ever : "))

    # set num to one for the multiplication
    for number in numbers:

        # how many number to get to the inputs number
        number_counter = [1]
        # the result list that i'm goona join it 
        result = []

        # converting number to its decimal value 
        number = ord(number)

        num = 1
        # start iterating 
        while True:
            # if the resault of next multiplication is greater than the number 
            if num * 2 > number:
                break
            # if not then multiplay it 
            num *= 2
            # add it to the list 
            number_counter.append(num)
        # assignign the zeros to list 
        # reversing the list 
        number_counter = number_counter[::-1]

        # the starting place of the list 
        index = len(result) - len(number_counter)

        for i in number_counter:
            result.append(0)

        if number != 0:
            rest = number - number_counter[0]
            result[index] = 1

        for i in number_counter[1:]:
            if rest >= i:
                result[index + 1] = 1
                rest -= i
            index += 1

        # printing list 
        FINAL_RESULT.append(''.join(str(x) for x in result))
    FINAL_RESULT = ' '.join(FINAL_RESULT)
    print(FINAL_RESULT)
    return


if __name__ == "__main__":
    main()
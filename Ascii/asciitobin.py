def main():
    # getting the inout from user 
    FINAL_RESULT = []
    string = input("Give A String : ")

    # itterating in every char in the string
    for char in string:
        # For DLOBAL VARIBELS 
        number_counter = [1]
        result = [0, 0, 0, 0, 0, 0, 0, 0]

        char = int(ord(char))
        # set num to one for the multiplication
        num = 1
        # start iterating 
        while True:
            # if the resault of next multiplication is greater than the number 
            if num * 2 > char:
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

        if char != 0:
            rest = char - number_counter[0]
            result[index] = 1

        for i in number_counter[1:]:
            if rest >= i:
                result[index + 1] = 1
                rest -= i
            index += 1

    # printing list 
        FINAL_RESULT.append(''.join(str(x) for x in result))
    FINAL_RESULT = ''.join(FINAL_RESULT)
    print(FINAL_RESULT)
            
    return


if __name__ == "__main__":
    main()
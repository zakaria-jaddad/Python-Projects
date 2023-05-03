def main():
    FINAL_RESULT = []

    # getting the inout
    print("Please Provide Spaces Between The each code")
    string = input("Give A Binary Code : ").split()
    for number in string:
        # declaring the counter for the power
        counter = 0
        result = 0
        # reversing the number 

        number = number[::-1]

        # strt etterating 
        for i in number:
            result += int(i) * pow(2, counter)
            counter += 1

        # getting the unicode value from the result 
        FINAL_RESULT.append(chr(result))
    # joinning the strings with each other
    FINAL_RESULT = ''.join(FINAL_RESULT)
    print(FINAL_RESULT)
    return


if __name__ == "__main__":
    main()
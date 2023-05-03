def main():
    # ok here is the thing here
    # so first take the input (number from the user)
    #   the number could be an ascii number or a integer 
    # start from 1 and dauble it untile you hit it or you be over it 
    #   store every number in a list to access it easely 
    # than in every number see if you can substract it until you hit 0
    # HERE IS AN EXAMPLE i have 14 an integer 
        # the proccess 1 - 2 - 4 - 8 - 16 so here i'm gonna 
        # stop in 8 because the dauble of 8 is 16 and if i use 16 i will get a negative number while doing the math
    # so here 14 == 8 + 4 + 2
    # in other hand i can do it like this 14 - 8 == 4 && 4 - 4 == 0 onece you hit zero it is done
    # the logic of this is if the number >= to the list[i] where i the index of that number than substract it 
        # if you hit 0 or the number that you got from a pruvius sub is < than number[i] than go to the next nubmber 


        # making the list to store the values of numbers that going to be substracter from the input 

    number_counter = [1]
    result = []
    # getting the input or the number
    print("Answer with Yes Or No")
    boolyan = input("Do You Want To Convert Unicode To Binary ").upper()

    if boolyan == "YES":
        number = ord(input("Give AN Emote Or What Ever : "))
    else:
        number = int(input("give A Decimal Number : "))

    # set num to one for the multiplication
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
    final_result = ''.join(str(x) for x in result)
    print(final_result)
    return


if __name__ == "__main__":
    main()
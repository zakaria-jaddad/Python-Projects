def main():
    # if argc == 0 then return erreur 
    # give a numer 
    # turn it to string
    # check weather there is or not a "0x" in the head of the hex string  and if the rest are numbers 
    # & the rest of the numbers after the "0x" are just a numbers IDK HOW TO DO IT I MIGHT JUST GOOGLE IT 
    # if there is than => # iterate in the string ones at a time starting fro the ending
    # if not => return this is not a valid hex number
        # after starting from the end take the the number and multiplay it to (16)ˆi
    # where i is just a loop from i=0 => i=n and n = lenght of the string(number - 2 where the 2 is just ("0x"of the number))
    # CREATE a global variable where in every iteration you add the value of the new number 

    HEX_NUM = {
        "a" : "10",
        "b" : "11",
        "c" : "12",
        "d" : "13",
        "e" : "14",
        "f" : "15"
    }
    INT_NUM = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    # getting a hex
    # print("GIVE ME A NUMBER WITH 0x")
    # hex_num = input("Give Me A HEX : ")
    print("GIVE ME A DECIMAL NUMBER")
    hex_num = input("Give Me A HEX : ")

    def hextoint(num):
        RESULT = 0 
        counter = 0
        num_len = len(num)
        if num_len == 0 or (num[0] != "0" and num[1] != "x"):
            return "This is not a valid Hex number"
        for i in range(num_len-1, 1, -1):
            if num[i].lower() in HEX_NUM:
                RESULT += int(HEX_NUM[num[i].lower()]) * pow(16, counter)
            elif num[i].isnumeric():
                RESULT += int(num[i]) * pow(16, counter)
            else:
                return "Your Number Is Not A Valid HEX Number"
            counter += 1
        return RESULT
    
    print(hextoint(hex_num))

if __name__ == "__main__":
    main()

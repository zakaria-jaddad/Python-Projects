def main():

    INT_NUM = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    dec_num = input("Give Me A DECIMAL : ")

    
    def inttohex(num):
        # division of the number
        div = int(num) // 16
        remainder = int(num) % 16
        
        # checking if thr division is 0
        if div == 0:
            full_number = []
            full_number.append(remainder)
            return full_number
        
        # recursion
        rem = inttohex(div)
        rem.append(remainder)
        return rem

    # print((hextoint(hex_num)))
    place = inttohex(dec_num)
    ana = ""
    for numbers in place:
        if numbers in INT_NUM:
            ana = ana + str(INT_NUM[numbers])


    print(ana)

if __name__ == "__main__":
    main()

def count_loop(line):
    count = 0
    for char in line:
            count += int(char)
    if (len(str(count)) > 1):
         count_loop(str(count))
    else:
         print(count)

def digit_of_life():
    line = input("Please input your full birthday date.\n")
    count = 0
    if (not line.isnumeric()):
        "Please input only numbers."
    elif (len(line) != 8):
        "Please input an 8 digit birth date."
    else:
        count_loop(line)
    

        #recursion? base case length 1, else call it again on current count
    
        
digit_of_life()
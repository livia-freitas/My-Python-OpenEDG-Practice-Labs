def palindrome():
    line = input("Please input some text.\n")
    i = 0
    j = i + 1
    k = -j
    check = 0
    for char in line:
        if (line[i] == line[k]):
            i+=1
        else:
            check += 1
            i+=1
            print(line[i] + " is not equal to " + line[k])
    if (check == 0):
        print("It's a palindrome\n")
    else:
        print("It's not a palindrome\n")
    
        
        
palindrome()
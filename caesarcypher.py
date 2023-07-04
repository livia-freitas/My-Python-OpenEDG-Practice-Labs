def caesar_improved():
    line = input("Please input a line of text to encrypt:")
    value = input("Please input an integer shift value between 1 and 25: ")
    cypher = []
    while (not value.isnumeric()) or (float(value) > 25) or (float(value) < 1): 
        value = input("Please input a valid shift value.")
    shift = int(value)
    for char in line:
        if not char.isalnum():
            cypher.append(char)
        else:
            encrypt = ord(char) + shift
            if(97 > encrypt > 90) or (encrypt > 122):
                encrypt -= 26
            encrypted = chr(encrypt)
            cypher.append(encrypted)
    output = ''.join(cypher)
    print(output)

caesar_improved()
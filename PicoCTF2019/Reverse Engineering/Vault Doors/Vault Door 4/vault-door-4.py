def main():
    myBytes = [
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o146, 0o64 ,
            'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,
    ]
    pw = ""
    for i in myBytes:
        if type(i) == str: #check if the value is a character from the last row
            pw = pw + i #add new character to the existing string
        else:
            pw = pw + chr(i) #convert the integer into a character and add it to the string
    print(pw) #show me the password
    
main()
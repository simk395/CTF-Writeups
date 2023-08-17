def main():
    decimal = [1096770097, 1952395366, 1600270708, 1601398833,
            1716808014, 1734293296, 842413104, 1684157793]
    
    bitstring = ""
    for i in decimal:
        bitstring = bitstring + format(i, '032b')
    
    print(bitstring)
    pw = ""
    val = ""
    for i in range(0, len(bitstring)):
        val = val + bitstring[i]
        if (i+1) % 8 == 0:
            val = chr(int(val, 2))
            pw = pw + val
            val = ""

    print(pw)
main()
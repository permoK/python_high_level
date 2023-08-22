import sys
def roman_to_int(roman_string):
    n = []
    romans = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,       
        "V": 5,
        "I": 1,
        }
    try:
        length = len(roman_string)
        for i in range(length):
            current = i
            next = i+1
            if next == length:
                next = i
                
            if romans[roman_string[current]] >= romans[roman_string[next]]:
                n.append(romans[roman_string[current]]*1)
            elif romans[roman_string[current]] < romans[roman_string[next]]:
                n.append(romans[roman_string[current]]*-1)
            
        roman_number = sum(n)
        print(roman_number)
    except KeyError:
        print(0)
        sys.exit(1)
    
roman_string = 'MMI'
roman_to_int(roman_string)


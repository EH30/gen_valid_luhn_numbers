import random

# Author: EH
# Educational Purposes Only 
# i am not responsible for you're actions
#-------------------------------------------------

# The logic behind this is simple
# first we generate random numbers from 1 to 9 and store it in an array
# until the length of that array reaches 16
# then we check how much value we need to remove to make it divisible by 10 
# after that we remove those value from the odd positions in array 

# This function returns the remainder
def luhn(num):
    if type(num) != str:
        num = str(num)
    else:
        num = num.strip()
    
    res = 0
    sec = False
    for i in range(len(num)-1, -1, -1):
        a = int(num[i])
        if sec:
            a = a*2
            if a > 9:
                res += a-9
                sec = False
                continue
            res += a
            sec = False
        else:
            res += a
            sec = True
    
    return res%10


# This function generates random numbers from 0 to 9
def gen_digits(length):
    out = []
    for i in range(length):
        out.append(str(random.randint(0, 9)))
    return out

def gen_val():
    digits = gen_digits(16)
    rem = luhn("".join(digits))
    pos = 0 # store the randomly picked position
    temp = 0 # store the number in that position as integer

    while rem > 0:
        pos = random.randint(0, len(digits)-1) 
        if digits[pos] == "0" or pos%2 == 0: # skip 0 and second digits 
            continue

        temp = int(digits[pos])
        if temp >= rem: # checks if the value is >= to the value we need to remove  
            digits[pos] = str(temp-rem)
            rem = 0
        else:
            rem -= 1
            temp -= 1
            digits[pos] = str(temp)
    
    return "".join(digits)


if __name__ == "__main__":
    print(gen_val())

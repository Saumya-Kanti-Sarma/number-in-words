numbers = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100:'hundred',
    1000:'thousand',
    100000:'lakh',
    10000000:'crore',
}
i = '875'
# for default
if int(i) in numbers:
    print(numbers[int(i)])

# 0-9
elif int(i) >0 and int(i) <10:
    print(numbers[int(i)])
    
# 13-19
elif int(i) >12 and int(i) <20:
    num = i[1]
    print(f"{numbers[int(num)]}teen")

#20-99    
elif int(i) >20 and int(i) <100:
    x = []
    for char in i:
        x.append(char)
        x.append('0')
    x.pop()
    
    first2digit = int(int("".join(x))/10)
    lastDigit = int(int("".join(x))%10)
    # print(first2digit)
    # print(lastDigit)
    print(f"{numbers[int(first2digit)]} {numbers[lastDigit]}")

#101-999
elif int(i) >100 and int(i)<1000:
    # 541
    # 540
    # 501
    f = int(i[0])
    m = int(i[1]+'0')
    l = int(i[2])
    if l == 0:
        print(f"{numbers[f]} {numbers[100]} and {numbers[m]}")
    elif m == 0:
        print(f"{numbers[f]} {numbers[100]} and {numbers[l]}")
    else:
        print(f"{numbers[f]} {numbers[100]} and {numbers[m]} {numbers[l]}")

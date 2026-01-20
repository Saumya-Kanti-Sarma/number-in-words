ds ={
  0: 'zero',  1: 'one',  2: 'two',  3: 'three',  4: 'four',  5: 'five',  6: 'six',  7: 'seven',  8: 'eight',  9: 'nine',  10: 'ten',  11: 'eleven',  12: 'twelve',  13: 'thirteen',  14: 'fourteen',  15: 'fifteen',  16: 'sixteen',  17: 'seventeen',  18: 'eighteen',  19: 'nineteen', 20: 'twenty',  30: 'thirty',  40: 'forty',  50: 'fifty',  60: 'sixty',  70: 'seventy',  80: 'eighty',  90: 'ninety'
}

words = []
def generate_word(num):
  if int(num) in ds:
    words.append(ds[int(num)])
  else:
    str_num = str(num)

    # 2 digit number (tens)
    if len(str_num) == 2: 
      n1 = int(str_num[0]+"0")
      words.append(ds[int(n1)])
      return generate_word(int(str_num[1]))
    
    # 3 digit number: (hundreds)
    elif len(str_num) == 3:
      n1 = int(str_num[0])
      words.append(f"{ds[int(n1)]} hundred")
      return generate_word(int(str_num[1:3]))
    
    # 4 digit number: (thousands)
    elif len(str_num) == 4:
      n1 = int(str_num[0])
      words.append(f"{ds[int(n1)]} thousand")
      return generate_word(int(str_num[1:4]))
    
    # 5 digit number: (ten-thousands)
    elif len(str_num) == 5:
      n1 = int(str_num[0:2])
      words.append(f"{ds[int(n1)]} thousand")
      return generate_word(int(str_num[2:5]))
    
    # 6 digit number: (hundred-thousands) 132432
    elif len(str_num) == 6:
      n1 = int(str_num[0])
      words.append(f"{ds[int(n1)]} hundred {ds[int(str_num[1]+"0")]} {ds[int(str_num[2])] } thousand")
      return generate_word(int(str_num[3:6]))
    
    # 7 digit number: (million)
    elif len(str_num) == 7:
      n1 = int(str_num[0])
      words.append(f"{ds[int(n1)]} million")
      return generate_word(int(str_num[1:7]))
    
    # 8 digit number: (ten-million)
    elif len(str_num) == 8:
      n1 = int(str_num[0:1])
      words.append(f"{ds[int(n1)]} million")
      return generate_word(int(str_num[2:8]))
    
    # 9 digit number: (hundred-million) 123456789
    elif len(str_num) == 9:
      n1 = int(str_num[0])
      words.append(f"{ds[int(n1)]} hundred {ds[int(str_num[1]+"0")]} {ds[int(str_num[2])] } million")
      return generate_word(int(str_num[3:9]))
    
    # 10 digit number: (billion)
    elif len(str_num) == 10:
      n1 = int(str_num[0])
      words.append(f"{ds[int(n1)]} billion")
      return generate_word(int(str_num[1:10]))
    
    # 8 digit number: (ten-billion)
    elif len(str_num) == 8:
      n1 = int(str_num[0:1])
      words.append(f"{ds[int(n1)]} billion")
      return generate_word(int(str_num[2:8]))
    
    # 9 digit number: (hundred-billion) 123456789
    elif len(str_num) == 9:
      n1 = int(str_num[0])
      words.append(f"{ds[int(n1)]} hundred {ds[int(str_num[1]+"0")]} {ds[int(str_num[2])] } billion")
      return generate_word(int(str_num[3:9]))

  str1 = " ".join(words)
  str1 = str1.replace("zero", "")
  str2 = str1.replace("  ", "")
  words.clear()
  return str2.lower()
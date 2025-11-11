from ds import ds as d

def tens(x:int)-> str:
  if x in d:
    return d[x]
  # 14-19
  if x >13 and x<20:
    x %= 10 #14 %10 = 4
    return f"{d[x]}teen"
  #21-99 except 10 multiples 
  elif x >20 and x%10 !=0 and x <100:
    fd = x // 10 #23 // 10 = 2 
    ld =  x%10 #23 % 10 = 3
    return f"{d[fd]} {d[ld]}"
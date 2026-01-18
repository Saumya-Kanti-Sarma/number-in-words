from ds import ds as d

def tens(x:int)-> str:
  if x in d:
    return d[x]
  elif x >20 and x <100:
    fd = (x // 10)*10 #23 // 10 = 2 
    ld =  x%10 #23 % 10 = 3
    return f"{d[fd]} {d[ld]}"
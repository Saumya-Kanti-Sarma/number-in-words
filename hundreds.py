from ds import ds as d

def hundreds(x:int) -> str:
  if x in d:
    return d[x]
  n1 = x //100 # 132 // 100 =1
  x %= 100 #132 %100 = 32
  n2 = (x//10)*10 #(32 //10)*10= 30
  x %= 10 # 32 % 10 = 2

  return f"{d[n1]} hundred {d[n2]+' ' if n2 != 0 else ''}{d[x]+' ' if x != 0 else ''}"  
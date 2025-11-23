from millions import millions
from tens import tens
from hundreds import hundreds
def billions (x:int)->str: 
  # Number smaller then 10 billion
  if x < 99999999999:
    n1 = x // 1000000000
    x %= 1000000000
    return f"{tens(n1)} billion {millions(x)}"
  # 10 billion to 999.99 billion
  else:
    n1 = x // 1000000000
    x %= 1000000000
    return f"{hundreds(n1)} billion {millions(x)}"
  
print("Billions")
for i in [1432456734,15676345232,654900000221,50490011007,1000000001,345678123467]:
  print(i,billions(i))
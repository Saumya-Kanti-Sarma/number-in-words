from .ds import ds as d
from hundreds import hundreds
from tens import tens
from thousands import thousands
def main(x:int) -> str:
  if x in d:
    return d[x]
  else:
    if x <= 99:
      return tens(x)
    elif x <= 999:
      return hundreds(x)
    elif x<= 999999:
      return thousands(x)
    else:
      return "Number out of range"

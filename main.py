"""
Given a string as input. Print total number of uppercase and lowercase characters. Note: String can contain non-alphabets.
Input-> "tRiSeCt100"
Output-> Upper=3 Lower=4
"""

st = "tRiSeCt100"
ln = len(st)
total1 = 0
total2 = 0
for i in range(0,ln):
  ch = st[i]
  if(ch>="a" and ch<="z"):
    total1 = total1 + 1
  elif(ch>="A" and ch<="z"):
    total2 = total2 + 1
print(f"Upper:{total2}")
print(f"Lower:{total1}")

s=str(input("Dati un sir:"))
a=s.count("A")
print("Numarul de aparitii ale caracterului 'A' in sir:",a)
if "A" in s:
 for i in s:
    x=s.replace("A","*")
    print("Sirul obtinut in urma substituirii:",x)
else:
    print("x)",s)
if "B" in s:
 for i in s:
    b=s.replace("B","")
    print("Sirul obtinut prin radierea a tuturor aparitiilor caracterului 'B': ",b)
else:
    print("b)",s)
if "MA" in s:
  for i in s:
    c=s.count("MA")
    print("Numarul de aparitii a silabei 'MA': ",c)
else:
    print("c) Nu avem silaba 'MA' in sirul dat")
if "MA"  in s:
  for i in s:
    y=s.replace("MA","TA")
    print("Substituirea silabei 'MA' cu 'TA': ",y)
if "TO" in s:
  for i in s:   
    z=s.replace("TO","")
    print(" Sirul obtinut prin radierea a tuturor aparitiilor silabe 'TO': ",z)
else:
    print("z) ",s)
d=len(s)
g=s[d::-1]
print("d) Sirul invers:",d)


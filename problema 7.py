s=str(input("Dati un sir:"))
a=s.count("A")
print("Numarul de aparitii ale caracterului 'A' in sir:",a)
print(a)
for i in s:
    x=s.replace("A","*")
    print(x)
for i in s:
    b=s.replace("B","")
    print("Sirul obtinut prin radierea a tuturor aparitiilor caracterului 'B' in sir:",b)
c=s.count("MA")
print("Numarul de aparitii ale silabei'MA' in sir:",c)
for i in s:
    y=s.replace("MA","TA")
    print(y)
for i in s:
    d=s.replace("TO","")
    print("Sirul obtinut prin radierea a tuturor aparitiilor caracterului 'TO' in sir:",d)
    z=len(s)
    e=s[s::-1]
    print("Sirul invers:",e)


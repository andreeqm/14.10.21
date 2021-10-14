x=str(input("Sa se introduca sirul de caractere: "))
for i in range(0,len(x)):
    if (ord(x[i])>65)and(ord(x[i])<89):
        print(chr(ord(x[i])+1))
y=x.replace("Z","A")
print(y)
z=x.replace(" ","-")
print(z)





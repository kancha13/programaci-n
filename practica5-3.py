print"dame una nota";
a=float(input())
li=[a]
while a<=10 and a>=0:
    print"dame una nota"
    a=float( input())
    li=li+[a]
li.remove (a)
print li;

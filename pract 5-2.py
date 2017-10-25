print "dame una numero";
a=raw_input()
li=[a]
while a!='':
    print"dame otro numero"
    a=raw_input()
    li=li+[a]
li.remove ('')
print li;

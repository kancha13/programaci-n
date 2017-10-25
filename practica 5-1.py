print "dame una palabra";
a=raw_input()
li=[a]
while a!='':
    print"dame otra palabra"
    a=raw_input()
    li=li+[a]
li.remove ('')
print li;


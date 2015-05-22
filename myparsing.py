#!/Users/aishahunte/anaconda/bin/python

import sys

mykeys = []
i = 0
fn1 = None
speeches = open('list', 'r')

for line in speeches:
    if 'index.html' not in line:
        line = line.replace(".html", "").strip()
        mykeys.append(line)
mykeys = sorted(mykeys)

for line in sys.stdin:   
    if '***' in line:
        if i < len(mykeys):
            fn1 = open('./data/' + str(mykeys[i]) + '.txt', 'w')
            i+=1
    elif fn1 != None:
        fn1.write(line)
    else:
        continue
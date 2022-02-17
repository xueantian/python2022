

for a in range(1,10):
    while a>0:
        print('x', end='\t')
        a-=1
    print()

for a in range(1,10):
    for i in range(1,a+1):
        print('x',end='')
    print()

for a in range(1,10):
    for i in range(1,a+1):
        print(a,'*',(i),'=',int(a*i),end='\t')

    print()



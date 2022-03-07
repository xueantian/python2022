import random

price=random.randint(1000,1050)
print(' the price of this product is (1000-1050):')

i=1
while i <= 10:
    guess = int(input('you have last {} time to try,please input the number:'.format((11-i))))
    if guess > price:
        print('higher,try again!')
    elif guess < price:
        print('lower,try again!!')
    else:
        print('===================================')
        print('good, congratulation!! you got it !!')
        print('===================================')
        break
    i+=1


import os
import time
username = 'admin'
password = 'admin123'
result=1

def write_log(inputusename,result):
    resultcode=''
    if result ==1:
        resultcode='login success'
    elif result == 2:
        resultcode = 'password wrong'
    else:
        resultcode='username wrong'
    with open('login_log.txt','a',encoding='utf-8') as afile:
        s=f'\tusername\t\t:{inputusename},\tlogintime\t:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))},\tlogin_result\t\t:{resultcode}'

        afile.write(s)
        afile.write('\n')
def read_log():
    with open('login_log.txt','r',encoding='utf-8') as rfile:
        while True:
            line=rfile.readline()

            if line == '':
                break
            else:
                print(line)

def input_func():
    i=1
    while i <=3:
        inputusername = input('please input the username:')
        if inputusername == username:
            inputpassword = input('password:')
            if inputpassword==password:
                print('===================================')
                print('Congratulation!,login successfully!!')
                print('===================================')
                result=1
                write_log(inputusername,result)
                break
            else:
                print('===================================')
                print('the password is wrong, please try again')
                print('===================================')
                result = 2
                write_log(inputusername,result)


        else:
            print('===================================')
            print('username is wrong,please try again, leave time to try is {}'.format(3-i))
            print('===================================')
            result = 3
            write_log(inputusername,result)
        i+=1




if __name__ == '__main__':
    while True:
        mode = int(input('please input 0,1 or 2, 0 for quit,1 for login, 2 for view the log:'))
        if mode == 1:
            input_func()

        elif mode == 2:
            read_log()
        elif mode == 0:
            break
        else:
            print('input error, please try again!!')



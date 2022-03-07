import os.path

filename='student.txt'

def menu():
    print('=============================Student information management system======================')
    print('-----------------------------------function chose---------------------------------------')
    print('\t\t\t\t\t\t1.input the student information')
    print('\t\t\t\t\t\t2.search the student information')
    print('\t\t\t\t\t\t3.delete the student information')
    print('\t\t\t\t\t\t4.modify the student information')
    print('\t\t\t\t\t\t5.sort the student information')
    print('\t\t\t\t\t\t6.total the student information')
    print('\t\t\t\t\t\t7.show all the student information')
    print('\t\t\t\t\t\t8.quit')
    print('\n')
    print('=============================Student information management system======================')

def insert():
    student_list=[]
    while True:
        id = input('please input the student ID(1001):')
        if not id:
            break
        name= input('please input the student name(David):')
        if not name:
            break
        try:
            englishcore=int(input('please input the English score(99):'))
            chinesecore=int(input('please input the Chinese score(99):'))
            pythoncore=int(input('please input the Python score(99):'))
        except:
            print('input error, please try again')
            continue
      #save to dict
        student={'id':id,'name':name,'englishcore':englishcore,'chinesecore':chinesecore,'pythoncore':pythoncore}
        student_list.append(student)
        answer=input('do you want to insert more ? Y/N')
        if answer == 'y':
            continue
        elif answer == 'Y':
            continue
        else:
            break

    save(student_list)
    print('insert finish,thank you')



def save(list):
    try:
        stu_list=open(filename,'a',encoding='utf-8')
    except:
        stu_list=open(filename,'w',encoding='utf-8')
    for item in list:
        stu_list.write(str(item)+'\n')
    stu_list.close()

def search():
    student_temp=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=int(input('search on ID input 1, search on Name input 2,other for quit:'))
            if mode == 1:
                id=input('please input the ID:')
            elif mode == 2:
                name=input('please input the name:')
            else:
                print('input error, please try again!!')
                break
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id !='':
                        if d['id'] == id:
                            student_temp.append(d)
                    elif name !='':
                        if d['name'] == name:
                            student_temp.append(d)
            show_student(student_temp)
            student_temp.clear()
            answer=input('do you want to search again ? Y/N')
            if answer == 'y':
                search()
            elif answer == 'Y':
                search()
            else:
                break

        else:
            print('there is no student information yet')

def show_student(list):

    if len(list) ==0:
        print('no student information!!!')
        return
    else:
        format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
        print(format_title.format('ID', 'NAME', 'English core', 'Python core', 'Chinese core', 'Total core'))
        format_data = '{:^6}\t{:^13}\t{:^13}\t{:^13}\t{:^10}\t{:^10}\t'
        for item in list:
            print(format_data.format(item.get('id'),
                                     item.get('name'),
                                     item.get('englishcore'),
                                     item.get('pythoncore'),
                                     item.get('chinesecore'),
                                     int(item.get('englishcore'))+int(item.get('pythoncore'))+
                                     int(item.get('chinesecore'))
                                     ))

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student=rfile.readlines()
            student_new=[]
            for item in student:
                d=dict(eval(item))
                student_new.append(d)

    else:
        print('there is no student information yet !!')
        return
    mode = int(input('how to sort ? 0 for up, 1 for down:'))
    if mode == 0:
        mode = False
    elif mode == 1:
        mode = True
    else:
        print('input error, please try again!!')
        sort()
    classmode=input('please input the class for sort, 1 for english, 2 for chinese, 3 for python,4 for total score:')
    if classmode == '1':
        student_new.sort(key=lambda x:int(x['englishcore']),reverse=mode)
        show_student(student_new)
    elif classmode == '2':
        student_new.sort(key=lambda x: int(x['chinesecore']), reverse=mode)
        show_student(student_new)
    elif classmode == '3':
        student_new.sort(key=lambda x: int(x['pythoncore']), reverse=mode)
        show_student(student_new)
    elif classmode == '4':
        student_new.sort(key=lambda x: int(x['englishcore'])+int(x['chinesecore'])+int(x['pythoncore']), reverse=mode)
        show_student(student_new)
    else:
        print('input error, please try again!!')
        sort()


def delete():
    while True:
        student_id=input('please input the student ID to delete:')
        if student_id !='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False # flag for whether delete successfully.
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))   # convert string to dict
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'the information of the id {student_id} is deleted')
                    else:
                        print(f'the information of the id {student_id} can not be found')
        else:
            print('no this student ID')
            break
        show()
        answer=input('do you want to delete more ? Y/N')
        if answer == ['y','Y']:
            continue
        else:
            print('thank you')
            break

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student=rfile.readlines()
            if student:
                print('===============================================')
                print('===============there is total {} students============'.format(len(student)))
                print('===============================================')
            else:
                print('there is no student information yet')
    else:
        print('there is no student information yet')
def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student=rfile.readlines()
            for item in student:
                student_list.append(eval(item))


            if len(student_list) !=0:
                show_student(student_list)
            else:
                print('there is no student information yet!!!')

    else:
        print('there is no student file yet!!')

def modify():
    student_id=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id =input('input the ID to modify:')
    print(student_id)
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id'] == student_id:
                print('found this student,lets change its information!!')
                while True:
                    try:
                        d['name'] = input('input the name:')
                        d['englishcore'] = input('input the english core:')
                        d['pythoncore'] = input('input the python core:')
                        d['chinesecore'] = input('input the Chinese core:')
                    except:
                        print('input error,please try again!')

                    wfile.write(str(d) + '\n')
                    print('modify successfully!!')
                    break
            else:

                wfile.write(str(d) + '\n')
        print('can not find it, please try again')
        answer=input('do u want to modify more ? Y/N')
        if answer == 'y':
            modify()
        elif answer == 'Y':
            modify()
        else:
            pass


def main():
    while True:
        menu()
        choice=int(input('please input your request:'))
        if choice in [1,2,3,4,5,6,7,8]:
            if choice == 8:
                doubleconfirm=input('are you sure you will quit the system, Y/N')
                if doubleconfirm in ['y','Y']:
                    print('thank you')
                    break  # quit and close
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        else:
            print('------you input error,please try again-------')
            print('\n')
            print('\n')
            print('\n')
            print('\n')


if __name__ == '__main__':
    while True:
        try:
            main()
            break
        except BaseException as e:
            print('input error')
            print(e)
            continue




import os.path

filename='student.txt'

def delete():
    while True:
        student_id=input('please input the student ID to delete:')
        if student_id !='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
                    print(student_old)
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

        answer=input('do you want to delete more ? Y/N')
        if answer == ['y','Y']:
            continue
        else:
            print('thank you')
            break

delete()

def caluc(a,b):
    c=a/b
    return c




if __name__ == '__main__':
  try:
    a=input('number1:')
    b=input('number2:')
    result = caluc(int(a), int(b))
    print(result)
  except ZeroDivisionError:
      print('0')
  except BaseException as e:
      print('there is a error',e)

  else:
      print('done')

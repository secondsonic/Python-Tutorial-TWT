#optional parameters

def func(x, text):
    print(x)
    if text == '1':
        print('Text is one')
    else:
        print("Text is not one")

func('Arsalan', '1')


def func0(x, text = '2'): #text is defaulted to the value of the 2
    print(x)              #but still changeable
    if text == '1':
        print('Text is one')
    else:
        print("Text is not one")

func0('Arsalan', '1')

def func0(x = '2', text = '1'):
    print(x)
    if text == '1':
        print('Text is one')
    else:
        print("Text is not one")

func0()

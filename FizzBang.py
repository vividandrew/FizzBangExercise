count = 0

def FizzBang(i):
    if i%3 == 0 and i%5 == 0:
        print('FizzBang')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Bang')
    else:
        print(str(i))


while True:
    count += 1
    FizzBang(count)
    if count == 100:
        break

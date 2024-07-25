import random
num = random.randint(1, 100)
input_num = 0 #input('숫자를 입력하세요 1~100 : ')
while input_num != num :
    input_num = int(input('숫자를 입력하세요 1~100 : '))
    if input_num == num :
        print('정답입니다 {}'.format(num))
        break
    elif input_num > num :
        print('정답보다 큽니다. {}'.format(input_num))
    elif input_num < num :
        print('정답보다 작습니다. {}'.format(input_num))



# auto
import random
num = random.randint(1, 100)
input_num = random.randint(1, 100)
min_num = 1
max_num = 100
while input_num != num :
    if input_num > num :
        print('정답보다 큽니다. {} 답{}'.format(input_num, num))
        max_num = input_num
    elif input_num < num :
        print('정답보다 작습니다. {} 답{}'.format(input_num, num))
        min_num = input_num

    input_num = random.randint(min_num + 1, max_num - 1)

    if input_num == num :
        print('정답입니다 {}  입력값 : {}'.format(num, input_num))
        break
    
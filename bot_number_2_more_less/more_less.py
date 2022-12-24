import random

flag = True
answer = random.randint(1, 100)
k = 0


while True:
    try:
        n = int(input())
        if n == answer:
            print(f'YOU WIN! Count of attempts = {k}')

            with open('high_score.txt', 'w+') as high_score:
                if len(high_score.read()) == 0:
                    high_score.write(f'{k}')
                    break
                elif int(high_score.read()) > k:
                    print('NEW RECORD')
                    high_score.write(f'{k}')
                    break
        elif n < answer:
            print('The hidden number is greater')
            k += 1
        elif n > answer:
            print('The hidden number is less')
            k += 1
    except ValueError:
        print('Print number!')

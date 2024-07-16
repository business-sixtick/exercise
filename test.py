def count_up_to(max):
    count = 1
    while count <= max:
        print('함수 ', count)
        yield count
        count += 1
        print('카운트 ', count)

counter = count_up_to(5)
print('호출자 ', counter, type(counter))
for num in counter:
    print(num, ' 반복문')



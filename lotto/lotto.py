# 기 당첨 누적치. 각번호당 뽑힌 누적치. + 5개 뽑기 5천원치~
import sqlite3
import pandas as pd
#conn =  sqlite3.connect('../data/lotto.db') # C:\source\exercise\data\lotto.db
conn =  sqlite3.connect('C:\source\exercise\data\lotto.db')
cursor = conn.cursor()
rows = cursor.execute('select * from win').fetchall()

pass # TODO

# 가중치 : 연속으로 당첨될 경우 가중치가 늘어난다 
def weighting(val : int, up_down : bool = True) -> int :   # 웨이팅 : 가중치, 지역수당
    """가중치를 적용해서 리턴한다

    Args: 
        val (int) : 가중치를 넣는다.
        up_down (bool) : True: 올림, False:내림\n\t 가중치를 올린 건지 내릴 건지 결정 한다
    Returns:
        (float) : 가중치를 계산해서 리턴한다
    """
    up = 0.1
    down = 0.02
    if up_down == True :
        val += (val * up)
    elif up_down == False : 
        val -= (val * down)    

    if val < 1 :
        val = 1

    return round(val) #int(val)

accumulate = { key : [0, 100.0] for key in range(1, 46) } # 초기 가중치를 넣어서 테이블을 초기화 한다.

for row in rows : # 당첨된 테이블을 순회 한다.
    for item in accumulate.items() :
        # print(item)
        index = item[0]
        count = item[1][0]
        weight = item[1][1]
        if index in row : 
            accumulate.update({index : [count + 1, weighting(weight)]})
        else : # 카운트 누적하지 않고 가중치 내림
            accumulate.update({index : [count, weighting(weight, up_down=False)]})


conn.close()

weight_list = [ int(i[1][1]) for i in accumulate.items()]
# print(len(weight_list), weight_list) # 가중치는 int 리스트로 줘야 한다. 

def lotto_get() :
    import random
    lotto_set = set()
    while len(lotto_set) <= 6 :
        lotto_set.add(random.sample(range(1, 46), 1, counts=weight_list)[0])
        
    # 가중치에 가중치 주기
    for j in lotto_set : 
        weight_list[j-1] += weighting(weight_list[j-1])
    
    return (sorted(lotto_set))

def a_weight_lotto():
    lotto_list = []
    #while len(lotto_list) <= 10 : 
    while True : 
        if len(lotto_list) < 10 : 
            lotto_list.append(lotto_get())
        else :
            if lotto_list[-1] == lotto_list[-2] :
                break
            else :
                lotto_list.pop(0)
                lotto_list.append(lotto_get())
    return lotto_list[-1]

print(a_weight_lotto())


# for i, val in enumerate(lotto_list) :
#     if i in [4, 5, 6, 7, 8, 9] :
#         print(val)
    
# print(len(weight_list), weight_list)
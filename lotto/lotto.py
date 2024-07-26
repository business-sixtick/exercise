import logging
import sqlite3
import random
logging.basicConfig(level=logging.INFO) # debug가 젤낮은거넹~ ㅎ
debug = logging.info
# 
class cLotto :
    pass
    # 생성자. 
    def __init__(self):
        if not cLotto.__gWinTable :
            debug('if not cLotto.__gWinTable')
            cLotto.__gWinTable = self.__aSetWinTable()
            self.mWeightTable = self.__aSetWeightTable(cLotto.__gWinTable)

    __gWinTable = None
    
    def __aSetWeightTable(self, rows : list) -> list:
        accumulate = { key : [0, 100.0] for key in range(1, 46) } # 초기 가중치를 넣어서 테이블을 초기화 한다.

        for row in rows : # 당첨된 테이블을 순회 한다.
            for item in accumulate.items() :
                # print(item)
                index = item[0]
                count = item[1][0]
                weight = item[1][1]
                if index in row : 
                    accumulate.update({index : [count + 1, cLotto.__weighting(weight)]})
                else : # 카운트 누적하지 않고 가중치 내림
                    accumulate.update({index : [count, cLotto.__weighting(weight, up_down=False)]})

        weight_list = [ int(i[1][1]) for i in accumulate.items()]
        # print(len(weight_list), weight_list) # 가중치는 int 리스트로 줘야 한다. 
        return weight_list

    # 가중치 : 연속으로 당첨될 경우 가중치가 늘어난다 
    def __weighting(self, val : int, up_down : bool = True) -> int :   # 웨이팅 : 가중치, 지역수당
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

    def __aSetWinTable(self):
        conn =  sqlite3.connect('C:\source\exercise\data\lotto.db')
        cursor = conn.cursor()
        rows = cursor.execute('select * from win').fetchall()
        conn.close()
        return rows
        # TODO : 디비주소 정보 파일을 따로 둬야 한다.

    def aShowWinTable(self):
        """ [(round,1,2,3,4,5,6,bonus),...]
        """
        print(len(cLotto.__gWinTable))
        for i in cLotto.__gWinTable:
            print(i)

    def aShowWeightTable(self):
        # for i in self.mWeightTable:
        #     print(i)
        print(len(self.mWeightTable))
        print(self.mWeightTable)

    def aChoice(self, how = 6, much = 1, new = False): # 번호 뽑기
        for i in range(much):
            lotto_set = set()
            while len(lotto_set) < how :
                lotto_set.add(random.sample(range(1, 46), 1, counts=self.mWeightTable)[0])
            debug(lotto_set)
        
            for j in lotto_set : #가중치에 가중치 주기
                self.mWeightTable[j-1] += self.__weighting(self.mWeightTable[j-1])

    
    # 신규 당첨 크롤링

lotto = cLotto()
# lotto.aShowWinTable()
print('.')
# lotto.aShowWeightTable()
lotto.aChoice(much=5)
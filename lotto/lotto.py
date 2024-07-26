import logging
import sqlite3
import random
import requests #pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

logging.basicConfig(level=logging.INFO) # debug가 젤낮은거넹~ ㅎ
debug = logging.info

class cLotto :
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
                    accumulate.update({index : [count + 1, self.__weighting(weight)]})
                else : # 카운트 누적하지 않고 가중치 내림
                    accumulate.update({index : [count, self.__weighting(weight, up_down=False)]})

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

    def aChoiceHard(self):
        
        lotto_set_list = []
        while True:
            lotto_set = set()
            while len(lotto_set) < 6 :
                lotto_set.add(random.sample(range(1, 46), 1, counts=self.mWeightTable)[0])
            debug('aChoiceHard')
            debug(sorted(lotto_set))
        
            for j in lotto_set : #가중치에 가중치 주기
                self.mWeightTable[j-1] += self.__weighting(self.mWeightTable[j-1])

            if not lotto_set_list or len(lotto_set_list) == 1:
                lotto_set_list.append(lotto_set)
            elif len(lotto_set_list) == 2:
                if lotto_set_list[0] == lotto_set_list[1]:
                    break
                else :
                    del lotto_set_list[0]
                    lotto_set_list.append(lotto_set)

    # 신규 당첨 번호 테이블에 추가
    def new_win_add(self, win_list):
        conn =  sqlite3.connect('C:\source\exercise\data\lotto.db')
        cursor = conn.cursor()
        rows = cursor.execute('select * from win').fetchall()
        if rows[-1][0] < win_list[0] :
            cursor.execute('''INSERT INTO win (id, win1, win2, win3, win4, win5, win6, bonus) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', win_list)
            conn.commit()
        conn.close()

    # 신규 당첨 크롤링
    def aNewWinCrawling(self):
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Whale/3.26.244.21 Safari/537.36'}
        url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin'
        response = requests.get(url, headers=headers) 
        debug(response.ok)

        html_content = response.text
        debug(len(html_content))
        # Beautiful Soup을 사용하여 HTML 내용 파싱
        soup = BeautifulSoup(html_content, 'html.parser')
        debug(type(soup))

        turn = soup.find('div', class_="win_result").find('h4').find('strong').get_text() #회차
        debug('turn : ', turn.replace('회', '').strip())
        turn = int(turn.replace('회', '').strip())
        win_num_span = soup.find('div', class_="win_result").find('span')
        debug('span 1 : ' , win_num_span.get_text())
        bonus = int(soup.find('div', class_="num bonus").find('span').get_text())
        
        win_list = []
        while len(win_list) < 6 :
            if win_num_span :
                win_list.append(int(win_num_span.get_text()))
            else : 
                break
            win_num_span = win_num_span.find_next_sibling()
        
        win_list.insert(0, turn)
        win_list.append(bonus)
        debug(win_list)
        return win_list


        # print('rows[-1][0] == turn : ', rows[-1][0] == turn)

        # if(rows[-1][0] < turn) :
        #     print('새로운 당첨 번호가 있습니다. ')
        #     while len(win) < 6 :
        #         if win_num_span :
        #             win.append(int(win_num_span.get_text()))
        #         else : 
        #             break
        #         win_num_span = win_num_span.find_next_sibling()
        #     print(win)
        #     cursor.execute('''INSERT INTO win (id, win1, win2, win3, win4, win5, win6, bonus) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', win)
        #     conn.commit()
        # else : 
        #     print('최신정보입니다.')


        # conn.close()

        ''' 
        <div class="win_result">
                            <h4><strong>1128회</strong> 당첨결과</h4>
                            <p class="desc">(2024년 07월 13일 추첨)</p>
                            <div class="nums">
                                <div class="num win">
                                    <strong>당첨번호</strong>
                                    <p>
                                        <span class="ball_645 lrg ball1">1</span>
                                        <span class="ball_645 lrg ball1">5</span>
                                        <span class="ball_645 lrg ball1">8</span>
                                        <span class="ball_645 lrg ball2">16</span>
                                        <span class="ball_645 lrg ball3">28</span>
                                        <span class="ball_645 lrg ball4">33</span>
                                    </p>
                                </div>
                                <div class="num bonus">
                                    <strong>보너스</strong>
                                    <p><span class="ball_645 lrg ball5">45</span></p>
                                </div>
                            </div>
                        </div>
        '''

            

lotto = cLotto()
# lotto.aShowWinTable()
print('.')
# lotto.aShowWeightTable()
# lotto.aChoice(much=5)

# lotto.aChoiceHard()
# lotto.new_win_add(lotto.aNewWinCrawling())

lotto.aChoiceHard()

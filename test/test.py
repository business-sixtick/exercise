import platform
print('python version : ', platform.architecture())
import time
def message_time():
    try:
        count = 0   # 살짝 클로저 냄새가 나는군~ ㅋㅋ
        while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
            count += 1
            x = (yield count)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
                                # yield 뒤에 값을 넣어주면 반환을 함
            print(x, f'\n<{time.asctime()}>')
    except GeneratorExit as e :     # close() 할때 발생하는 예외인데
        print(e, type(e).__name__)  # 굳이 안잡아도 됨. 에러를 발생시키지 않음. 
        print(x, count)             # 예외에도 등급이 있나??
 
msg = message_time()
#next(msg)           # yield까지 실행해서 대기상태로 만듦
print(msg.send(None)) # 내부적으로 next와 같은 효과를 냄

msg.send('hello~ nice meet you^^ ')   # 값을 보내고 다음 대기상태까지 진행
print(msg.send('see you again')) 

msg.close() # 코루틴 종료
print('프로그램 종료')
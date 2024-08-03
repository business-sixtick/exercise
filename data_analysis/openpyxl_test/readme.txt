import pandas as pd

# Excel 파일 읽어오기
df = pd.read_excel('example.xlsx')

# DataFrame 출력
print(df)

pandas에 엑셀 전체 읽기 있네 ㅋ

import pandas as pd

# 데이터 프레임 생성
data = {
    '이름': ['Alice', 'Bob', 'Charlie'],
    '나이': [30, 25, 35]
}

df = pd.DataFrame(data)

# Excel 파일로 저장
df.to_excel('example.xlsx', index=False)
print("Excel 파일이 생성되었습니다.")

쓰는것도 잇어 ~ ㅋㅋㅋ
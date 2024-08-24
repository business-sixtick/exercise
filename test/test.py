import matplotlib.pyplot as plt
import numpy as np
import time

# 실시간 데이터를 시뮬레이션하기 위한 샘플 데이터
x = np.linspace(0, 10, 100)

plt.ion()  # Interactive 모드를 켬 (실시간 업데이트)
fig, ax = plt.subplots()

for i in range(50):
    y = np.sin(x + i * 0.1)  # 데이터를 업데이트
    ax.clear()  # 기존 플롯을 지움
    ax.plot(x, y)  # 새로운 데이터로 플롯을 그림
    plt.draw()  # 업데이트된 플롯을 그리기
    plt.pause(0.1)  # 잠시 대기 (0.1초)
    print(i)

plt.ioff()  # Interactive 모드 끔
plt.show()  # 마지막 플롯을 유지

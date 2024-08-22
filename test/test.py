import tensorflow as tf

# 로그 레벨 설정
tf.debugging.set_log_device_placement(True)

# 예제 연산
a = tf.constant([[1, 2, 3], [4, 5, 6]])
b = tf.constant([[1, 2], [3, 4], [5, 6]])

# 올바른 행렬 곱셈
c = tf.matmul(a, b)  # 크기가 [2, 2]인 행렬 결과
print(c)
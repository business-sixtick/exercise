from PIL import Image
import numpy as np

# 이미지를 로드합니다.
img = Image.open(r"C:\source\exercise\web_study\project\son_word\uploaded_image.png")

# print(np.array(img).reshape(784,4))
# 흑백 이미지로 변환합니다.
# img = img.convert("L")

# 이미지를 NumPy 배열로 변환합니다.
np.set_printoptions(threshold=np.inf)

img_array = np.array(img)
print(img_array.shape, img_array[:,:,3])

import matplotlib.pyplot as plt

# plt.imshow(img_array, cmap='gray')  # 흑백 이미지로 표시
plt.imshow(img_array)
plt.show()

# 배열의 shape을 확인합니다.
print("Image shape:", img_array.shape)  # (28, 28) 형태로 나와야 합니다.
# print(img_array)




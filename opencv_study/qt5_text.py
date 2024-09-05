import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLabel, QVBoxLayout, QWidget, QSlider, QLabel as QtLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class ImageProcessor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 메인 창 설정
        self.setWindowTitle('Image Processor with Trackbars')
        self.setGeometry(100, 100, 1000, 800)

        # 메인 위젯과 레이아웃 설정
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # 이미지 라벨 설정
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        # 트랙바 레이아웃 설정
        self.trackbar_layout = QVBoxLayout()
        self.layout.addLayout(self.trackbar_layout)

        # 트랙바 생성
        self.create_trackbars()

        # 메뉴바 설정
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # 파일 열기 액션
        open_file_action = QAction('Open Image', self)
        open_file_action.triggered.connect(self.open_image)
        file_menu.addAction(open_file_action)

    def create_trackbars(self):
        # 트랙바 범위와 레이블 생성
        self.h_min_slider = self.create_slider('H Min', 0, 179, 0)
        self.h_max_slider = self.create_slider('H Max', 0, 179, 179)
        self.s_min_slider = self.create_slider('S Min', 0, 255, 0)
        self.s_max_slider = self.create_slider('S Max', 0, 255, 255)
        self.v_min_slider = self.create_slider('V Min', 0, 255, 0)
        self.v_max_slider = self.create_slider('V Max', 0, 255, 255)
        self.threshold_min_slider = self.create_slider('Threshold Min', 0, 255, 0)
        self.threshold_max_slider = self.create_slider('Threshold Max', 0, 255, 255)

    def create_slider(self, label, min_value, max_value, init_value):
        # 슬라이더 생성
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_value)
        slider.setMaximum(max_value)
        slider.setValue(init_value)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval((max_value - min_value) // 10)
        slider.valueChanged.connect(self.update_image)

        # 레이블 생성
        slider_label = QtLabel(label)
        self.trackbar_layout.addWidget(slider_label)
        self.trackbar_layout.addWidget(slider)

        return slider

    def open_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.jpg *.bmp)', options=options)
        
        if file_path:
            self.image_path = file_path
            self.process_image(file_path)

    def process_image(self, file_path):
        # OpenCV로 이미지 읽기
        self.image = cv2.imread(file_path)
        if self.image is None:
            return

        # 이미지 전처리
        self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.update_image()

    def update_image(self):
        # 트랙바 값 읽기
        h_min = self.h_min_slider.value()
        h_max = self.h_max_slider.value()
        s_min = self.s_min_slider.value()
        s_max = self.s_max_slider.value()
        v_min = self.v_min_slider.value()
        v_max = self.v_max_slider.value()
        t_min = self.threshold_min_slider.value()
        t_max = self.threshold_max_slider.value()

        # HSV 범위에 따른 마스크 생성
        lower_bound = np.array([h_min, s_min, v_min])
        upper_bound = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(self.hsv_image, lower_bound, upper_bound)

        # 2진화(이진화) 처리
        _, binary_image = cv2.threshold(mask, t_min, t_max, cv2.THRESH_BINARY)

        # OpenCV 이미지를 QImage로 변환
        height, width = binary_image.shape
        bytes_per_line = width
        q_image = QImage(binary_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

        # QImage를 QPixmap으로 변환하고 QLabel에 표시
        self.image_label.setPixmap(QPixmap.fromImage(q_image))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageProcessor()
    ex.show()
    sys.exit(app.exec_())

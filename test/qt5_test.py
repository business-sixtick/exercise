import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QLabel, QPushButton, QLineEdit, QSlider, QCheckBox, QRadioButton,
                             QComboBox, QProgressBar, QVBoxLayout, QHBoxLayout, QWidget, QFormLayout, QGroupBox, QTextEdit, QButtonGroup, QMessageBox)
from PyQt5.QtCore import Qt

class ExampleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Layout and Menu Example')
        self.setGeometry(100, 100, 1000, 600)

        # 메뉴바 설정
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        open_file_action = QAction('Open File', self)
        file_menu.addAction(open_file_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # 중앙 위젯과 레이아웃 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # 좌측 사이드바
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar.setLayout(sidebar_layout)

        # 사이드바 컴포넌트
        sidebar_label = QLabel('Sidebar', self)
        sidebar_layout.addWidget(sidebar_label)

        sidebar_button = QPushButton('Sidebar Button', self)
        sidebar_button.clicked.connect(self.show_message_box)
        sidebar_layout.addWidget(sidebar_button)

        main_layout.addWidget(sidebar)

        # 우측 레이아웃 설정
        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        # 우측 상단 레이아웃
        top_right_layout = QVBoxLayout()
        right_layout.addLayout(top_right_layout)

        top_right_label = QLabel('Top Right', self)
        top_right_layout.addWidget(top_right_label)

        top_right_text_input = QLineEdit(self)
        top_right_text_input.setPlaceholderText('Enter text here')
        top_right_layout.addWidget(top_right_text_input)

        top_right_slider = QSlider(Qt.Horizontal, self)
        top_right_slider.setMinimum(0)
        top_right_slider.setMaximum(100)
        top_right_slider.setValue(50)
        top_right_slider.setTickPosition(QSlider.TicksBelow)
        top_right_slider.setTickInterval(10)
        top_right_slider.valueChanged.connect(self.on_slider_value_changed)
        top_right_layout.addWidget(top_right_slider)

        top_right_checkbox = QCheckBox('Check me', self)
        top_right_checkbox.stateChanged.connect(self.on_checkbox_state_changed)
        top_right_layout.addWidget(top_right_checkbox)

        top_right_combobox = QComboBox(self)
        top_right_combobox.addItem('Item 1')
        top_right_combobox.addItem('Item 2')
        top_right_combobox.addItem('Item 3')
        top_right_combobox.currentIndexChanged.connect(self.on_combobox_index_changed)
        top_right_layout.addWidget(top_right_combobox)

        # 멀티라인 텍스트 박스
        multiline_text_edit = QTextEdit(self)
        multiline_text_edit.setPlaceholderText('Enter multiple lines of text here')
        top_right_layout.addWidget(multiline_text_edit)

        # 라디오 버튼 추가
        radio_group_box = QGroupBox('Radio Buttons', self)
        radio_layout = QVBoxLayout()
        radio_group_box.setLayout(radio_layout)

        self.radio_button1 = QRadioButton('Option 1', self)
        self.radio_button2 = QRadioButton('Option 2', self)
        self.radio_button3 = QRadioButton('Option 3', self)

        radio_layout.addWidget(self.radio_button1)
        radio_layout.addWidget(self.radio_button2)
        radio_layout.addWidget(self.radio_button3)

        # 라디오 버튼 그룹 설정
        self.radio_button_group = QButtonGroup(self)
        self.radio_button_group.addButton(self.radio_button1)
        self.radio_button_group.addButton(self.radio_button2)
        self.radio_button_group.addButton(self.radio_button3)

        top_right_layout.addWidget(radio_group_box)

        # 우측 하단 레이아웃
        bottom_right_layout = QVBoxLayout()
        right_layout.addLayout(bottom_right_layout)

        bottom_right_progress_bar = QProgressBar(self)
        bottom_right_progress_bar.setValue(50)
        bottom_right_layout.addWidget(bottom_right_progress_bar)

        bottom_right_group_box = QGroupBox('Group Box', self)
        group_layout = QFormLayout()
        bottom_right_group_box.setLayout(group_layout)

        group_label = QLabel('Inside Group Box', self)
        group_button = QPushButton('Inside Group Box Button', self)
        group_button.clicked.connect(self.show_message_box)
        group_layout.addRow(group_label, group_button)

        bottom_right_layout.addWidget(bottom_right_group_box)

        # 키 이벤트 처리
        self.setFocusPolicy(Qt.StrongFocus)

    def on_slider_value_changed(self, value):
        print(f'Slider value: {value}')

    def on_checkbox_state_changed(self, state):
        print(f'Checkbox state: {"Checked" if state == Qt.Checked else "Unchecked"}')

    def on_combobox_index_changed(self, index):
        print(f'ComboBox selected index: {index}')

    def show_message_box(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box.")
        msg.setWindowTitle("Message Box")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        response = msg.exec_()
        print(f'Message box response: {response}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleApp()
    ex.show()
    sys.exit(app.exec_())

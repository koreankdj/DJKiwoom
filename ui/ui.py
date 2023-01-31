from kiwoom.kiwoom import *

import sys
from PyQt5.QtWidgets import *


class UI_class():
    def __init__(self):
        print("UI_class 입니다.")

        # App의 UI 실행 하기 위한 함수 & 변수 초기화
        self.app = QApplication(sys.argv)

        self.kiwoom = Kiwoom()

        self.app.exec_()
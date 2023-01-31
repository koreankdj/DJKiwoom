from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()

        print("Kiwoom 클래스 입니다")

        ########## eventloop 모음
        self.login_event_loop = None
        ####################

        ########## 변수모음
        self.account_num = None
        ####################

        self.get_ocx_instance()
        self.event_slots()

        self.signal_login_commConnect()
        self.get_account_info()
        self.detail_account_info()  # 예수금 가져오는 것

    def get_ocx_instance(self):
        # 키움 API 사용할 수 있도록 제작된 레지스트리 정보
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)
        self.OnReceiveTrData.connect(self.trdata_slot)

    # 로그인 시도
    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")

        self.login_event_loop = QEventLoop()
        # 로그인이 완료될 때까지 정지
        self.login_event_loop.exec_()

    def login_slot(self, errCode):
        print(errors(errCode))

        self.login_event_loop.exit()

    def get_account_info(self):
        account_list = self.dynamicCall("GetLoginInfo(String)", "ACCNO")

        self.account_num = account_list.split(':')[0]

        print("나의 보유 계좌번호 %s " % self.account_num)  # 8041148811 -> My Account

    def detail_account_info(self):
        print("예수금 요청하는 부분")

        self.dynamicCall("SetInputValue(String, String)", "계좌번호", "8041148811")
        self.dynamicCall("SetInputValue(String, String)", "비밀번호", "0000")
        self.dynamicCall("SetInputValue(String, String)", "비밀번호입력매체구분", "00")
        self.dynamicCall("SetInputValue(String, String)", "조회구분", "2")
        self.dynamicCall("CommRqData(String, String, int, String)", "예수금상세현황요청", "opw00001", "0", "2000")

    def amount_info(self):
        print("전일 거래량 요청하는 부분")
        self.dynamicCall("SetInputValue(String, String)", "시장구분", "001")
        self.dynamicCall("SetInputValue(String, String)", "조회구분", "1")
        self.dynamicCall("SetInputValue(String, String)", "순위시작", "0")
        self.dynamicCall("SetInputValue(String, String)", "순위끝", "10")
        self.dynamicCall("CommRqData(String, String, int, String)")

    def trdata_slot(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext):
        '''
        tr요청을 받는 구역!
        :param sScrNo: 스크린번호
        :param sRQName: 내가 요청했을 때 지은 이름
        :param sTrCode: 요청 id, tr코드
        :param sRecordName: 사용 안함
        :param sPrevNext: 다음 페이지가 있는지
        :return:
        '''

        if sRQName == "예수금상세현황요청":
             deposit = self.dynamicCall("GetCommData(String, String, int, String)", sTrCode, sRQName, 0, "예수금")
             print("예수금 : %s" % deposit)
             deposit = int(deposit)
             print("예수금2 : %s" % deposit)

             possible = self.dynamicCall("GetCommData(String, String, int, String)", sTrCode, sRQName, 0, "출금가능금액")
             possible = int(possible)
             print("출금 가능 금액 : %s " % possible)
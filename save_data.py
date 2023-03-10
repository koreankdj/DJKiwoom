import sys
from PyQt5.QtWidgets import QApplication
from pykiwoom.kiwoom import *
from pykiwoom.wrapper import *
import numpy as np
import pandas as pd
import sqlite3
import datetime

MARKET_KOSPI   = 0
MARKET_KOSDAK  = 10

class DailyData:
    def __init__(self):
        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()
        self.wrapper = KiwoomWrapper(self.kiwoom)
        self.get_code_list()
        print(self.kospi_codes)
        print(self.kosdak_codes)

    def get_code_list(self):
        self.kospi_codes = self.kiwoom.get_codelist_by_market(MARKET_KOSPI)
        self.kosdak_codes = self.kiwoom.get_codelist_by_market(MARKET_KOSDAK)

    def check_recent_file(self, code):
        import os
        from time import strftime, gmtime, time
        fname = '../data/hdf/%s.hdf'%code
        try:
            print(time() - os.path.getmtime(fname))
            if (time() - os.path.getmtime(fname)) < 200000:
                return True
        except FileNotFoundError:
            return False
        return False

    def save_all_data(self):
        today = datetime.date.today().strftime("%Y%m%d")
        #today = datetime.date(2011,9,1).strftime("%Y%m%d")
        print(today, len(self.kosdak_codes), len(self.kospi_codes))

        # load code list from account
        DATA = []
        with open('../data/stocks_in_account.txt', encoding='utf-8') as f_stocks:
            for line in f_stocks.readlines():
                data = line.split(',')
                DATA.append([data[6].replace('A', ''), data[1], data[0]])
        for idx, code in enumerate(DATA):
            if code == '':
                continue
            print("get data of %s" % code)
            if self.check_recent_file(code[0]): continue
            self.save_table(code[0], today)

        for code in self.kospi_codes:
            if code == '':
                continue
            print("get data of %s" % code)
            if self.check_recent_file(code): continue
            self.save_table(code, today)
        for code in self.kosdak_codes:
            if code == '':
                continue
            print("get data of %s" % code)
            if self.check_recent_file(code): continue
            self.save_table(code, today)

    def save_table(self, code, date):
        TR_REQ_TIME_INTERVAL = 4
        time.sleep(TR_REQ_TIME_INTERVAL)
        data_81 = self.wrapper.get_data_opt10081(code, date)
        time.sleep(TR_REQ_TIME_INTERVAL)
        data_86 = self.wrapper.get_data_opt10086(code, date)
        col_86 = ['?????????', '?????????', '??????(??????)', '?????????', '??????', '??????', '????????????', '?????????', '????????????',
                  '?????????', '????????????', '????????????', '????????????', '???????????????', '???????????????', '???????????????', '???????????????']
        data = pd.concat([data_81, data_86.loc[:, col_86]], axis=1)
        #con = sqlite3.connect("../data/stock.db")
        try:
            data = data.loc[data.index > int(self.kiwoom.start_date.strftime("%Y%m%d"))]
            #orig_data = pd.read_sql("SELECT * FROM '%s'" % code, con, index_col='??????').sort_index()
            orig_data = pd.read_hdf("../data/hdf/%s.hdf" % code, 'day').sort_index()
            end_date = orig_data.index[-1]
            orig_data = orig_data.loc[orig_data.index < end_date]
            data = data.loc[data.index >= end_date]
            data = pd.concat([orig_data, data], axis=0)
        except (FileNotFoundError, IndexError) as e:
            print(e)
            pass
        finally:
            data.index.name = '??????'
            if len(data) != 0:
                #data.to_sql(code, con, if_exists='replace')
                data.to_hdf('../data/hdf/%s.hdf'%code, 'day', mode='w')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    daily_data = DailyData()
    
    daily_data.save_all_data()

    import glob
    import zipfile
    filelist = glob.glob('../data/hdf/*.hdf')
    with zipfile.ZipFile('../data/hdf.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
        for f in filelist:
            myzip.write(f)

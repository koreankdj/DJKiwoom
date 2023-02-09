<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>903</width>
    <height>580</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>PyTrader v0.5</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QGroupBox" name="groupBox">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>20</y>
      <width>181</width>
      <height>291</height>
     </rect>
    </property>
    <property name="title">
     <string>수동주문</string>
    </property>
    <widget class="QComboBox" name="comboBox_3">
     <property name="geometry">
      <rect>
       <x>58</x>
       <y>140</y>
       <width>101</width>
       <height>22</height>
      </rect>
     </property>
     <item>
      <property name="text">
       <string>지정가</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>시장가</string>
      </property>
     </item>
    </widget>
    <widget class="QLabel" name="label_6">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>200</y>
       <width>31</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>가격</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_5">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>170</y>
       <width>31</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>수량</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_4">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>140</y>
       <width>31</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>종류</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_2">
     <property name="geometry">
      <rect>
       <x>60</x>
       <y>110</y>
       <width>101</width>
       <height>20</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(0, 255, 255);</string>
     </property>
    </widget>
    <widget class="QSpinBox" name="qtySpinBox">
     <property name="geometry">
      <rect>
       <x>60</x>
       <y>170</y>
       <width>101</width>
       <height>22</height>
      </rect>
     </property>
     <property name="maximum">
      <number>100</number>
     </property>
    </widget>
    <widget class="QSpinBox" name="priceSpinBox">
     <property name="geometry">
      <rect>
       <x>60</x>
       <y>200</y>
       <width>101</width>
       <height>22</height>
      </rect>
     </property>
     <property name="maximum">
      <number>5000</number>
     </property>
     <property name="singleStep">
      <number>50</number>
     </property>
    </widget>
    <widget class="QPushButton" name="orderBtn">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>230</y>
       <width>141</width>
       <height>41</height>
      </rect>
     </property>
     <property name="text">
      <string>현금주문</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="codeLineEdit">
     <property name="geometry">
      <rect>
       <x>60</x>
       <y>80</y>
       <width>101</width>
       <height>20</height>
      </rect>
     </property>
    </widget>
    <widget class="QLabel" name="label_3">
     <property name="geometry">
      <rect>
       <x>21</x>
       <y>80</y>
       <width>31</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>종목</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>50</y>
       <width>31</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>주문</string>
     </property>
    </widget>
    <widget class="QComboBox" name="orderTypeComboBox">
     <property name="geometry">
      <rect>
       <x>60</x>
       <y>50</y>
       <width>101</width>
       <height>20</height>
      </rect>
     </property>
     <item>
      <property name="text">
       <string>신규매수</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>신규매도</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>매수취소</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>매도취소</string>
      </property>
     </item>
    </widget>
    <widget class="QComboBox" name="accountComboBox">
     <property name="geometry">
      <rect>
       <x>60</x>
       <y>20</y>
       <width>101</width>
       <height>20</height>
      </rect>
     </property>
    </widget>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>21</x>
       <y>20</y>
       <width>31</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>계좌</string>
     </property>
    </widget>
   </widget>
   <widget class="QGroupBox" name="groupBox_2">
    <property name="geometry">
     <rect>
      <x>209</x>
      <y>19</y>
      <width>681</width>
      <height>311</height>
     </rect>
    </property>
    <property name="title">
     <string>잔고 및 보유종목 현황</string>
    </property>
    <widget class="QTableWidget" name="accountEvaluationTable">
     <property name="geometry">
      <rect>
       <x>15</x>
       <y>21</y>
       <width>651</width>
       <height>51</height>
      </rect>
     </property>
     <property name="rowCount">
      <number>1</number>
     </property>
     <row/>
     <column>
      <property name="text">
       <string>예수금 (d+2)</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>총매입</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>총평가</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>총손익</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>총수익률 (%)</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>추정자산</string>
      </property>
     </column>
    </widget>
    <widget class="QTableWidget" name="stocksTable">
     <property name="geometry">
      <rect>
       <x>15</x>
       <y>81</y>
       <width>651</width>
       <height>181</height>
      </rect>
     </property>
     <column>
      <property name="text">
       <string>종목명</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>보유량</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>매입가</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>현재가</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>평가손익</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>수익률 (%)</string>
      </property>
     </column>
    </widget>
    <widget class="QCheckBox" name="realtimeCheckBox">
     <property name="geometry">
      <rect>
       <x>500</x>
       <y>280</y>
       <width>81</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>실시간 조회</string>
     </property>
    </widget>
    <widget class="QPushButton" name="inquiryBtn">
     <property name="geometry">
      <rect>
       <x>590</x>
       <y>270</y>
       <width>75</width>
       <height>31</height>
      </rect>
     </property>
     <property name="text">
      <string>조회</string>
     </property>
    </widget>
   </widget>
   <widget class="QGroupBox" name="groupBox_3">
    <property name="geometry">
     <rect>
      <x>209</x>
      <y>329</y>
      <width>681</width>
      <height>211</height>
     </rect>
    </property>
    <property name="title">
     <string>자동 선정 종목 리스트</string>
    </property>
    <widget class="QTableWidget" name="automatedStocksTable">
     <property name="geometry">
      <rect>
       <x>15</x>
       <y>21</y>
       <width>651</width>
       <height>171</height>
      </rect>
     </property>
     <column>
      <property name="text">
       <string>주문유형</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>종목명</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>호가구분</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>수량</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>가격</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>상태</string>
      </property>
     </column>
    </widget>
   </widget>
   <widget class="QGroupBox" name="groupBox_4">
    <property name="geometry">
     <rect>
      <x>19</x>
      <y>319</y>
      <width>181</width>
      <height>221</height>
     </rect>
    </property>
    <property name="title">
     <string>로그</string>
    </property>
    <widget class="QTextEdit" name="logTextEdit">
     <property name="geometry">
      <rect>
       <x>13</x>
       <y>20</y>
       <width>161</width>
       <height>191</height>
      </rect>
     </property>
    </widget>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>903</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

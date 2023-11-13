#　https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_OpenCV_Webcam.py

#!usr/bin/env python
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import numpy as np

# メイン関数
def main():

    sg.theme('Black')

    # レイアウト（1行目：テキスト、2行目：映像画面、3行目：ボタン、ボタン、ボタン）
    layout = [[sg.Text('OpenCVによるカメラデモ ', size=(20, 3), justification='center', font='Helvetica 20')],
                  [sg.Image(filename='', key='image')],
                  [sg.Button('開始', size=(10, 3), font='Helvetica 14'),sg.Button('撮影', size=(10, 3), font='Helvetica 14'),sg.Button('終了', size=(10, 3), font='Helvetica 14'), ]]

    # ウィンドウの生成
    window = sg.Window(' デモアプリ - OpenCVによるカメラアプリ',layout, location=(200, 10))

    # キャプチャするカメラを設定
    cap = cv2.VideoCapture(0)

    recording = False

    #　イベントループ
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (800, 600))
        #　イベント取得
        event, values = window.read(timeout=20)

        #　「Exit」ボタン押下時、ウィンドウ右上の×押下時の処理
        if event == '終了' or event == sg.WIN_CLOSED:
            break

        #　「Record」ボタン押下時の処理
        elif event == '開始':
            #　撮影を開始する
            recording = True

        #　「Stop」ボタン押下時の処理
        elif event == '撮影':
            # 撮影を停止する
            recording = False
            ret, frame = cap.read()
            cv2.imwrite("data/src/image12312.jpg",frame)
            
            #　映像を消す
            # img = np.full((480, 640), 255)
            # imgbytes = cv2.imencode('.png', img)[1].tobytes()
            # window['image'].update(data=imgbytes)

        #　録画フラグがTrueなら、撮影を開始する
        if recording:
            #　カメラ映像を取得する
            ret, frame = cap.read()
            frame = cv2.resize(frame, (800, 600))
            #　映像をメモリにエンコードする
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
            #　映像を表示する
            window['image'].update(data=imgbytes)

#　メイン関数をCALL
main()
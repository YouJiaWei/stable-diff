import PySimpleGUI as sg
import subprocess
# import camera5
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import numpy as np
import sys
sg.theme('LightBlue')   # デザインテーマの設定


recording = False
cap = cv2.VideoCapture(0)
# def func_button_ok(name):

#    window['ket_name'].update(name)
#    pass
def make_main():
# ウィンドウに配置するコンポーネント
    main_layout = [  [sg.Text('画像AI生成ツール',font=('Arial',20),text_color='Blue')],#background_color='White'
            # [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
            [sg.Frame("手順:", [[sg.Text('①カメラ起動し、キーボード"a"で写真を撮ってから、"q"で閉じる')],[sg.Text('②以下の選択から好きなパターンを選んでください')],[sg.Text('③パターンを押した後、画像生成が完了するまでお待ちください・・・')],[sg.Text('④AI画像が表示された際に、ウインドウズの"x"ボタンを押下すると、AI画像生成処理が止まり、メニュー画面に戻る')],[sg.Text('※AI画像がdata/srcフォルダに保存されたため、カバーされないように別の名前に変更必要')]])], 
            [sg.Button('カメラ起動',size=(10,2),button_color=('#ffffff', '#68be8d'))] ,
            [sg.Button('男性風(リアル)',size=(20, 2),button_color=('#ffffff', '#2ca9e1'),font=('Arial',12)), sg.Button('女性風(リアル)',size=(20, 2),button_color=('#ffffff', '#2ca9e1'),font=('Arial',12))],
            [sg.Button('男性風(アニメ)',size=(20, 2),button_color=('#ffffff', '#cc7eb1'),font=('Arial',12)), sg.Button('女性風(アニメ)',size=(20, 2),button_color=('#ffffff', '#cc7eb1'),font=('Arial',12))],
            [sg.Button('男性風(イラスト)',size=(20, 2),button_color=('#ffffff', '#f6ad49'),font=('Arial',12)), sg.Button('女性風(イラスト)',size=(20, 2),button_color=('#ffffff', '#f6ad49'),font=('Arial',12))],
            [sg.Button("Open",size=(20, 2),button_color=('#ffffff', '#f6ad49'))],
            # [sg.Text(size=(73,2), key='ket_name')],

            [sg.Image("onepiece06_chopper.png"),sg.Button('終了',size=(10,2))] ,
            # [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)]
            
            ]



    # ウィンドウの生成
    return sg.Window('AI生成プログラム', main_layout, finalize=True)

def make_sub():
    sub_layout = [[sg.Text("サブウィンドウ")],
            [sg.Button("Close")],
            [sg.Button("Exit")]]
    return sg.Window("サブウィンドウ", sub_layout, finalize=True)

def make_camera():
    
    # レイアウト（1行目：テキスト、2行目：映像画面、3行目：ボタン、ボタン、ボタン）
    camera_layout = [[sg.Text('カメラ撮影 ', size=(65, 3), justification='center', font='Helvetica 20')],
                  [sg.Image(filename='', key='image')],
                  [sg.Button('開始', size=(30, 3), font='Helvetica 14'),sg.Button('撮影', size=(30, 3), font='Helvetica 14'),sg.Button('終了1', size=(30, 3), font='Helvetica 14'), ]]

    
    # ウィンドウの生成
    return sg.Window(' 画像生成のためのカメラ撮影',camera_layout, location=(100, 10))
    
#最初に表示するウィンドウを指定する。    
window=make_main()

# イベントループ
while True:
    # recording = False
    # cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1024, 768))
    event, values = window.read(timeout=20)


    if event == 'カメラ起動':
    # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        # subprocess.run(['python', 'camera5.py'])
        window.close()
        window = make_camera()

    elif event == '終了1' or event == sg.WIN_CLOSED:
        window.close()
        window = make_main()

    #cameraの撮影イベント
    #　「開始」ボタン押下時の処理
    elif event == '開始':
        #　撮影を開始する
        #　カメラ映像を取得する
        recording = True

        #　映像をメモリにエンコードする

    
    #　「Exit」ボタン押下時、ウィンドウ右上の×押下時の処理
   

    #　「撮影」ボタン押下時の処理
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


    # sg.theme(values['-LIST-'][0])
    # sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

    

    # elif event == 'OK':
    #     print('以下を入力しました', values[0])

    if event == sg.WIN_CLOSED or event == '終了':
        break

    # elif event == 'カメラ起動':
    # # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
    #     # subprocess.run(['python', 'camera5.py'])
    #     window.close()
    #     window = make_camera()


    if event == '女性風(リアル)':
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_woman.py'])
        

    if event == '女性風(アニメ)':
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_anime_girl.py'])
        
    
    if event == '女性風(イラスト)':
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_illust_woman.py'])
        
    
    if event == '男性風(リアル)':
        # func_button_ok('男性風画像生成中・・・')
        # sg.popup_auto_close("カAI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_man.py'])

    if event == '男性風(アニメ)':
        # func_button_ok('男性風画像生成中・・・')
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        # subprocess.run(['python', 'loding.py'])
        subprocess.run(['python', 'photo_anime_boy.py'])

    if event == '男性風(イラスト)':
        # func_button_ok('男性風画像生成中・・・')
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_illust_man.py'])

    # Openボタンが押された場合
    if event == "Open":
        # メインウィンドウを閉じて、サブウィンドウを作成して表示する
        window.close()
        window = make_sub()

    # Closeボタンが押された場合
    if event == "Close":
        # サブウィンドウを閉じて、メインウィンドウを作成して表示する
        window.close()
        window = make_main()


    # # sg.theme(values['-LIST-'][0])
    # # sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

    

    # # elif event == 'OK':
    # #     print('以下を入力しました', values[0])

window.close()
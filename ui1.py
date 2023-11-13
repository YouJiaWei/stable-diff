import PySimpleGUI as sg
import subprocess
import os
import numpy as np
# import camera5
# import cv2
import sys
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
sg.theme('LightBlue')   # デザインテーマの設定

# def func_button_ok(name):

#    window['ket_name'].update(name)
#    pass

# ウィンドウに配置するコンポーネント
def make_main():
    layout = [  
            [sg.Column([
            [sg.Push(),sg.Text('画像AI生成ツール',font=('Arial',20,"bold"),text_color='Blue'),sg.Push()],#background_color='White'
            # [sg.Text('ここは2行目：適当に文字を入力してください'), sg.InputText()],
            [sg.Frame("手順:", [[sg.Text('①カメラ起動し、キーボード"a"で写真を撮ってから、"q"で閉じる',font=('Arial',16,"bold"))],[sg.Text('②以下の選択から好きなパターンを選んでください',font=('Arial',16,"bold"))],[sg.Text('③パターンを押した後、画像生成が完了するまでお待ちください・・・',font=('Arial',16,"bold"))],[sg.Text('④AI画像が表示された際に、ウインドウズの"x"ボタンを押下すると、AI画像生成処理が止まり、メニュー画面に戻る',font=('Arial',16,"bold"))],[sg.Text('※AI画像がdata/srcフォルダに保存されたため、カバーされないように別の名前に変更必要',font=('Arial',16,"bold"),text_color='#e60033')]])], 
            [sg.Button('カメラ起動',size=(10,2),button_color=('#ffffff', '#68be8d'),font=('Arial',16,"bold"))],
            [sg.Push(),sg.Button('男性風(リアル)',size=(20, 2),button_color=('#ffffff', '#2ca9e1'),font=('Arial',16,"bold")),sg.Button('男性風(アニメ)',size=(20, 2),button_color=('#ffffff', '#cc7eb1'),font=('Arial',16,"bold")),sg.Button('男性風(イラスト)',size=(20, 2),button_color=('#ffffff', '#f6ad49'),font=('Arial',16,"bold")),sg.Push()],
            [sg.Push(),sg.Button('女性風(リアル)',size=(20, 2),button_color=('#ffffff', '#2ca9e1'),font=('Arial',16,"bold")), sg.Button('女性風(アニメ)',size=(20, 2),button_color=('#ffffff', '#cc7eb1'),font=('Arial',16,"bold")),sg.Button('女性風(イラスト)',size=(20, 2),button_color=('#ffffff', '#f6ad49'),font=('Arial',16,"bold")),sg.Push()],
            [sg.Button("Open")],
            [sg.Push(),sg.Image("onepiece06_chopper.png"),sg.Push()] ,
            # [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)]
            #,scrollable=True,size=(1920,1080),
            # [sg.Button('閉じる',size=(10,2),button_color=('#ffffff', '#e60033'),font=('Arial',12,"bold")),sg.Push()],
            ], justification='c')]
            
            ]
    return sg.Window('AI生成プログラム', layout,resizable=True)

def make_sub():
    # ------------ サブウィンドウ作成 ------------
    sub_layout = [[sg.Text("サブウィンドウ")],
            [sg.Button("Close")],
            [sg.Button("Exit")]]
    return sg.Window("サブウィンドウ", sub_layout, finalize=True)

# ウィンドウの生成
# window = sg.Window('AI生成プログラム', layout,resizable=True)

window=make_main()




# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '閉じる':
        break

    elif event == "Open":
        # メインウィンドウを閉じて、サブウィンドウを作成して表示する
        window.close()
        window = make_sub()

     # Closeボタンが押された場合
    elif event == "Close":
        # サブウィンドウを閉じて、メインウィンドウを作成して表示する
        window.close()
        window = make_main()
        

    elif event == 'カメラ起動':
    # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'camera5.py'])

    elif event == '女性風(リアル)':
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_woman.py'])
        

    elif event == '女性風(アニメ)':
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_anime_girl.py'])
        
    
    elif event == '女性風(イラスト)':
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_illust_woman.py'])
        
    
    elif event == '男性風(リアル)':
        # func_button_ok('男性風画像生成中・・・')
        # sg.popup_auto_close("カAI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_man.py'])

    elif event == '男性風(アニメ)':
        # func_button_ok('男性風画像生成中・・・')
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        # subprocess.run(['python', 'loding.py'])
        subprocess.run(['python', 'photo_anime_boy.py'])

    elif event == '男性風(イラスト)':
        # func_button_ok('男性風画像生成中・・・')
        # sg.popup_auto_close("AI画像生成中です・・・・・・",title="AI画面生成",auto_close_duration=1)
        subprocess.run(['python', 'photo_illust_man.py'])


    


    # sg.theme(values['-LIST-'][0])
    # sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

    

    # elif event == 'OK':
    #     print('以下を入力しました', values[0])

window.close()
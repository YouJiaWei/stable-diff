import PySimpleGUI as sg

sg.theme('Dark Red')
BAR_MAX=1000
        #　レイアウト（1段目：テキスト、2段目：プログレスバー、3段目：ボタン）
layout = [[sg.Text('画像生成中！！！')],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')],
          [sg.Cancel()]]

        #　ウィンドウの生成
window = sg.Window('　プログレスバーのサンプルアプリ　', layout)

        
for i in range(BAR_MAX):
            #　入力待ち（10msでタイムアウトして、次の処理へ進む）
            event, values = window.read()

            #　キャンセルボタンか、ウィンドウの右上の×が押された場合の処理
            if event == 'Cancel' or event == sg.WIN_CLOSED:
                break

            #　プログレスバーの表示更新（カウンタ(i)をインクリメントして表示）
            window['-PROG-'].update(i+1)
window.close()
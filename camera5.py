import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import PySimpleGUI as sg



def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    popup = sg.popup_no_wait("カメラ起動中です・・・・・・", title="カメラ",font=('Arial',20))

    n = 0
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1024, 768))
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('a'):
            cv2.imwrite('{}_{}.{}'.format(base_path, n, ext), frame)
            #n += 1
        elif key == ord('q'):
            break

        # ウィンドウが閉じられたかどうかを確認します
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyWindow(window_name)
    # ポップアップが表示されている場合、自動的に閉じる
    if popup.Displayed:
        popup.Close()


save_frame_camera_key(0, 'data/src', 'camera')
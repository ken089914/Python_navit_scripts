import tkinter  #tkinterの導入
import os #OS導入
#ウインドウ作成
root=tkinter.Tk()
root.title("Strada Menu")
root.minsize(1920, 1080)

#各動作の定義
def modoru():
    os.system("sudo python3 /home/pi/.navit/python/GUInavi.py")

#背景色設定
canvas = tkinter.Canvas(bg="black", width =1920, height=1080)
canvas.place(x=0, y=0)

#戻るボタン
gamen_button = tkinter.Button(text="メニューに戻る", width=80, height=2)
gamen_button["command"] = modoru
gamen_button.place(x=897, y=445)

#メインループ
root.mainloop()

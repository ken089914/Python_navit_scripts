import tkinter  #tkinterの導入
import os #OS導入
#ウインドウ作成
root=tkinter.Tk()
root.title("Strada Menu")
root.minsize(1920, 1080)
root.option_add("*font", ["Noto Sans Vai", 74])
#各動作の定義
def modoru():
	os.system("sudo python3 /home/pi/.navit/python/GUInavi.py")
	root.destroy()
def tojiru():
	root.destroy()
#背景色設定
canvas = tkinter.Canvas(bg="black", width =1920, height=1080)
canvas.place(x=0, y=0)

#テキスト表示
tet = tkinter.Label(text="運転中に画面を見ないでください!", bg="black", fg='yellow')
tet.place(x=200, y=300)


#戻るボタン
gamen_button = tkinter.Button(text="メニューに戻る", width=20, height=2)
gamen_button["command"] = modoru
gamen_button.place(x=0, y=705)

#戻るボタン
gamen_button = tkinter.Button(text="閉じる", width=20, height=2)
gamen_button["command"] = tojiru
gamen_button.place(x=987, y=705)


#メインループ
root.mainloop()

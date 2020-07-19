import tkinter  #tkinterの導入
import os #OS導入
#ウインドウ作成
root=tkinter.Tk()
root.title("Strada Menu")
root.minsize(1920, 1080)
root.option_add("*font", ["Noto Sans Vai", 32])

#各動作の定義
def music():
    os.system("sudo python /home/pi/.navit/python/music.py")
def radio():
    os.system("sudo python /home/pi/.navit/python/black.py")
def youtube():
    os.system("sudo python /home/pi/.navit/python/black.py")
def car():
    os.system("sudo python /home/pi/.navit/python/black.py")
def navi():
    os.system("sudo python /home/pi/.navit/python/black.py")
def settings():
    os.system("sudo python /home/pi/.navit/python/black.py")
#def terminal():
    #os.system("sudo /home/pi/.navit/python/pythonettings.py")
def andoid():
    os.system("sudo python /home/pi/.navit/python/black.py")
def off():
    os.system("sudo python /home/pi/.navit/python/black.py")

#背景色設定
canvas = tkinter.Canvas(bg="black", width =1920, height=1080)
canvas.place(x=0, y=0)

#ボタン設定(上)
#音楽ボタン
music_button = tkinter.Button(text="音楽", width=50, height=17)
music_button["command"] = music
music_button.place(x=123, y=95)

#ラジオボタン
radio_button = tkinter.Button(text="ラジオ", width=50, height=17)
radio_button["command"] = radio
radio_button.place(x=123, y=505)

#Youtubeボタン
youtube_button = tkinter.Button(text="Youtube", width=50, height=17)
youtube_button["command"] = youtube
youtube_button.place(x=763, y=95)

#車両情報ボタン
car_button = tkinter.Button(text="車両情報", width=50, height=17)
car_button["command"] = car
car_button.place(x=763, y=505)

#ナビボタン
navit_button = tkinter.Button(text="地図", width=50, height=17)
navit_button["command"] = navi
navit_button.place(x=1403, y=95)

#設定ボタン
settings_button = tkinter.Button(text="設定", width=50, height=17)
settings_button["command"] = settings
settings_button.place(x=1403, y=505)

#ボタン設定(下)
#ターミナルボタン
terminal_button = tkinter.Button(text="コマンド", width=80, height=2)
terminal_button.place(x=3, y=715)

#Andoroid切り替えボタン
Andoroid_button = tkinter.Button(text="Android", width=80, height=2)
Andoroid_button["command"] = andoid
Andoroid_button.place(x=650, y=715)

#画面オフボタン
gamen_button = tkinter.Button(text="画面オフ", width=80, height=2)
gamen_button["command"] = off
gamen_button.place(x=1297, y=715)

#メインループ
root.mainloop()

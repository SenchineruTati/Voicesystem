import sys
import tkinter as tk

#tkinterオブジェクトの取得
window = tk.Tk()

#ウィンドウのタイトル設定
window.title("新人研修音声解析システム")

#ウィンドウの表示サイズ設定
window.geometry("1000x600")

#選択した研修生のラベル
label = tk.Label(text = "ID:ここに選択した研修生のID" + "   " + "氏名:ここに選択した研修生の氏名",
                    font = ("Helvetica","20","bold"))
label.place(x = 50, y = 25)

#結果のグラフを表示するプログラム

#前の画面に戻るボタン
Button_Back = tk.Button(text = "前の画面に戻る", width=15, font = ("Helvetica","15","bold"), bg = "#d4d4d4")
Button_Back.place(x = 400, y = 500)

#メインメニューへ戻るボタン
Button_Mainmenu = tk.Button(text = "メインメニューへ戻る", width=20, font = ("Helvetica","15","bold"), bg = "#d4d4d4")
Button_Mainmenu.place(x = 650, y = 500)

window.mainloop()
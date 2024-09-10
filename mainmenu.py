import sys
import tkinter as tk

#tkinterオブジェクトの取得
window = tk.Tk()

#ウィンドウのタイトル設定
window.title("新人研修音声解析システム")

#ウィンドウの表示サイズ設定
window.geometry("1000x600")

#ラベル
label1 = tk.Label(text = '以下のボタンをクリックしてください',font = ("Helvetica","20","bold") )
label1.place(x=250,y=35)

#録音画面ボタン
Button_REC = tk.Button(text = "録音",width=20, height=2, font = ("Helvetica","20","bold"), bg = "#d4d4d4")
Button_REC.place(x = 325,y = 100)

#分析結果表示ボタン
Button_result = tk.Button(text = "分析結果表示",width=20, height=2, font = ("Helvetica","20","bold"), bg = "#d4d4d4")
Button_result.place(x = 325 , y = 250)

#研修生編集ボタン
Button_member = tk.Button(text = "研修生編集",width=20, height=2, font = ("Helvetica","20","bold"), bg = "#d4d4d4")
Button_member.place(x = 325 , y = 400)

window.mainloop()
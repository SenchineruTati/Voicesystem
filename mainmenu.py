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
label1.pack()
#録音画面ボタン
Button_REC = tk.Button(text = "録音",width=50)
Button_REC.pack()
#分析結果表示ボタン
Button_result = tk.Button(text = "分析結果表示",width=50)
Button_result.pack()
#研修生編集ボタン
Button_memuber = tk.Button(text = "研修生編集",width=50)
Button_memuber.pack()

window.mainloop()
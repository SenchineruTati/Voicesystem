import sys
import tkinter as tk
import tkinter.ttk as ttk

#tkinterオブジェクトの取得
window = tk.Tk()

#ウィンドウのタイトル設定
window.title("新人研修音声解析システム")

#ウィンドウの表示サイズ設定
window.geometry("1000x600")

#選択した研修生のラベル
label = tk.Label(text = "ID:0001" + "   " + "氏名:蒲田太郎",
                    font = ("Helvetica","20","bold"))
label.place(x = 50, y = 25)

#表示するテキストのプルダウン
count = ["1回目のテキストファイル","2回目のテキストファイル",
            "3回目のテキストファイル","4回目のテキストファイル","5回目のテキストファイル"] #選択肢
variable1 = tk.StringVar()
count_pulldown = ttk.Combobox(window, values = count, textvariable = variable1, justify=tk.CENTER, 
                                    state="readonly", font = ("Helvetica","10","bold"), width = 35)
count_pulldown.place(x=600, y=40)

#プルダウンで選択された回のテキストを表示

#前の画面に戻るボタン
Button_Back = tk.Button(text = "前の画面に戻る", width=15, font = ("Helvetica","15","bold"), bg = "#d4d4d4")
Button_Back.place(x = 400, y = 500)

#メインメニューへ戻るボタン
Button_Mainmenu = tk.Button(text = "メインメニューへ戻る", width=20, font = ("Helvetica","15","bold"), bg = "#d4d4d4")
Button_Mainmenu.place(x = 650, y = 500)

window.mainloop()
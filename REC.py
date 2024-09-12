import sys
import tkinter as tk
import tkinter.ttk as ttk

#tkinterオブジェクトの取得
window = tk.Tk()

#ウィンドウのタイトル設定
window.title("新人研修音声解析システム")

#ウィンドウの表示サイズ設定
window.geometry("1000x600")

#ラベル
label1 = tk.Label(text = '以下のボタンをクリックしてください',font = ("Helvetica","20","bold") )
label1.place(x=250,y=35)

#審査回数プルダウン
count = ["1回目","2回目","3回目","4回目","5回目"] #選択肢
variable1 = tk.StringVar()
count_pulldown = ttk.Combobox(window, values = count, textvariable = variable1, justify=tk.CENTER, 
                                    state="readonly", font = ("Helvetica","10","bold"), width = 15)
count_pulldown.place(x=140, y=100)

#研修生氏名プルダウン
member = ["研修生DBの研修生名を参照してくる"]
variable2 = tk.StringVar()
member_pulldown = ttk.Combobox(window, values = member, textvariable = variable2, justify=tk.CENTER,
                                    state="readonly", font = ("Helvetica","10","bold"), width = 30)
member_pulldown.place(x=400, y=100)

#時間設定のプルダウン
time = ["50秒間だけ録音","録音終了ボタンを押すまで録音"]
variable3 = tk.StringVar()
time_pulldown = ttk.Combobox(window, values = time, textvariable = variable3,justify=tk.CENTER,
                                state = "readonly", font = ("Helvetica","10","bold"), width = 30)
time_pulldown.place(x=700 ,y=100)

#録音開始ボタン
Button_REC_start = tk.Button(text = "録音開始",width=18, height=4, font = ("Helvetica","20","bold"), bg = "#d4d4d4")
Button_REC_start.place(x = 350,y = 200)

#メインメニューへ戻るボタン
Button_Mainmenu = tk.Button(text = "メインメニューへ戻る", width=20, font = ("Helvetica","15","bold"), bg = "#d4d4d4")
Button_Mainmenu.place(x = 650, y = 500)

window.mainloop()
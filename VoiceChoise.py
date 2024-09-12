import sys
import tkinter as tk
import tkinter.ttk as ttk

#tkinterオブジェクトの取得
window = tk.Tk()

#ウィンドウのタイトル設定
window.title("新人研修音声解析システム")

#ウィンドウの表示サイズ設定
window.geometry("1000x600")

#ラベルの表示
label = tk.Label(text = "結果表示または、テキストファイル表示する\n研修生の氏名を選択してください",font = ("Helvetica","20","bold"))
label.place(x = 225, y = 30)

#研修生氏名プルダウン
member = ["研修生DBの研修生名を参照してくる"]
variable2 = tk.StringVar()
member_pulldown = ttk.Combobox(window, values = member, textvariable = variable2, justify=tk.CENTER,
                                    state="readonly", font = ("Helvetica","10","bold"), width = 30)
member_pulldown.place(x=400, y=225)

#テキスト表示ボタン
Button_text = tk.Button(text = "テキスト表示", width = 20, height = 2, font = ("Helvetica","15","bold"), bg = "#d4d4d4")
Button_text.place(x = 100, y = 400)

#結果表示ボタン
Button_result = tk.Button(text = "結果表示", width = 20, height = 2, font = ("Helvetica","15","bold"), bg = "#d4d4d4")
Button_result.place(x = 400, y = 400)

#メインメニューへ戻るボタン
Button_back = tk.Button(text = "メインメニューへ戻る", width=20, height = 2,font = ("Helvetica","15","bold"), bg = "#d4d4d4")
Button_back.place(x = 700, y = 400)

window.mainloop()
import tkinter as tk
import sys
import time
from mutagen.mp3 import MP3 as mp3
import pygame
def sys_btn():
    sys.exit(1)
a = 0
b = '１'
question = ['問題１','問題２','問題３','問題４','おわり']
c = 1
i = 0
j = 0
abc =""
count = 0
answer = ["１", "５", "９", "１３",""]
root = tk.Tk()
root.attributes("-topmost",True)
root.title(u"四択クイズ")

def key(event):
    global b
    global lang
    if event.char == 'a':
        print("pressed", repr(event.char))

        c = 0
        v.set(1)
        print("現在選ばれている値:",b)
        btn_click()
    elif event.char ==  'z':
        print("pressed", repr(event.char))
        b = languages2[1]
        c = 1
        v.set(2)
        print("現在選ばれている値:",b)
        btn_click()
    elif event.char == 'q' or event.char == 'Q':
        print("pressed", repr(event.char))
        b = languages2[2]
        c = 2
        v.set(3)
        print("現在選ばれている値:",b)
        btn_click()
    elif event.char == ']':
        b = languages2[3]
        c = 3
        print("pressed", repr(event.char))
        v.set(4)
        print("現在選ばれている値:",b)
        btn_click()
    elif event.keysym == 'Return':
        label2 = tk.Label(root, text="ゲームを終了します")
        label2.pack()
        filename = 'escape.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        mp3_length = mp3(filename).info.length
        pygame.mixer.music.play(1)
        time.sleep(3)
        sys.exit(1)


def question_select(mon1,mon2,mon3,mon4,ans,toi):
    global b
    button1["text"] = mon1
    button2["text"] = mon2
    button3["text"] = mon3
    button4["text"] = mon4
    b = ans
    label["text"] = toi

frame = tk.Frame(root, width=450, height=450)
label = tk.Label(root, text=str(question[0]),justify=tk.LEFT,padx=20)
label.pack()
v = tk.IntVar()
v.set(1) # initializing the choice, i.e. Python
languages = [
    ("１", 1),
    ("２", 2),
    ("３", 3),
    ("４", 4)
]
languages2 = ["１", "２", "３", "４"]

def queston_box(suchi):
    global languages2
    if suchi == 0:
        languages2 = ["１", "２", "３", "４"]
    elif suchi == 1:
        languages2 = ["５", "６", "７", "８"]
    elif suchi == 2:
        languages2 = ["９", "１０", "１１", "１２"]
    elif suchi == 3:
        languages2 = ["１３", "１４", "１５", "１６"]

lang = tk.StringVar()
def ShowChoice():
    global lang
    print(v.get())
    print(lang.get())
def btn_click():
    global a,b,c,j,count,button,lang,label,question
    print(b)
    if answer[int(j)] == b:
        # 正解の場合
        tk.Label(root, text="正解！", justify=tk.LEFT, padx=20).pack()
        filename = 'bestselect.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        mp3_length = mp3(filename).info.length
        pygame.mixer.music.play(1)
        j += 1
        queston_box(int(j))
        a += 1
        count += 1
        question_select(languages2[0],languages2[1],languages2[2],languages2[3],answer[int(j)],question[int(j)])
    else:
        #不正解の場合
        tk.Label(root, text="不正解", justify=tk.LEFT, padx=20).pack()
        filename = 'badselect.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        mp3_length = mp3(filename).info.length
        pygame.mixer.music.play(1)
        j += 1
        count +=1
        queston_box(int(j))
        question_select(languages2[0],languages2[1],languages2[2],languages2[3],answer[int(j)], question[int(j)])
    if int(count) == 4:
        sub_win = tk.Toplevel(root)
        sub_win.title(u"結果")
        label2 = tk.Label(sub_win, text="あなたの正解数は"+str(a)+"です")
        esc_button = tk.Button(sub_win, text="閉じる", command=sys_btn, width=15, bg="#ff00ff", fg="white")
        label2.pack()
        esc_button.pack()



for language, val in languages:
    #選択肢をボタンで出力
    if i == 0:
        button1 = tk.Button(root, text=languages2[int(i)], command=ShowChoice, width=15, bg="black", fg="white")
    elif i == 1:
        button2 = tk.Button(root, text=languages2[int(i)], command=ShowChoice, width=15, bg="black", fg="white")
    elif i == 2:
        button3 = tk.Button(root, text=languages2[int(i)], command=ShowChoice, width=15, bg="black", fg="white")
    else:
        button4 = tk.Button(root, text=languages2[int(i)], command=ShowChoice, width=15, bg="black", fg="white")
    i += 1
button1.pack()
button2.pack()
button3.pack()
button4.pack()
frame.bind("<Key>", key)
frame.focus_set()
frame.pack()
root.mainloop()
import tkinter as tk
import sys
import time
from mutagen.mp3 import MP3 as mp3
import pygame
a = 'Java'
b = ''
question = ['問題１','問題２','問題３','問題４']
c = 0
i = 0
root = tk.Tk()
root.title(u"四択クイズ")
def key(event):
    global b
    global lang
    if event.char == 'a':
        print("pressed", repr(event.char))
        b = languages2[0]
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
        print("pressed", repr(event.char))
        btn_click()
    elif event.keysym == 'Escape':
        label2 =tk.Label(root, text="ゲームを終了します")
        label2.pack()
        filename = 'escape.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        mp3_length = mp3(filename).info.length
        pygame.mixer.music.play(1)
        time.sleep(3)
        sys.exit(1)


frame = tk.Frame(root, width=450, height=450)
label = tk.Label(root, text=question[2],justify=tk.LEFT,padx=20).pack()
v = tk.IntVar()
v.set(1) # initializing the choice, i.e. Python
languages = [
    ("１", 1),
    ("２", 2),
    ("３", 3),
    ("４", 4)
]
languages2 = ["１", "２", "３", "4"]
lang = tk.StringVar(value=languages2)
def ShowChoice():
    global lang
    print(v.get())
    print(lang.get())
def btn_click():
    global b,c,lang
    print(b)
    if b == "１":
        tk.Label(root, text="正解", justify=tk.LEFT, padx=20).pack()
        #正解の場合
        filename = 'bestselect.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        mp3_length = mp3(filename).info.length
        pygame.mixer.music.play(1)
    else:
        #不正解の場合
        tk.Label(root, text="不正解", justify=tk.LEFT, padx=20).pack()
        filename = 'badselect.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        mp3_length = mp3(filename).info.length
        pygame.mixer.music.play(1)
for language, val in languages:
    #選択肢をボタンで出力
    tk.Button(root, text=languages2[int(i)], command=ShowChoice,width=15,bg="#ff00ff",fg="white").pack()
    i += 1
tk_button = tk.Button(root,text='回答',command=btn_click)
tk_button.place(x=140,y=170)
tk_button.pack()
frame.bind("<Key>", key)
frame.focus_set()
frame.pack()
root.mainloop()
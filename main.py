# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:53:29 2021

@author: DELL
"""

from tkinter import *
import time
root = Tk()
root.title("TIC-TAC-TOE GAME")
root.geometry("600x500")
root.resizable(0,0)

widget = Canvas(root, width = 600, height = 500)
widget.pack()
widget.create_line(250,200,250,420, width = 4, fill = "purple")
widget.create_line(350,200,350,420, width = 4, fill = "purple")
widget.create_line(150,260,450,260, width = 4, fill = "purple")
widget.create_line(150,360,450,360, width = 4, fill = "purple")
Label(root, text = "TIC-TAC-TOE GAME", font = "cambriamath 20 bold italic underline").place(x = 175, y = 20)


def vanish_submission ():
    def vanish ():
        l2.destroy()
        b2.destroy() 
    l2 = Label(root, text = f"Player#1 Marker = \"X\"\nPlayer#2 Marker = \"O\""
               , font = "cambriamath 12 italic")
    l2.place(x = 230, y = 100)
    b2 = Button(root, text = "START", font = "timesnewroman 8 bold italic",
    background="purple",foreground="orange",activebackground= "black",
    activeforeground="red",padx = 3, command = vanish)
    b2.place(x = 280, y = 155)
    
vanish_submission()



marker = StringVar()
current_marker = marker.get()
def change_marker ():
    global current_marker
 
    if current_marker == "X":
        current_marker = "O"
    else:
        current_marker = "X"

    return current_marker



entry = ["","","","","","","","",""]
def check (entry):
    if entry[0] != "" and entry[1] != "" and entry[2] != "" and entry[0] == entry[1] and entry[1] == entry[2]:
        if entry[0] == "X":
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#1 WON",background="magenta", foreground="black",
            font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red",foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
        else:
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#2 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
            
    if entry[0] != "" and entry[3] != "" and entry[6] != "" and entry[0] == entry[3] and entry[3] == entry[6]:
        if entry[0] == "X":
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#1 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
        else:
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#2 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
            
    if entry[0] != "" and entry[4] != "" and entry[8] != "" and entry[0] == entry[4] and entry[4] == entry[8]:
        if entry[0] == "X":
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#1 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
        else:
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#2 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black"
            , command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
            
    if entry[1] != "" and entry[4] != "" and entry[7] != "" and entry[1] == entry[4] and entry[4] == entry[7]:
        if entry[1] == "X":
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#1 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black"
            , command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
        else:
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#2 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black"
            , command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop(
                )
    if entry[2] != "" and entry[5] != "" and entry[8] != "" and entry[2] == entry[5] and entry[5] == entry[8]:
        if entry[2] == "X":
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#1 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
        else:
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#2 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
            
    if entry[2] != "" and entry[4] != "" and entry[6] != "" and entry[2] == entry[4] and entry[4] == entry[6]:
        if entry[2] == "X":
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#1 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
        else:
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#2 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
            
    if entry[3] != "" and entry[4] != "" and entry[5] != "" and entry[3] == entry[4] and entry[4] == entry[5]:
        if entry[3] == "X":
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#1 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black"
            , command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
        else:
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#2 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black", command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
            
    if entry[6] != "" and entry[7] != "" and entry[8] != "" and entry[6] == entry[7] and entry[7] == entry[8]:
        if entry[6] == "X":
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#1 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black"
            , command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()
        else:
            root1 = Tk()
            root1.geometry("300x200")
            root1.resizable(0,0)
            root1.title("RESULT")
            root1.config(background="gold")
            def vanish_():
                root1.destroy()
                root.destroy()
            l1 = Label(root1, text = "PLAYER#2 WON",background="magenta", foreground="black"
            , font = "symbolic 14 italic", border = 4, relief = RAISED, padx = 5, pady = 3)
            l1.place(x = 70, y = 50)
            b1 = Button(root1, text = "CLOSE",background="red", foreground="black"
            , command = vanish_)
            b1.place(x = 130, y = 150)
            root1.mainloop()


def exchange (event):
    text = event.widget.cget("text")
    
    if text == "1":
        b1.destroy()
        change_marker ()
        b_1 = Label(root, text = current_marker,font = "timesnewroman 24 bold",
        background= "black",foreground="red",padx = 35, pady = 7)
        b_1.place(x=150, y = 200)
        entry[0] = b_1.cget("text")
        
    if text == "2":
        b2.destroy()
        change_marker ()
        b_2 = Label(root, text = current_marker,font = "timesnewroman 24 bold",
        background= "black",foreground="red", padx = 32, pady = 7)
        b_2.place(x=255, y = 200)
        entry[1] = b_2.cget("text")
        
    if text == "3":
        b3.destroy()
        change_marker ()
        b_3 = Label(root, text = current_marker,font = "timesnewroman 24 bold",
        background= "black",foreground="red", padx = 34, pady = 7)
        b_3.place(x=355, y = 200)
        entry[2] = b_3.cget("text")
    
    if text == "4":
        b4.destroy()
        change_marker ()
        b_4 = Label(root, text = current_marker,font = "timesnewroman 24 bold",
        background= "black",foreground="red", padx = 35, pady = 24)
        b_4.place(x=150, y = 265)
        entry[3] = b_4.cget("text")
        
    if text == "5":
        b5.destroy()
        change_marker ()
        b_5 = Label(root, text = current_marker,font = "timesnewroman 24 bold",
        background= "black",foreground="red", padx = 32, pady = 24)
        b_5.place(x=255, y = 265)
        entry[4] = b_5.cget("text")
        
    if text == "6":
        b6.destroy()
        change_marker ()
        b_6 = Label(root, text = current_marker,font = "timesnewroman 24 bold",
        background= "black",foreground="red", padx = 35, pady = 24)
        b_6.place(x=355, y = 265)
        entry[5] = b_6.cget("text")
        
    if text == "7":
        b7.destroy()
        change_marker ()
        b_7 = Label(root, text = current_marker,font = "timesnewroman 24 bold",
        background= "black",foreground="red", padx = 35, pady = 7)
        b_7.place(x=150, y = 365)
        entry[6] = b_7.cget("text")
        
    if text == "8":
        b8.destroy()
        change_marker ()
        b_8 = Label(root, text = current_marker,font = "timesnewroman 24 bold",
        background= "black",foreground="red", padx = 32, pady = 7)
        b_8.place(x=255, y = 365)
        entry[7] = b_8.cget("text")
        
    if text == "9":
        b9.destroy()
        change_marker ()
        b_9 = Label(root, text = current_marker,font = "timesnewroman 24 bold",
        background= "black",foreground="red", padx = 34, pady = 7)
        b_9.place(x=355, y = 365)
        entry[8] = b_9.cget("text")


    print(entry)
    check(entry)

root.config(background="orange")    
b1 = Button(root, text = "1",font = "timesnewroman 14 bold",background= "orange",
foreground="green",padx = 35, pady = 10)
b1.place(x=150, y = 200)
b1.bind("<Button-1>", exchange)
b2 = Button(root, text = "2",font = "timesnewroman 14 bold",background= "orange",
foreground="green", padx = 32, pady = 10)
b2.place(x=255, y = 200)
b2.bind("<Button-1>", exchange)
b3 = Button(root, text = "3",font = "timesnewroman 14 bold",background= "orange",
foreground="green", padx = 34, pady = 10)
b3.place(x=355, y = 200)
b3.bind("<Button-1>", exchange)
b4 = Button(root, text = "4",font = "timesnewroman 14 bold",background= "orange",
foreground="green", padx = 34, pady = 27)
b4.place(x=150, y = 265)
b4.bind("<Button-1>", exchange)
b5 = Button(root, text = "5",font = "timesnewroman 14 bold",background= "orange",
foreground="green", padx = 32, pady = 27)
b5.place(x=255, y = 265)
b5.bind("<Button-1>", exchange)
b6 = Button(root, text = "6",font = "timesnewroman 14 bold",background= "orange",
foreground="green", padx = 34, pady = 27)
b6.place(x=355, y = 265)
b6.bind("<Button-1>", exchange)
b7 = Button(root, text = "7",font = "timesnewroman 14 bold",background= "orange",
foreground="green", padx = 34, pady = 9)
b7.place(x=150, y = 365)
b7.bind("<Button-1>", exchange)
b8 = Button(root, text = "8",font = "timesnewroman 14 bold",background= "orange",
foreground="green", padx = 32, pady = 9)
b8.place(x=255, y = 365)
b8.bind("<Button-1>", exchange)
b9 = Button(root, text = "9",font = "timesnewroman 14 bold",background= "orange",
foreground="green", padx = 34, pady = 9)
b9.place(x=355, y = 365)
b9.bind("<Button-1>", exchange)


root.mainloop()


import tkinter as tkr
import pygame
import os
from tkinter.filedialog import askdirectory
from tkinter.ttk import *

player = tkr.Tk()
player.title("Spot Gaana")
player.geometry("500x500")

direc = askdirectory()
os.chdir(direc)

songList = os.listdir()

playlist = tkr.Listbox(player, font='Aleo', bg='black',fg='white', selectmode=tkr.SINGLE)

for item in songList:
    pos = 0
    playlist.insert(pos, item)
    pos += 1
    
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
    
def exit_mp():
    pygame.mixer.music.stop()
    

def pause():
    pygame.mixer.music.pause()
    
def resume():
    pygame.mixer.music.unpause()
    
photo = tkr.PhotoImage(file = r'D:/Abhi/Udemy/Music player/playbt.jpg')

playBt = tkr.Button(player, height=3, width=5, text='Play', font='Aleo', command=play, bg='white', fg='black', image=photo)
stopBt = tkr.Button(player, height=3, width=5, text='Stop', font='Aleo', command=exit_mp, bg='white', fg='black')
pauseBt = tkr.Button(player, height=3, width=5, text='Pause', font='Aleo', command=pause, bg='white', fg='black')
resumeBt = tkr.Button(player, height=3, width=5, text='Resume', font='Aleo', command=resume, bg='white', fg='black')
playBt.pack(fill='x')
stopBt.pack(fill='x')
pauseBt.pack(fill='x')
resumeBt.pack(fill='x')


playlist.pack(fill='both', expand='Yes') #type: ignore
var = tkr.StringVar()
songTitle = tkr.Label(player, font='Aloe', textvariable=var)
player.mainloop()
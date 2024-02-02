import tkinter as tk
import fnmatch
import os
from pygame import mixer
# help's to display the root window 
window=tk.Tk()
window.title("Music Player")
# sets the width and height of the widget
window.geometry("600x800")
window.config(bg='grey')

rootpath="C:\\Users\\Aditya\\OneDrive\\Desktop\\Pythn Project"
# selects all the mp3 files
pattern="*.mp3"
mixer.init()
# Built-in methods which is used to add user defined images
prev_img=tk.PhotoImage(file='C:\\Users\\Aditya\\OneDrive\\Desktop\\Pythn Project\\images\\prev.png')
stop_img=tk.PhotoImage(file='C:\\Users\\Aditya\\OneDrive\\Desktop\\Pythn Project\\images\\stop.png')
play_img=tk.PhotoImage(file='C:\\Users\\Aditya\\OneDrive\\Desktop\\Pythn Project\\images\\play.png')
pause_img=tk.PhotoImage(file='C:\\Users\\Aditya\\OneDrive\\Desktop\\Pythn Project\\images\\pause.png')
next_img=tk.PhotoImage(file='C:\\Users\\Aditya\\OneDrive\\Desktop\\Pythn Project\\images\\next.png')

def select():
    # It is meant to display the name of the song 
    label.config(text=listBox.get('anchor'))
    mixer.music.load(rootpath+"\\"+listBox.get('anchor'))
    mixer.music.play()

def stop():
     mixer.music.stop()
    #  here select_clear clears the selection list
     listBox.select_clear('active')

def play_next():
    next_song=listBox.curselection()
    next_song=next_song[0]+1
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    prev_song=listBox.curselection()
    prev_song=prev_song[0]-1
    prev_song_name=listBox.get(prev_song)
    label.config(text=prev_song_name)
    mixer.music.load(rootpath+"\\"+prev_song_name)
    mixer.music.play()
    listBox.select_clear(0,'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)
def pause_song():
     if pauseButton['text']=='Pause':
          mixer.music.pause()
          pauseButton ['text']=='Play'
     else:
        mixer.music.unpause()
        pauseButton['text']=='Pause'

# tk.Listbox is used to display diff type of items 
listBox=tk.Listbox(window,fg="white",bg="black",width=100)
listBox.pack(padx=15,pady=15)

# displays which song is playing currently
label = tk.Label(window, text = 'Welcome to Music Player!', bg = 'black', fg = 'white', font = ('verdana',18))
label.pack(pady = 15)

# for framing the play,pause,next,prev,stop button
top=tk.Frame(window,bg='black')
top.pack(anchor='center')

# command is like the onclick() in fsd
# Button's are defined in this section
prevButton = tk.Button (window, text = "Prev",image=prev_img,bg='grey',borderwidth=0,command=play_prev)
prevButton.pack(in_=top,side='left')

stopButton = tk. Button(window, text ='Stop',image=stop_img,bg='grey',borderwidth=0,command=stop)
stopButton.pack(in_=top,side='left')

playButton = tk. Button(window, text ='Play',image=play_img,bg='grey',borderwidth=0,command=select)
playButton.pack(in_=top,side='left')

pauseButton = tk. Button(window, text ='Pause',image=pause_img,bg='grey',borderwidth=0,command=pause_song)
pauseButton.pack(in_=top,side='left')

nextButton = tk. Button(window, text ='Next',image=next_img,bg='grey',borderwidth=0,command=play_next)
nextButton.pack(in_=top,side='left')

# made to 
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern) :
            listBox.insert('end', filename)

window.mainloop()
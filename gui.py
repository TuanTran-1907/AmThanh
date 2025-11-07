from tkinter import *
import music

root = Tk()
root.title("Music Player")

n = 0

def play():
    global n
    n+=1
    if n % 2 != 0:
        music.stop_music()
    else:
        music.play_music()
    

Button(root,text="click",command=play).pack()
# Button(root, text="Play", command=music.play_music).pack(pady=10)

if __name__ == "__main__":
    music.play_music()
    root.mainloop()
    

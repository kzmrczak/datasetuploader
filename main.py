import os
import tkinter as tk

from PIL import ImageDraw, Image

window = tk.Tk()
window.geometry('300x350')
window.title("Dataset Uploader")
val = 0
lastx, lasty = None, None

def active_draw(event):
    global lastx, lasty
    canvas.bind('<B1-Motion>', draw)
    lastx, lasty = event.x, event.y


def draw(event):
    global lastx, lasty
    x, y = event.x, event.y
    info.delete("1.0", tk.END)
    canvas.create_line((lastx, lasty, x, y), width=5, fill='white', smooth='true')
    draw1.line((lastx, lasty, x, y), fill='white', width=5)
    lastx, lasty = x, y
    global val
    if options.get():
        val = options.get()
    else:
        text = 'Choose the number!'
        info.delete("1.0", tk.END)
        info.insert(tk.END, text)

def upload():
    if options.get():
        global draw1, image1
        text = "Successfully uploaded!"
        info.delete("1.0", tk.END)
        info.insert(tk.END, text)
        i = 0
        if not os.path.exists('dataset/{}'.format(val)):
            os.makedirs('dataset/{}'.format(val))
        while os.path.exists("dataset/{}/{}_{}.png".format(val,val,i)):
            i = i + 1
        image1.save("dataset/{}/{}_{}.png".format(val,val,i))
        canvas.delete("all")
        canvas.create_rectangle((0, 0, 200, 200), fill="#000000", width=0)
        image1 = Image.new('RGB', (200, 200), 'black')
        draw1 = ImageDraw.Draw(image1)

    else:
        text = 'Choose the number!'
        info.delete("1.0", tk.END)
        info.insert(tk.END, text)

def reset():
    global image1, draw1
    canvas.delete("all")
    canvas.create_rectangle((0, 0, 200, 200), fill="#000000", width=0)
    info.delete("1.0", tk.END)
    image1 = Image.new('RGB', (200, 200), 'black')
    draw1 = ImageDraw.Draw(image1)


def returnval():
    global val
    info.delete("1.0", tk.END)
    val = options.get()


canvas = tk.Canvas(window, width = 200, height = 200)



canvas.place(x = 25, y = 25)
canvas.create_rectangle((0,0,200,200), fill="#000", width = 0)
canvas.bind("<1>", active_draw)



options = tk.StringVar()
option = options
option0 = tk.Radiobutton(window, variable = option, value = 0, text = "0", command=returnval)
option0.place(x = 250, y = 20)
option1 = tk.Radiobutton(window, variable = option, value = 1, text = "1", command=returnval)
option1.place(x = 250, y = 50)
option2 = tk.Radiobutton(window, variable = option, value = 2, text = "2", command=returnval)
option2.place(x = 250, y = 80)
option3 = tk.Radiobutton(window, variable = option, value = 3, text = "3", command=returnval)
option3.place(x = 250, y = 110)
option4 = tk.Radiobutton(window, variable = option, value = 4, text = "4", command=returnval)
option4.place(x = 250, y = 140)
option5 = tk.Radiobutton(window, variable = option, value = 5, text = "5", command=returnval)
option5.place(x = 250, y = 170)
option6 = tk.Radiobutton(window, variable = option, value = 6, text = "6", command=returnval)
option6.place(x = 250, y = 200)
option7 = tk.Radiobutton(window, variable = option, value = 7, text = "7", command=returnval)
option7.place(x = 250, y = 230)
option8 = tk.Radiobutton(window, variable = option, value = 8, text = "8", command=returnval)
option8.place(x = 250, y = 260)
option9 = tk.Radiobutton(window, variable = option, value = 9, text = "9", command=returnval)
option9.place(x = 250, y = 290)




info = tk.Text(window, height = 1, width = 24)
info.place(x = 28, y = 2)

image1 = Image.new('RGB', (200, 200), 'black')
draw1 = ImageDraw.Draw(image1)

resetButton = tk.Button(window, text="Reset", width = 27, height = 1, command = reset)
resetButton.place(x = 27 , y = 310 )
uploadButton = tk.Button(window, text="Upload", width = 27, height = 4, command = upload)
uploadButton.place(x = 27 , y = 230 )


window.mainloop()

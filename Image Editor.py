from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x600")
root.config(background = "grey")

label_image = Label(root, bg="white", highlightthickness=5)
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

img_path=""
def openFile():
    global img_path
    img_path = filedialog.askopenfilename(title=" Open Text File", filetypes=[("Image Files","*.jpg *.gif *.jpg *.png *.jpeg")])
    print(img_path)
    im = Image.open(img_path)
    rotated_img = im.rotate(180)
    img = ImageTk.PhotoImage(rotated_img)
    label_image["image"] = img
    
def rotateImage():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(180))
    label_image["image"] = img
    print(img_path)
    img.close()

    img.close()

   
btn=Button(root,text="Open Image",font= ("Times New Roman0", 12),bg="cyan",fg="black", command=openFile, relief=SOLID, padx=15, pady=10)
btn.place(relx=0.5,rely=0.1,anchor=CENTER)

btn1=Button(root,text="Rotate Image",font= ("Times New Roman0", 12),bg="cyan",fg="black", command=openFile, relief=SOLID, padx=15, pady=10)
btn1.place(relx=0.5,rely=0.8,anchor=CENTER)


root.mainloop()
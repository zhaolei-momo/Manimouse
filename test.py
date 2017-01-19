import Tkinter as tk 
#from PIL import ImageTk, Image

def func():
	root1 = tk.Tk()
	root1.title("Navigation Frame")

	root1.geometry('{}x{}'.format(480, 270))

	w1 = tk.Label(root1,text = "Sub-portion used for Cursor\nMovement of Dimensions\n 480 x 270.", font=('Helvetica',24,'bold'),justify=tk.LEFT,padx=20)
	w1.pack(pady = 50)

	root1.mainloop()

root = tk.Tk()
root.title("Test Window")


#bgi = tk.PhotoImage(file = 'yo.gif')
w = tk.Label(root,text = "Video Frame of Dimensions 1920 x 1080.", font=('Helvetica',36,'bold'),justify=tk.LEFT,padx=40)
w.pack(pady = 100)

run1 = tk.PhotoImage(file = 'run.gif')
runButton = tk.Button(root,image = run1, command = func)
runButton.pack(side = tk.BOTTOM,pady = 20)

root.geometry('{}x{}'.format(1920, 1080))
#root.resizable(width=False, height=False)


#canvas=tk.Canvas(root,bg='grey',height=400,width=800)

#filename = ImageTk.PhotoImage(Image.open("ITSPlogo.gif"))
#image = canvas.create_image(250, 250,  image=filename)

#panel = Label(root, image = image)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()

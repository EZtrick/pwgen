import tkinter as tk
from pwgen import *



root = tk.Tk()

root.title("PWGEN")

#can change starting position
#root.geometry("+700+520")

# Gets the requested values of the height and width.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
#print("Width",windowWidth,"Height",windowHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)
#positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

canvas = tk.Canvas(root, width=300, height=100)
canvas.grid(columnspan=3,rowspan=3)

#instructions
instructions = tk.Label(root, text="Generate a secure password", font="Helvetica")
instructions.grid(columnspan=3, column=0, row=0)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_pass():
    #gives temporary new name to the button
    #generate_text.set("Generating...")
    password = gen()

    #text box
    #all the hashes underneath are from how the command originally looked
    #text_box = tk.Text(root, height=1, width=15, padx=15, pady=15)
    text_box.insert(1.0, password)
    #text_box.tag_configure("center", justify="center")
    #text_box.tag_add("center", 1.0, "end")
    #text_box.grid(column=1, row=5)

    #sets button back to what it was before "generating"
    #generate_text.set("Generate Password")


#generate button
#can add bg value of #20bebe for blue background
#can add fg value for text colour, eg "white"
generate_text = tk.StringVar()
generate_btn = tk.Button(root, textvariable=generate_text, command=lambda:get_pass(), font ="Helvetica", height=2, width=15)
generate_text.set("Generate Password")
generate_btn.grid(column=1, row=2)


text_box = tk.Text(root, height=1, width=15, padx=15, pady=15)
text_box.tag_configure("center", justify="center")
text_box.tag_add("center", 1.0, "end")
text_box.grid(column=1, row=3)

#add below for extra size on the window at the bottom
canvas = tk.Canvas(root, width=300, height=50)
canvas.grid(columnspan=3)

root.mainloop()
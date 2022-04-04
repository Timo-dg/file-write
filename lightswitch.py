# schijf hier tussen je code
import tkinter as tk
window = tk.Tk()

file = open('C:/Users/timo/Documents/GitHub/file-write/actions.log', 'a')


button = tk.Button(text= 'Switch light on', bg='white', fg='black')
button.pack(pady = 20, padx = 20)

def clickButton(event):
    button.config(text='Switch light on')
    file.writelines('Switch light on\n')
    print ("Switch light on")
    window['bg'] = 'yellow'
button.bind("<Button-1>", clickButton)

def clickButton2(event):
    button.config(text='Switch light off')
    file.writelines('Switch light off\n')
    print ("Switch light off")
    window['bg'] = 'black'
button.bind("<Button-3>", clickButton2)
# schijf hier tussen je code
window.mainloop()
from tkinter import *

class fooFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.inputText=Label(self)
        self.inputText["text"]="Input:"
        self.inputText.grid(row=0,column=0)

if __name__ == '__main__':
    winObj = Tk()
    contain=fooFrame(master=winObj)
    contain.pack()
    winObj.mainloop()

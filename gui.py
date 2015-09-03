from tkinter import *

class fooFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # "Input:"
        self.inputText=Label(self)
        self.inputText["text"]="Input:"
        self.inputText.grid(row=0,column=0)

        # "_______" (input Field)
        self.inputField=Entry(self)
        self.inputField["width"]=50
        self.inputField.grid(row=0,column=1,columnspan=6)




if __name__ == '__main__':
    winObj = Tk()
    contain=fooFrame(master=winObj)
    contain.pack()
    winObj.mainloop()


from Tkinter import *
import os
class TraversalDemo:
    def __init__(self, root):
        
        


        root.title('Project GUI')
        #TAKING GESTURE CODE
        button = Button(root, text = "Take gesture")
        button.pack()

        def callback():
            print('Take gesture')#call module instead of print
            os.system('TAKE.py')

        button.config(command = callback)
        #TAKE GESTURE ENDS
        
    #button.invoke()
        #TEXT FILE INPUT
        label_1 = Label(root, text="Write meaning: ")
        label_1.pack()
        entry_1 = Entry(root)
        entry_1.pack()
        button = Button(root, text="Assign")
        button.pack()
        
        def print_to_console():
            os.system('TEXT.py')
           # if( len(entry_1.get()) > 0 ):
            #        print entry_1.get()
            #else:
            #        print "Entry field is empty, add some text and try again"

        button.config(command = print_to_console)               
        #TEXT FILE COMPLETE


        #PROCESS CODE STARTS
        button = Button(root, text = "Process")
        button.pack()

        def callback():
                print('Process')#call module instead of print
                os.system('tempcomb.py')
        button.config(command = callback)
        #button.invoke()
        #PROCESS CODE ENDS

        #EXIT CODE
        button = Button(root, text = "exit")
        button.pack()

        def callback():
                exit();
        button.config(command = callback)
        #EXIT CODE ENDS

                #SAY CODE STARTS
        button = Button(root, text = "Say")
        button.pack()

       

root = Tk()
app = TraversalDemo(root)
root.mainloop()

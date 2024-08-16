from tkinter import *

# Function to create a frame with specific packing options
def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=NO, fill=BOTH)  # expand=NO means the frame will not expand to fill available space
    return w

# Function to create a button with specified text and command
def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)  # expand=YES means the button will expand to fill available space
    return w

# Calculator class to define the UI and logic
class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Simple Calculator by Dawood Sarfraz')
        self.master.iconname("calc1")
        
        # StringVar to hold the display text
        display = StringVar()
        # Entry widget for the display
        Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)

        # Create operator buttons on the right side
        opsF = frame(self, RIGHT)
        for char in "+-*/=":
            if char == '=':
                # Bind the '=' button to calculate the result
                btn = button(opsF, RIGHT, char)
                btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                # Other operator buttons append the operator to the display
                btn = button(opsF, TOP, char, lambda w=display, c=char: w.set(w.get()+' '+c+' '))
        
        # Create number buttons in the grid format
        for key in ("123", "456", "789", ",0."):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w=display, s=' %s '%char: w.set(w.get()+s))
        
        # Clear button to reset the display
        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clear', lambda w=display: w.set(''))

    # Function to evaluate the expression in the display
    def calc(self, display):
        try:
            # Evaluate the expression safely
            display.set(eval(display.get()))
        except Exception:
            # Catch any exceptions and show "ERROR"
            display.set("ERROR")

# Run the Calculator application
if __name__ == '__main__':
    Calculator().mainloop()


# Exercise 5 on "How to think like a computer scientist", ch. 11.
from tkinter import filedialog
import turtle

def main():
    name = filedialog.askopenfilename(title="Choose File")
    
    screen = turtle.Screen()
    t = turtle.Turtle()
    

    # Use t.up(), t.down() and t.goto(x, y)

    # Put your code here
    with open(name, "r") as fin:
        for line in fin:
            line = line.strip()
            if line == "UP":
                t.up()
            elif line == "DOWN":
                t.down()
            else:
                parts = line.split()
                x = int(parts[0])
                y = int(parts[1])
                t.goto(x, y)

    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()


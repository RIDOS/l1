import tkinter as tk
import DigitDrawer as Digit

root = tk.Tk()
app = Digit.DigitDrawingApp(root)

# Выравнивание элементов по центру окна
app.root.update_idletasks()
width = app.root.winfo_width()
height = app.root.winfo_height()

# Выравнивание элементов по центру экрана
x = (app.root.winfo_screenwidth() // 2) - (width // 2)
y = (app.root.winfo_screenheight() // 2) - (height // 2)
app.root.geometry(f"{width}x{height}+{x}+{y}")

root.mainloop()

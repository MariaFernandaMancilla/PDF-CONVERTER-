import tkinter as tk
from PIL import Image, ImageTk
import gui


def show_splash():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.configure(bg="#FFFFFF")
    splash.geometry("500x300+400+200")

    label = tk.Label(splash, text="PDF CONVERTER",
                     font=("Arial", 18), bg="#FFFFFF")
    label.pack(expand=True)

    def launch_main_app():
        splash.destroy()
        gui.main()

    splash.after(2000, launch_main_app)
    splash.mainloop()


# Ejecuta la función
if __name__ == "__main__":
    show_splash()

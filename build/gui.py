import sys
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label, ttk
from PIL import Image, ImageTk
from hilos import run_conversion_in_thread


def relative_to_assets(path: str) -> Path:
    base_path = getattr(sys, '_MEIPASS', Path(__file__).parent)
    return Path(base_path) / "assets" / "frame0" / "frame0" / "frame0" / path


def main():
    window = Tk()
    window.geometry("550x700")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)
    window.title("PDF TO WORD CONVERTER")

    try:
        logo_path = relative_to_assets("icon.jpg")
        logo_image = Image.open(logo_path)
        logo_photo = ImageTk.PhotoImage(logo_image)
        window.iconphoto(False, logo_photo)
    except Exception as e:
        print("Error:", e)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=700,
        width=550,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    canvas.create_rectangle(0.0, 0.0, 550.0, 195.0, fill="#DA5759", outline="")
    canvas.create_text(36.0, 76.0, anchor="nw",
                       text="PDF TO WORD CONVERTER",
                       fill="#FFFFFF", font=("Inter", 36 * -1))

    status_label = Label(
        window,
        text="",
        font=("Arial", 12),
        fg="#000000",
        bg="#FFFFFF"
    )
    status_label.place(x=225, y=463)

    progress = ttk.Progressbar(
        window,
        orient="horizontal",
        length=200,
        mode="determinate"
    )

    file_label = Label(
        window,
        text="",
        font=("Arial", 10),
        fg="#555555",
        bg="#FFFFFF"
    )

    try:
        chat_img_path = relative_to_assets("imagen_chat.png")
        chat_img = Image.open(chat_img_path)
        chat_img = chat_img.resize((180, 180))
        chat_photo = ImageTk.PhotoImage(chat_img)

        label_chat = Label(window, image=chat_photo, bg="#FFFFFF")
        label_chat.image = chat_photo
        label_chat.place(x=180, y=210)
    except Exception as e:
        print("Could not load image_chat.png:", e)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))

    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_conversion_in_thread(
            status_label, progress, file_label, window),


        relief="flat",
        cursor="hand2"
    )
    button_1.place(x=136.0, y=390.0, width=302.0, height=127.0)

    def on_hover(event):
        button_1.config(image=button_image_2)

    def on_leave(event):
        button_1.config(image=button_image_1)

    button_1.bind("<Enter>", on_hover)
    button_1.bind("<Leave>", on_leave)

    window.mainloop()


if __name__ == "__main__":
    main()

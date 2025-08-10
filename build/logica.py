from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os
import time


def convert_multiple_pdfs_with_progress(progress, file_label, window):
    file_paths = filedialog.askopenfilenames(
        title="Select one or more pdf files...",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not file_paths:
        messagebox.showwarning("Warning", "You didnt select any file...")
        return False

    save_folder = filedialog.askdirectory(
        title=""
    )
    if not save_folder:
        messagebox.showwarning(
            "Warning", "No destination folder selected.")
        return False

    total_files = len(file_paths)
    progress["maximum"] = 100

    progress.place(x=(550 - 200) // 2, y=550)
    file_label.place(x=0, y=515)

    for file_index, file_path in enumerate(file_paths):
        try:
            filename = os.path.basename(file_path)
            file_label.config(text=f"Converting: {filename}")
            window.update_idletasks()

            text_width = file_label.winfo_reqwidth()
            center_x = (550 - text_width) // 2
            file_label.place(x=center_x, y=515)

            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(save_folder, base_name + ".docx")

            for i in range(0, 101, 5):
                progress["value"] = i
                window.update_idletasks()
                time.sleep(0.02)

            cv = Converter(file_path)
            cv.convert(output_path, start=0, end=None)
            cv.close()

            print(f"✅ Converted: {output_path}")

        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred with {file_path}:\n{e}"
            )

        if file_index < total_files - 1:
            progress["value"] = 0
            window.update_idletasks()

    progress["value"] = 100
    file_label.config(text="")
    progress.place_forget()
    window.update_idletasks()

    messagebox.showinfo(
        "Finished", "All files have been converted successfully."
    )

    return True

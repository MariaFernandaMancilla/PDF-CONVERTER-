import threading
from logica import convert_multiple_pdfs_with_progress
from tkinter import messagebox

lock = threading.Lock()


def run_conversion_in_thread(status_label, progress, file_label, window):

    if not lock.locked():
        thread = threading.Thread(
            target=lambda: safe_convert(
                status_label, progress, file_label, window)
        )

        thread.daemon = True
        thread.start()
    else:
        messagebox.showwarning(
            "Please wait", "A conversion is already in progress.")


def safe_convert(status_label, progress, file_label, window):
    with lock:
        try:
            status_label.config(text="")
            progress["value"] = 0
            progress.place(x=180, y=550)
            window.update_idletasks()

            conversion_realizada = convert_multiple_pdfs_with_progress(
                progress, file_label, window)

            if conversion_realizada:
                status_label.config(text="Completed")
                progress["value"] = 100
            else:
                status_label.config(text="")

        except Exception as e:
            status_label.config(text="❌ Error")
            print(f"❌ Error: {e}")

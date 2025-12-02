import psutil
import time
from plyer import notification
import tkinter as tk
from threading import Thread
import winsound

notified = False

def send_notification():

    notification.notify(
        title="Battery Notification ⚡",
        message="Battery has reached 99%. You can unplug the charger.",
        timeout=10
    )

    Thread(target=show_popup_with_sound_loop).start()

def show_popup_with_sound_loop():

    winsound.PlaySound("file_example_WAV_1MG.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    root = tk.Tk()
    root.title("Battery Alert 🔋")
    root.geometry("300x100+100+100")
    root.configure(bg="red")
    root.attributes("-topmost", True)

    label = tk.Label(
        root,
        text="Battery at 99%\nUnplug the charger!",
        font=("Helvetica", 12, "bold"),
        bg="red",
        fg="white"
    )
    label.pack(expand=True)


    def on_close():
        winsound.PlaySound(None, winsound.SND_PURGE)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.after(10000, on_close)
    root.mainloop()

while True:
    battery = psutil.sensors_battery()
    if battery is None:
        time.sleep(60)
        continue

    percent = battery.percent
    plugged = battery.power_plugged

    if percent >= 97 and plugged and not notified:
        send_notification()
        notified = True

    elif not plugged:
        notified = False

    time.sleep(60)
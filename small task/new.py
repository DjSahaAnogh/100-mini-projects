import pyautogui
import tkinter as tk
import time
import threading
from datetime import datetime

clicking = False

def check_time():
    """Check if the current time is 9:45 AM and stop clicking."""
    now = datetime.now().strftime('%H:%M')
    return now == '09:45'

def start_clicking(event):
    global clicking
    clicking = True
    def click_loop():
        while clicking:
            if check_time():
                break
            pyautogui.click()
            time.sleep(1.5)  # 1.5s gap between clicks
    
    thread = threading.Thread(target=click_loop)
    thread.daemon = True
    thread.start()

def stop_clicking(event):
    global clicking
    clicking = False

# Create GUI window
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("200x100")

button = tk.Button(root, text="Hover to Click", font=("Arial", 12))
button.pack(pady=20)

# Bind hover events
button.bind("<Enter>", start_clicking)
button.bind("<Leave>", stop_clicking)

root.mainloop()

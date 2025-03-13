import time
import platform
import os

def beep() -> None:
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 1000)
    else:
        os.system("echo -e '\a'")

def clock() -> None:
    user_input = input("Enter the countdown time(MM:SS): ")
    min, sec = map(int, user_input.split(":"))
    total_seconds = min * 60 + sec
    print(f"⏳ Countdown set for {min} minutes and {sec} seconds. Waiting for {total_seconds} seconds...")
    time.sleep(total_seconds)
    print("\n⏰ Time's up! ⏰")
    for _ in range(5):
        beep()
        time.sleep(1)
if __name__ == "__main__":
    clock()
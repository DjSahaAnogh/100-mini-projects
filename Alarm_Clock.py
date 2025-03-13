import time
import datetime
import platform
import os

def beep() -> None:
    """Plays a beep sound based on the OS."""
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 1000)  # 1000 Hz for 1 second
    else:
        os.system("printf '\a'")  # Works on most Linux/macOS terminals

def alarm_clock():
    """Converts time input to seconds and sleeps until alarm time."""
    user_input = input("Enter the alarm time (HH:MM:SS): ")
    
    # Get current datetime
    now = datetime.datetime.now()
    
    # Convert user input to a datetime object (today's date + given time)
    target_time = datetime.datetime.strptime(user_input, "%H:%M:%S").time()
    alarm_time = datetime.datetime.combine(now.date(), target_time)

    # If the time has already passed today, set it for tomorrow
    if alarm_time < now:
        alarm_time += datetime.timedelta(days=1)

    # Calculate seconds to wait
    seconds_to_wait = (alarm_time - now).total_seconds()
    
    print(f"⏳ Alarm set for {user_input}. Waiting for {int(seconds_to_wait)} seconds...")
    
    # Sleep until the alarm time
    time.sleep(seconds_to_wait)

    # Alarm goes off
    print("\n⏰ Wake up! ⏰")
    for _ in range(5):  # Beep multiple times
        beep()
        time.sleep(1)

if __name__ == "__main__":
    alarm_clock()

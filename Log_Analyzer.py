from collections import Counter

def log_analyzer() -> Counter:
    fliename: str = input("Enter the name of the log file: ")
    with open(fliename, 'r') as file:
        log_data = file.readlines()
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]
    log_counts = Counter()

    for line in log_data:
        for level in log_levels:
            if level in line:
                log_counts[level] += 1
    def get_log_time_range(log_file):
        with open(log_file, "r") as file:
            first_line = file.readline().strip()  # Read the first line
            last_line = None

            # Read the last line efficiently
            for line in file:
                last_line = line.strip()

        # Extract timestamps from first and last lines
        start_time = first_line.split(" ", 1)[0] if first_line else "Unknown"
        end_time = last_line.split(" ", 1)[0] if last_line else "Unknown"

        return start_time, end_time
    start_time, end_time = get_log_time_range(fliename)
    def report(log_counts, start_time, end_time):
        import datetime
        import platform
        if platform.system() == "Windows":
            import os
            base_name = "log_report"
            count = 1
            while os.path.exists(f"{base_name}_{count}.txt"):
                    counter += 1
            filename = f"{base_name}_{count}.txt"
        else:  # macOS and Linux
            directory = os.path.expanduser("~/Documents/")  # Save in ~/Documents/
            os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
            while os.path.exists(os.path.join(directory, f"{base_name}_{count}.txt")):
                count += 1
            filename = os.path.join(directory, f"{base_name}_{count}.txt")
        with open(filename, "w") as log_report:
            log_report.write(f"Log report generated on {datetime.datetime.now()}\n")
            log_report.write(f"Log time range: {start_time} - {end_time}\n\n")
            for level, count in log_counts.items():
                log_report.write(f"{level}: {count}\n")
    report(log_counts, start_time, end_time)

if __name__ == "__main__":
    log_analyzer()

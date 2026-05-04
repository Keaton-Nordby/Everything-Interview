# Log levels (INFO, ERROR, DEBUG)
# Store logs in memory
# Filter logs
from datetime import datetime

logs = []


# add log to log list
def add_log(logs, level, message):
    log = {
        "level" : level,
        "message" : message,
        "timestamp" : datetime.now()
    }
    logs.append(log)
    

# filtering logs by level 
def filter_logs(logs, level):
    return [log for log in logs if log["level"] == level]


# printing logs
def print_logs(logs):
    for log in logs:
        print(f"[{log['timestamp']}] [{log['level']}] {log['message']}")


add_log(logs, "INFO", "User logged in")
add_log(logs, "ERROR", "Database failed")
add_log(logs, "DEBUG", "x = 42")
add_log(logs, "INFO", "User clicked button")


print("\nERROR LOGS ONLY:")
error_logs = filter_logs(logs, "ERROR")
print_logs(error_logs)
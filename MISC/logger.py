# Log levels (INFO, ERROR, DEBUG)
# Store logs in memory
# Filter logs


logs = []


def add_log(logs, level, message):
    log = {
        "level" : level,
        "message" : message
    }
    logs.append(log)
    
    
def filter_logs(logs, level):
    return [log for log in logs if log["level"] == level]


def print_logs(logs):
    for log in logs:
        print(f"[{log['level']}] {log['message']}")


add_log(logs, "INFO", "User logged in")
add_log(logs, "ERROR", "Database failed")
add_log(logs, "DEBUG", "x = 42")
add_log(logs, "INFO", "User clicked button")


print("\nERROR LOGS ONLY:")
error_logs = filter_logs(logs, "ERROR")
print_logs(error_logs)
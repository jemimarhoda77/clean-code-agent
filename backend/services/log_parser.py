def parse_logs(log_text):
    logs = []
    for line in log_text.split("\n"):
        if line:
            logs.append({
                "message": line
            })
    return logs
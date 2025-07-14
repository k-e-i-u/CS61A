# example: configuration
def create_logger(log_level):
    def log(message):
        if log_level == "DEBUG":
            print(f"DEBUG: {message}")
        elif log_level == "ERROR":
            print(f"ERROR: {message}")
    return log

# 通过curring的方法，
debug_log = create_logger("DEBUG")
error_log = create_logger("ERROR")

debug_log("test")  # DEBUG: test
error_log("test")  # ERROR: test
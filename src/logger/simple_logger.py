# This is a simple logger that just prints the log message to the console
class BaseLogger:
    def __init__(self) -> None:
        self.info = print

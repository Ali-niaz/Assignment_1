# message_formatter.py

# Decorator 1: Add a pixel-style frame
def pixel_frame(func):
    def wrapper(message):
        border = "▓" * (len(message) + 8)
        return f"{border}\n▓  {func(message)}  ▓\n{border}"
    return wrapper

# Decorator 2: Add arcade emojis and stars
def arcade_decorator(func):
    def wrapper(message):
        return f"👾 ★ {func(message)} ★ 🕹️"
    return wrapper

# main.py
from .message_formatter import pixel_frame, arcade_decorator

@pixel_frame
@arcade_decorator
def display_message(msg):
    return msg

if __name__ == "__main1__":
    print(display_message("Insert Coin to Start"))
    print()
    print(display_message("Game Over! Try Again?"))


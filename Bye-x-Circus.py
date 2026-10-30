import os
import sys
import time
from threading import Thread, Lock

lock = Lock()

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def animate_text(text, speed):
    with lock:
        sys.stdout.write("\033[1;95m")
        try:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed)
        finally:
            sys.stdout.write("\033[0m\n")
            sys.stdout.flush()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nThere's only two types of people in the world", 0.08),
        ("The ones that entertain and the ones that observe", 0.09),
        ("Well, baby, I'm a put-on-a-show kinda girl", 0.09),
        ("Don't like the backseat, gotta be first (Oh, oh)", 0.09),
        ("", 0.05),
        ("I'm like the ringleader, I call the shots (Call the shots)", 0.07),
        ("I'm like a firecracker, I make it hot when I put on a show", 0.08),
        ("", 0.05),
        ("I feel the adrenaline movin' through my veins", 0.10),
        ("Spotlight on me and I'm ready to break", 0.09),
        ("I'm like a performer, the dance floor is my stage", 0.07),
        ("Better be ready, hope that you feel the same", 0.07),
        ("", 0.05),
    ]

    delays = [0.1, 4.4, 8.4, 12.6, 17.0, 18.0, 21.4, 27.5, 28.0, 32.0, 37.0, 42.0, 43.0
    ]

    os.system("cls" if os.name == "nt" else "clear")
    hide_cursor()

    try:
        threads = [
            Thread(
                target=sing_lyric,
                args=(lyric, delays[i], speed)
            )
            for i, (lyric, speed) in enumerate(lyrics)
        ]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    finally:
        show_cursor()


if __name__ == "__main__":
    sing_song()
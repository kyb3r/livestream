import os
import random
import subprocess

STREAM_URL = os.getenv('STREAM_URL')

def livestream_files():
    directory = os.listdir('videos')
    random.shuffle(directory)
    for video in directory:
        command = (
            f"ffmpeg -re -i 'videos/{video}' -c:v libx264 -preset veryfast -maxrate 3000k "
            f"-bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 "
            f"-ar 44100 -f flv {STREAM_URL}"
        ).split()
        print("Starting livestream for:", video)
        subprocess.run(command, capture_output=True)
        try:
            os.remove('None')
        except FileNotFoundError:
            pass
        print("Finished livestream for:", video)
        print()


while True:
    try:
        livestream_files()
    except KeyboardInterrupt:
        print('\nStopped livestream')
        break
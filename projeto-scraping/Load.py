from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

def loader(string, final):
    
    class Loader:
        def __init__(self, desc="", end='\033[1m'+final+'\033[0m!', timeout=0.1):

            self.desc = desc
            self.end = end
            self.timeout = timeout

            self._thread = Thread(target=self._animate, daemon=True)
            self.steps = ['⢿ ', '⣻ ', '⣽ ', '⣾ ', '⣷ ', '⣯ ', '⣟ ', '⡿ ']
            self.done = False

        

        def start(self):
            self._thread.start()
            return self

        def _animate(self):
            for c in cycle(self.steps):
                if self.done:
                    break
                print(f"\r{self.desc} {c}", flush=True, end="")
                sleep(self.timeout)

        def __enter__(self):
            self.start()

        def stop(self):
            self.done = True
            cols = get_terminal_size((80, 20)).columns
            print("\r" + " " * cols, end="", flush=True)
            print(f"\r{self.end}", flush=True)

        def __exit__(self, exc_type, exc_value, tb):
            self.stop()


    
    with Loader('\033[1m'+string+'\033[0m'):
        for i in range(20):
            sleep(0.25)

    sleep(1.5)
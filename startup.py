import threading
import time
import os


class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=60):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution
        thread.join()

    def run(self):
        """ Method that runs forever """
        os.system("python3 MoonBot.py")

while 0 == 0:
    example = ThreadingExample()
    time.sleep(30)
    print('Bot died :(')
time.sleep(30)
print('Bye')

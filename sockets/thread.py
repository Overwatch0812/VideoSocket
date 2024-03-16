import threading
from .mlModels.functions1 import *
from .mlModels.micro_functions import *

class RunThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.camera=cv2.VideoCapture(0)
    def run(self):
        try:
            print('execution started')
            data = run(self.camera)
            if data:
                data = 'ok'
            else:
                data = "alert"
        except Exception as e:
            print(e)
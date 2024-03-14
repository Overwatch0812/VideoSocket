from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from .mlModels.functions import *

class SyncSocketConsumer(SyncConsumer):
    camera=cv2.VideoCapture(0)
    def websocket_connect(self,event):
        print('Connect...')
        self.camera=cv2.VideoCapture(0)
        self.send({
            'type':'websocket.accept',
            })
    def websocket_disconnect(self,event):
        print('disconnected')
        try:
            self.camera.release()
        except AttributeError:
            pass
        raise StopConsumer()
    def websocket_receive(self,event):
        print("Message received from client",)
        data=run(self.camera)
        print(data)
        self.send({'type':'websocket.send',
        'text':data})

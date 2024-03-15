from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from .mlModels.functions1 import *
# from .mlModels.functions2 import *
class SyncSocketConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Connected...')
        self.camera=cv2.VideoCapture(0)
        self.start_time = time.time()

        # while time.time() - self.start_time < 180:
        #     # print(time.time() - start_time)  # Run for 180 seconds
        #     self.ret, self.frame = self.camera.read()
        #     self.count = 0
        #     for i in self.frame:
        #         self.count += len(i) 
        #     verification = verify(frame)
        #     if verification:
        #         verification = "verified"
        #         break
        #     else:
        #         continue
        self.send({
            'type':'websocket.accept',
            # 'text':verification
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
        if data:
            data='ok'
        else:
            data="alert"
        self.send({'type':'websocket.send',
        'text':data})

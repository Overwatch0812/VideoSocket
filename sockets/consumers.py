# from channels.consumer import SyncConsumer
# from channels.exceptions import StopConsumer
# from .mlModels.functions1 import *

# class SyncSocketConsumer(SyncConsumer):
#     def websocket_connect(self,event):
#         print('Connected...')
#         self.camera=cv2.VideoCapture(0)
#         self.start_time = time.time()
#         self.send({
#             'type':'websocket.accept',
#             })

#     def websocket_disconnect(self,event):
#         print('disconnected')
#         try:
#             self.camera.release()
#         except AttributeError:
#             pass
        

#     def websocket_receive(self,event):
#         print("Message received from client",)
#         data=run(self.camera)
#         if data:
#             data='ok'
#         else:
#             data="alert"
#         self.send({'type':'websocket.send',
#         'text':data})







# from channels.consumer import SyncConsumer
# from channels.exceptions import StopConsumer
# from threading import Thread
# from .mlModels.functions1 import *
# from .mlModels.micro_functions import *

# class SyncSocketConsumer(SyncConsumer):
#     def _init_(self, *args, **kwargs):
#         super()._init_(*args, **kwargs)
#         self.camera = None
#         self.sim = None

#     def websocket_connect(self, event):
#         print('Connected...')
#         self.camera = cv2.VideoCapture(0)
#         self.start_time = time.time()
#         # self.thread_similarity = Thread(target=self.process_similarity)
#         # self.thread_similarity.start()

#         self.send({
#             'type': 'websocket.accept',
#         })

#     def websocket_disconnect(self, event):
#         # print('Disconnected')
#         # try:
#         #     self.camera.release()
#         # except AttributeError:
#         pass

#     def websocket_receive(self, event):
#         print("Message received from client")
#         data = run(self.camera)
#         if data:
#             data = 'ok'
#         else:
#             data = "alert"
#         self.send({'type': 'websocket.send', 'text': data})

#     def process_similarity(self):
#         text = listen()
#         paper='''What is DSA?,
#             Define Machine learning.
#             Explain merge sort.
#             How to deploy a  Machine learning model??
#         '''
#         similarity = compare_files(text, paper)
#         if similarity > 50:
#             self.sim = False
#         else:
#             self.sim = True

# from channels.consumer import SyncConsumer
# from .mlModels.functions1 import *
# from .mlModels.micro_functions import *
# from threading import Thread
# import time

# class SyncSocketConsumer(SyncConsumer):
#     def _init_(self, *args, **kwargs):
#         super()._init_(*args, **kwargs)
#         self.camera = None
#         self.sim = None

#     def websocket_connect(self, event):
#         print('Connected...')
#         self.start_time = time.time()
#         self.thread_similarity = Thread(target=self.process_similarity)
#         self.thread_similarity.start()
#         self.camera = cv2.VideoCapture(0)
#         self.send({
#             'type': 'websocket.accept',
#         })

#     def websocket_disconnect(self, event):
#         print('Disconnected')
#         try:
#             self.camera.release()
#         except AttributeError:
#             pass

#     def websocket_receive(self, event):
#         print("Message received from client")
#         data = run(self.camera)
#         if data:
#             if self.sim:
#                 data = 'ok'
#         else:
#             data = "alert"
#         self.send({'type': 'websocket.send', 'text': data})

#     def process_similarity(self):
#         self.camera = cv2.VideoCapture(0)
#         while True:
#             text = listen()
#             if text is None:
#                 speak('No voice detected')
#                 op='None'
#             else:
#                 paper='''What is DSA?,
#                     Define Machine learning.
#                     Explain merge sort.
#                     How to deploy a  Machine learning model??'''
#                 opf=compare_files(text,paper)
#                 opf = int(opf)
#                 op = str(opf)
#             if op == "None":
#                 self.sim = True
#             elif op > 10.0:
#                 speak('similarity detected')
#                 self.sim = True
#             else:
#                 self.sim = False
#                 speak('No similarity detected')
# #             time.sleep(1)  # Adjust the delay as needed
# import asyncio
# from channels.generic.websocket import AsyncWebsocketConsumer
# from .mlModels.functions1 import *
# from .mlModels.micro_functions import *
# import json
# import threading

# class AsyncSocketConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         print('Connected...')
#         await self.accept()
#         self.sim = None
#         self.start_time = time.time()

#         # Start the functions in separate threads
#         listen_thread = threading.Thread(target=self.listen_function)
#         listen_thread.start()

#         run_thread = threading.Thread(target=self.run_function)
#         run_thread.start()

#     async def disconnect(self, close_code):
#         print('Disconnected')

#     async def receive(self, text_data):
#         pass
#         # print("Message received from client")

#     def listen_function(self):
#         while True:
#             text = listen()
#             if text is None:
#                 speak('No voice detected')
#                 op = 'None'
#             else:
#                 paper = '''What is DSA?,
#                            Define Machine learning.
#                            Explain merge sort.
#                            How to deploy a Machine learning model??'''
#                 opf = compare_files(text, paper)
#                 opf = int(opf)
#                 op = str(opf)
#             if op == "None":
#                 self.sim = True
#             elif opf > 10.0:
#                 speak('similarity detected')
#                 self.sim = True
#             else:
#                 self.sim = False
#                 speak('No similarity detected')

#     def run_function(self):
#         camera = cv2.VideoCapture(0)
#         while True:
#             data = run(camera)
#             if data:
#                 if self.sim:
#                     data = 'ok'
#             else:
#                 data = "alert"
#             # Send data to the client
#             asyncio.run_coroutine_threadsafe(
#                 self.send(text_data=json.dumps({'text': data})),
#                 asyncio.get_event_loop()
#             )

# Working

from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from .mlModels.functions1 import *
import pyautogui

class VideoSyncSocketConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('Connected...')
        self.camera=cv2.VideoCapture(0)
        self.imgCount = 1
        self.start_time = time.time()
        await self.send({
            'type':'websocket.accept',
            })

    async def websocket_disconnect(self,event):
        print('disconnected')
        try:
            self.camera.release()
        except AttributeError:
            pass
        

    async def websocket_receive(self,event):
        print("Message received from client",)
        data=run(self.camera)
        if data:
            data='ok'
        else:
            data="alert"
            ret,frame = self.camera.read()
            cv2.imwrite(f"webimg{self.imgCount}.jpg", frame)
            pyautogui.screenshot().save(f"ss{self.imgCount}.jpg")
            self.imgCount += 1

        await self.send({'type':'websocket.send',
        'text':data})


# from channels.consumer import AsyncConsumer
# from channels.exceptions import StopConsumer
# from .mlModels.functions1 import *
# from .mlModels.micro_functions import *

# class SyncAudioSocketConsumer(AsyncConsumer):
#     async def websocket_connect(self,event):
#         print('Connected...')
#         self.camera=cv2.VideoCapture(0)
#         self.start_time = time.time()
#         await self.send({
#             'type':'websocket.accept',
#             })

#     async def websocket_disconnect(self,event):
#         print('disconnected')
#         try:
#             self.camera.release()
#         except AttributeError:
#             pass
#         raise StopConsumer()

#     async def websocket_receive(self,event):
#         print("Message received from client",)
#         op=''
#         text=listen()
#         print(text)
#         if text is None:
#             op='None'
#         else:
#             paper='''What is DSA?,
#                 Define Machine learning.
#                 Explain merge sort.
#                 How to deploy a  Machine learning model??'''
#             op=str(cosine(text.lower(),paper.lower()))
#             print(op)
#         await self.send({'type':'websocket.send',
#         'text':op})



# import asyncio
# from channels.generic.websocket import AsyncWebsocketConsumer
# from .mlModels.functions1 import *
# from .mlModels.micro_functions import *
# import json
# import threading

# class AsyncSocketConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         print('Connected...')
#         await self.accept()
#         self.camera = cv2.VideoCapture(0)
#         self.sim = None
#         self.start_time = time.time()

#         self.listen_task = asyncio.create_task(self.process_similarity())
#         self.self.run_task =asyncio.create_task(self.run_function())

#     async def disconnect(self, close_code):
#         print('Disconnected')
#         self.listen_task.cancel()
#         self.run_task.cancel()
#         # try:
#         #     self.camera.release()
#         # except AttributeError:
#         #     pass

#     async def receive(self, text_data):
#         print("Message received from client")
        

#     async def process_similarity(self):
#         while True:
#             text = listen()
#             if text is None:
#                 speak('No voice detected')
#                 op = 'None'
#             else:
#                 paper = '''What is DSA?,
#                            Define Machine learning.
#                            Explain merge sort.
#                            How to deploy a Machine learning model??'''
#                 opf = compare_files(text, paper)
#                 opf = int(opf)
#                 op = str(opf)
#             if op == "None":
#                 self.sim = True
#             elif opf > 10.0:
#                 speak('similarity detected')
#                 self.sim = True
#             else:
#                 self.sim = False
#                 speak('No similarity detected')

#     async def run_function(self):
#         camera=cv2.VideoCapture(0)
#         while True:
#             data = run(camera)
#             if data:
#                 if self.sim:
#                     data = 'ok'
#             else:
#                 data = "alert"
#             await self.send(text_data=json.dumps({'text': data}))
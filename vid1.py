from vidstream import *
import tkinter as tk
import socket
import threading
local_ip_address=socket.gethostbyname(socket.gethostname())
print(local_ip_address)
server=StreamingServer(local_ip_address,9999)
receiver=AudioReceiver(local_ip_address,8888)
window=tk.Tk()
window.title("hello")
window.geometry("500x200")

label_target_ip=tk.Label(window,text="target ip:")
label_target_ip.pack()
text_target_ip=tk.Text(window,height=1)
text_target_ip.pack()
def start_listening():
    t1=threading.Thread(target=server.start_server)
    t2=threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
def start_camera():
    camera_client=CameraClient(text_target_ip.get(1.0,'end-1c'),7777)
    t3=threading.Thread(target=camera_client.start_stream)
    t3.start()
def start_screen():
    screen_client=ScreenShareClient(text_target_ip.get(1.0,'end-1c'),7777)
    t4=threading.Thread(target=screen_client.start_stream)
    t4.start()  
def start_audio():
    audio_client=AudioSender(text_target_ip.get(1.0,'end-1c'),6666)
    t5=threading.Thread(target=audio_client.start_stream)
    t5.start()
btnl=tk.Button(window,text="start camera",width=50,command=start_listening)
btnl.pack(anchor=tk.CENTER,expand=True)

btnc=tk.Button(window,text="start camera",width=50,command=start_camera)
btnc.pack(anchor=tk.CENTER,expand=True)

btns=tk.Button(window,text="start screen sharing",width=50,command=start_screen)
btns.pack(anchor=tk.CENTER,expand=True)

btna=tk.Button(window,text="start audio",width=50,command=start_audio)
btna.pack(anchor=tk.CENTER,expand=True)

window.mainloop()

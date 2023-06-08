import redis
from redis.commands.json.path import Path
import secrets
import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageFilter, ImageTk

def get_info(e2):
    result = r.hgetall(e2.get())
    result = {k.decode(): v.decode() for k, v in result.items()}
    label = ttk.Label(text=result, wraplength=350)
    label.pack(anchor=tk.NW, padx=10, pady=5) 

def open_file():
    if len(e1.get()) == 0:
        return
    #r.hmset('client:{}')
    label = ttk.Label(text="Мои поздравления вы авторизовались!")
    label.pack(anchor=tk.NW, padx=10, pady=5) 
    size = r.dbsize()
    print(size)
    token = secrets.token_hex(16) 
    r.hmset(f'client:{size}', {'ФИО': e1.get(), 'token': token})
    label = ttk.Label(text=f'Получить информацию: (Для запроса:client:X, где Х - от 1 до {size})')
    label.pack(anchor=tk.NW, padx=10, pady=5) 
    e2 = ttk.Entry(root, width=50)
    e2.pack(anchor=tk.NW, padx=10, pady=5)
    new_button = ttk.Button(text="Get", command=lambda: get_info(e2))
    new_button.pack(anchor=tk.NW, padx=80, pady=5)
    


if __name__ == '__main__':
    r = redis.Redis(
    host='redis-17248.c299.asia-northeast1-1.gce.cloud.redislabs.com',
    port=17248,
    password='TELv1LgD1dnhBQRblHbZBeeyUzJdFJ8g')

    root = tk.Tk()
    root.title("Client")
    root.geometry("400x550")
    
    #img = PhotoImage(file='C:\\Users\\Ilyas\\AppData\\Local\\Programs\\Python\\Python310\\playground\\phoneRecognizer\\smile.png')
    imgMain = Image.open('.\smile.jpg')
    imgMain = imgMain.resize((300, 200), Image.ANTIALIAS)
    #im_file = 'C:\\Users\\Ilyas\\AppData\\Local\\Programs\\Python\\Python310\\playground\\phoneRecognizer\\smile.jpg'
    #imgMain = Image.open(im_file).convert('L')
    imgForApp = ImageTk.PhotoImage(imgMain)
    l_pict = ttk.Label(root, image=imgForApp)
    l_pict.pack(anchor=tk.NW, padx=10, pady=10)
    
    label = ttk.Label(text="Пропишите свои ФИО, чтобы авторизоваться:")
    label.pack(anchor=tk.NW, padx=10, pady=5)            
    
    e1 = ttk.Entry(root, width=50)
    e1.pack(anchor=tk.NW, padx=10, pady=5)
    
    open_button = ttk.Button(text="Entry", command=open_file)
    open_button.pack(anchor=tk.NW, padx=80, pady=5)
    
    root.mainloop()
    

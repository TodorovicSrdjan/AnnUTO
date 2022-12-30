import io
import json
import logging
import asyncio
import threading
import websockets
import urllib, base64
import pandas as pd
import matplotlib.pyplot as plt
from urllib.parse import quote

import config

#################################################################

socket_message = {
    'From':'me',
    'To':'you',
    'Message':''
}
 
################################################################# 

async def send_msg(dest_id, msg):
    async with websockets.connect(uri = config.BACKEND_WEB_SOCKET_URI) as websocket:
        socket_message['From'] = await websocket.recv()
        socket_message['To'] = dest_id
        socket_message['Message'] = msg

        await websocket.send(json.dumps(socket_message))

# # #

def run_async(func, *args, **kwargs):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        thread = RunThread(func, args, kwargs)
        thread.start()
        thread.join()
        return thread.result
    else:
        return asyncio.run(func(*args, **kwargs))

# # #

def figure_to_uri(figure, ext='png'):
    '''
    For given matplot figure return URI of base64 encoded image.
    '''
    buf = io.BytesIO()
    figure.savefig(buf, format=ext)
    buf.seek(0)
    base64Img = base64.b64encode(buf.read())

    return 'data:image/png;base64,' + urllib.parse.quote(base64Img)
    
# # #   

def read_json_data(url):
    json_data = None

    logging.info('url: ' + url)

    encoded_url = quote(url).replace('http%3A', 'http:')

    if not encoded_url.startswith('http'):
        encoded_url = 'http://' + encoded_url
    
    logging.info('encoded_url: ' + encoded_url)

    with urllib.request.urlopen(encoded_url) as data:
        json_data = data.read()

    return json.loads(json_data)

#################################################################
# # # Classes     
class RunThread(threading.Thread):
    def __init__(self, func, args, kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = asyncio.run(self.func(*self.args, **self.kwargs))
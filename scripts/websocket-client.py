#!/usr/bin/env python

import asyncio
import json
import requests
import sys
import time
import websockets


async def user_supplied_command(port):
    async with websockets.connect('ws://127.0.0.1:{}'.format(port)) as websocket:
        user_inpurt = input("input: ")
        await websocket.send(user_inpurt)
        print("> {}".format(user_inpurt))

        response = await websocket.recv()
        print("< {}".format(response))

async def run_commnad(port):
    async with websockets.connect('ws://127.0.0.1:{}'.format(port)) as websocket:
        start = json.dumps({'type': 'run'})
        await websocket.send(start)
        print("> {}".format(start))

        for i in range(10):
            response = await websocket.recv()
            print("< {}".format(response))


def start_server(port=5678):
    loop = asyncio.get_event_loop()
    response = requests.post('http://localhost:5000/state', json={'simulationStatus': 'running'})
    print(response.json())
    loop.run_until_complete(run_commnad(port))
    time.sleep(3)
    loop.run_until_complete(run_commnad(port))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        start_server(sys.argv[1])
    else:
        start_server()


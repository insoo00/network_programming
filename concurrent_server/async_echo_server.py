import asyncio
from socket import *

PORT = 2500
BUFSIZE = 1024

async def handler(conn, addr):
    while True:
        data = await asyncio.to_thread(conn.recv, BUFSIZE)
        if not data:
            break
        print(f'{addr} Received message: ', data.decode())
        conn.send(data)

async def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', PORT))
    sock.listen(5)

    while True:
        client, addr = await asyncio.to_thread(sock.accept)
        print(addr, 'accepted')
        await asyncio.create_task(handler(client, addr))

asyncio.run(main())


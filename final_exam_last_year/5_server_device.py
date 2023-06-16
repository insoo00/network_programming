import asyncio
import random

async def handle_asyncclient(reader, writer): 
    print('client :', writer.get_extra_info('peername')) 
    while True:
        data = await reader.read(8)
        if data == b'1':
            temp = random.randint(0, 40)
            res = 'Temp='+str(temp)
            writer.write(res.encode())
            await writer.drain()
        elif data == b'2':
            hum = random.randint(0, 100)
            res = 'Humid='+str(hum)
            writer.write(res.encode())
            await writer.drain()
        elif len(data) == 0:
            break
        else:
            res = 'Invalid messages'
            writer.write(res.encode())
            await writer.drain()
    writer.close()
    await writer.wait_closed()
    print('connection was closed')

async def server_asyncmain():
    server = await asyncio.start_server(handle_asyncclient,'localhost',9999) 
    print('server started')
    await server.serve_forever()
    
if __name__ == "__main__":
    asyncio.run(server_asyncmain())
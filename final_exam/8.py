import asyncio
import time

socks = [] # 소켓 리스트 -> writer 리스트

BUF_SIZE = 1024

async def handle_asyncclient(reader, writer): 
    socks.append(writer)
    while True:
        data = await reader.read(BUF_SIZE)
        print(data)
        if len(data) == 0:
            break
        elif 'quit' in data.decode():
            socks.remove(writer)
            continue
        else:
            print(time.asctime() + str(writer) + ':' + data.decode())
            for writer_in_socks in socks:
                if writer_in_socks != writer:
                    writer_in_socks.write(data.encode())
                    await writer_in_socks.drain()
    writer.close()
    await writer.wait_closed()
    print('connection was closed')

async def server_asyncmain():
    server = await asyncio.start_server(handle_asyncclient,'localhost',3000) 
    print('server started')
    await server.serve_forever()
    
if __name__ == "__main__":
    asyncio.run(server_asyncmain())

import asyncio

async def tcp_echo_client(message):
    try:
        reader, writer = await asyncio.open_connection(
            '127.0.0.1', 10000)

        print(f'Send: {message!r}')
        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')

        print('Close the connection')
        writer.close()
        await writer.wait_closed()
    except ConnectionRefusedError as e:
        print('something is wrong')
        print(str(e))

asyncio.run(tcp_echo_client('Hello World!'))
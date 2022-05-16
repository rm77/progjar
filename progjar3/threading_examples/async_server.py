import asyncio
async def handle_client(reader, writer):

    data = (await reader.read(1024))

    writer.write(data)
    writer.close()


loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(handle_client, 'localhost', 8001))
loop.run_forever()
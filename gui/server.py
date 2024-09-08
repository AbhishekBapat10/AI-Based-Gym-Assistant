import websockets
import asyncio

connected_clients = set()
# Creating WebSocket server
async def ws_server(websocket):
 connected_clients.add(websocket)
 print("WebSocket: Server Started.")
 try:
  while True:
   # Receiving values from client
   name = await websocket.recv()
   
   for client in connected_clients:
    if client != websocket:
     await client.send(name)
   if "sleep".lower() in name.lower():
    break
 except websockets.ConnectionClosed:
  print(f"Client {websocket} disconnected.")
  connected_clients.remove(websocket)


async def main():
 async with websockets.serve(ws_server, "localhost", 8765):
  await asyncio.Future()  # run forever


if __name__ == "__main__":
 asyncio.run(main())
    
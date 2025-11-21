import asyncio
import json
import websockets



async def send_message(a: int, b: int) -> int:
    """
    This function connects to the server, 
    sends messages to the server and receives 
    a response back.
    """
    
    async with websockets.connect("ws://localhost:8000") as websc:
        await websc.send(json.dumps({"a": a, "b": b}))
        response = json.loads(await websc.recv())

        if "error" in response:
            raise ValueError(response["error"])

        return response["result"]


async def check():
    """
    This function declares an array of pairs,
    unpacks and sends each as message to the server
    and prints the result.
    """

    print("Calling server...\n")

    tests = [(5, 5), (3, 4), (7, 8)]

    for a, b in tests:
        result = await send_message(a, b)
        print(f"{a}*{b} = {result}")


if __name__ == "__main__":
    asyncio.run(check())

import asyncio
import json
import websockets


# Sending messages to server and waititng for response
async def send_message(a: int, b: int) -> int:
    async with websockets.connect("ws://localhost:8000") as websc:
        await websc.send(json.dumps({"a": a, "b": b}))
        response = json.loads(await websc.recv())

        if "error" in response:
            raise ValueError(response["error"])

        return response["result"]

# Sending each of the pairs to server, getting the result and printing
async def check():
    print("Calling server...\n")

    tests = [(5, 5), (3, 4), (7, 8)]

    for a, b in tests:
        result = await send_message(a, b)
        print(f"{a}*{b} = {result}")


if __name__ == "__main__":
    asyncio.run(check())

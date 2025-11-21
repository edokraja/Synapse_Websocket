import asyncio
import json
import websockets


# function to multiply 2 numbers
def multiply(a: int, b: int):
    """
    Multiplies two integers and returns result.
    """
    result = a*b 
    return result




async def get_client_message(websocket):

    """
    This function listens each message, unpacks it,
    checks if it is a valid type, calculates a result
    and sends it back to the client.
    """


    async for message in websocket:

        # try except for error handling
        try:
            data = json.loads(message)

            a = data.get("a")
            b = data.get("b")

            # input should be valid
            if not isinstance(a, int) or not isinstance(b, int):
                await websocket.send(json.dumps({"error": "Invalid inputs"}))
                continue

            result = multiply(a, b)

            await websocket.send(json.dumps({"result": result}))

        except json.JSONDecodeError:
            await websocket.send(json.dumps({"error": "Malformed JSON"}))



async def main():
    """
    This function starts the websocket server
    and keeps it running forever.
    """


    async with websockets.serve(get_client_message, "localhost", 8000):
        print("Server running on ws://localhost:8000")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())

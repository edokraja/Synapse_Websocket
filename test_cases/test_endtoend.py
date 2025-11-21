import asyncio
import pytest
from synapse_ws.websocket_client import send_message
from synapse_ws.websocket_server import main


@pytest.fixture(scope="module", autouse=True)
def start_server():
    # create a loop to not block the server and let the test run
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)

    # initiate server
    server_start = new_loop.create_task(main())
    yield #here the tests will run
    server_start.cancel()


# actual test
@pytest.mark.asyncio
async def test_client_to_server():
    result = await send_message(6, 5)
    assert result == 30
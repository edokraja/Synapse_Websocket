import asyncio
import pytest
from synapse_ws.websocket_client import send_message
from synapse_ws.websocket_server import main


@pytest.fixture(scope="module", autouse=True)
def start_server():
    """
    Function to start the server for the whole module and
    before every test case, run the tests while server is running
    and then stop.
    """
    # create a loop to not block the server and let the test run
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)

    # initiate server
    server_start = new_loop.create_task(main())
    yield #here the tests will run
    server_start.cancel()


@pytest.mark.asyncio
async def test_client_to_server():
    """
    This function is the actual test case that will be executed.
    It will check if the client-server communication is working
    by sending a message and checking the response.
    """
    result = await send_message(6, 5)
    assert result == 30
from synapse_ws.websocket_server import multiply


def test_cases():
    assert multiply(2, 3) == 6
    assert multiply(-2, 5) == -10
    assert multiply(0, 1) == 0
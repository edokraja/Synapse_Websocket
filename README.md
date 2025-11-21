# Synapse_Websocket

This project demonstrates a simple asynchronous Websocket server.

## Setup
1. **Clone the repository**
In the terminal run:
git clone https://github.com/yourusername/Synapse_Websocket.git
cd Synapse_Websocket

2. **Create a virtual environment (optional)**
python -m venv venv
venv\Scripts\activate.bat

3. **Install required dependencies**
pip install -r requirements.txt

4. **Run the server**
python synapse_ws/server.py

5. **Open a new terminal in the same directory and run the client**
python synapse_ws/client.py


## Example Output
Request 1: "a":5, "b":5, Response from server: {"result": 25} 
Request 2: "a":3, "b":4, Response from server: {"result": 12} 
Request 3: "a":7, "b":8, Response from server: {"result": 56}

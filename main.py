import request
import logic

while True:
    # myCommand(request.py) passes voice recognized request to strutcture(logic.py)
    logic.structure(request.myCommand())

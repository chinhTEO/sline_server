import json
class message:
    def __init__(self):
    def genStatus(self,status,message):
        status = {
            'status': status,
            'message': message
        }

    return json.dumps(status)


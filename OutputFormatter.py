import json
class OutputFormatter:
    def __init__(self):
        None
    def formatOutput(self,inputDict):
        json_object = json.dumps(inputDict) 
        return json_object

import subprocess
def printToConsole(jsonString):    
    subprocess.run(['python', 'ReceiverMain.py'], input=jsonString)
    print(jsonString)
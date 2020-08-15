import serial
from serial.tools import list_ports
def getArduinoPort():
    portLists = list_ports.comports()
    for port in portLists:
        port = str(port)
        if 'Arduino' in port:
            print(port)
            return port.split(' ')[0]
    raise Exception("Port not exists")

def getRfidCardNumber():
    port = getArduinoPort()
    arduinoSerial = serial.Serial(port, 115200, timeout=10)
    arduinoSerial = checkPortIsOpend(arduinoSerial)
    keepSeeking = True
    cardNumber = ''
    while keepSeeking:
        print("wating tag")
        cardNumber, keepSeeking = readRfidCard(arduinoSerial)
        print(cardNumber)
    print(arduinoSerial)
    print("exit")
    arduinoSerial.close()
    return cardNumber, arduinoSerial
def checkPortIsOpend(arduinoSerial):
    if not arduinoSerial.isOpen():
        return arduinoSerial.open()
    return arduinoSerial

def getCardNumberIfDetected(rfidInfo):
    if rfidInfo != "b''":
        cardNumber = rfidInfo.split(' ')[1]
        cardNumber += rfidInfo.split(' ')[2]
        keepSeeking = False
        return cardNumber, keepSeeking
    cardNumber = '0'
    keepSeeking = True
    return cardNumber, keepSeeking

def readRfidCard(arduinoSerial):
    if arduinoSerial.readable():
        rfidInfo = str(arduinoSerial.readline())
        cardNumber, keepSeeking = getCardNumberIfDetected(rfidInfo)
        return cardNumber, keepSeeking

def stopReadRfidCard():
    port = getArduinoPort()
    arduinoSerial = serial.Serial()
    arduinoSerial.port = port
    print(arduinoSerial)
    arduinoSerial = checkPortIsOpend(arduinoSerial)
    arduinoSerial.flush()
    arduinoSerial.close()
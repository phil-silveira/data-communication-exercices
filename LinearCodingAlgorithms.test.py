import LinearCodingAlgorithms as code 

def testNRZ():
    print('* testing algorithm NRZ \t- '),
    print('input: "' + message + '" \t- '),

    encodedMessage = code.encodeNRZ(message)
    decodedMessage = code.decodeNRZ(encodedMessage)

    print('SUCESS' if message == decodedMessage else 'FAIL')

def testNRZ_L():
    print('* testing algorithm NRZ_L \t- '),
    print('input: "' + message + '" \t- '),

    encodedMessage = code.encodeNRZ_L(message)
    decodedMessage = code.decodeNRZ_L(encodedMessage)

    print('SUCESS' if message == decodedMessage else 'FAIL')

def testNRZ_I():
    print('* testing algorithm NRZ_I \t- '),
    print('input: "' + message + '" \t- '),

    encodedMessage = code.encodeNRZ_I(message)
    decodedMessage = code.decodeNRZ_I(encodedMessage)

    print('SUCESS' if message == decodedMessage else 'FAIL')

def testAMI():
    print('* testing algorithm AMI \t- '),
    print('input: "' + message + '" \t- '),

    encodedMessage = code.encodeAMI(message)
    decodedMessage = code.decodeAMI(encodedMessage)

    print('SUCESS' if message == decodedMessage else 'FAIL')

def test2B1Q():
    print('* testing algorithm 2B1Q \t- '),
    print('input: "' + message + '" \t- '),

    encodedMessage = code.encode2B1Q(message)
    decodedMessage = code.decode2B1Q(encodedMessage)

    print('SUCESS' if message == decodedMessage else 'FAIL')

def testMLT_3():
    print('* testing algorithm MLT_3 \t- '),
    print('input: "' + message + '" \t- '),

    encodedMessage = code.encodeMLT_3(message)
    decodedMessage = code.decodeMLT_3(encodedMessage)

    print('SUCESS' if message == decodedMessage else 'FAIL')

# Testing linear code algorithms

message = 'UERGS'

testNRZ()
testNRZ_L()
testNRZ_I()
testAMI()
test2B1Q()
testMLT_3()

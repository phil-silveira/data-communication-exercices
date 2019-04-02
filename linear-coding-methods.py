import numpy as np

# str2bin: convert a string to a bit stream
#
# description:
#   a char is represented by a byte, using ascii's representation.
#   each char is converted to a byte in a bit array
#
def str2bin(message):
    bitStream = []
    for x in message:
        bitStream.extend(list(format(ord(x),'08b')))
    return  bitStream

# bin2str: convert a bit stream to a string
#
# description:
#   the bit stream content is grouped in bytes
#   after these bytes are encoded to chars in
#   a single string
#
def bin2str(bitStream):
    message = ''
    for b in range(0, len(bitStream) -1, 8):
        message += chr(int(''.join(map(str, bitStream[b:b+8])), 2))
    return message

# encodeNRZ: bit stream when bit = 1 convert
# to HIGH and when bit = 0 keeps 0
#
def encodeNRZ(message, HIGH=1):
    return [int(x) * HIGH for x in str2bin(message)]

# decodeNRZ: bit stream when bit = HIGH convert
# to 1 and when bit = 0 keeps 0 after build the 
# string
# 
def decodeNRZ(bitStream, HIGH=1):
    return bin2str([int(x / HIGH) for x in bitStream])

# encodeNRZ_L: bit stream when bit = 1 convert
# to LOW and when bit = 0 convert to HIGH
#
def encodeNRZ_L(message, HIGH=1, LOW=-1):
    return [ HIGH if x == '0' else LOW for x in str2bin(message)]

# decodeNRZ_L: bit stream when bit = LOW convert
# to 1 and when bit = HIGH convert to 0 after 
# build the string
# 
def decodeNRZ_L(bitStream, HIGH=1, LOW=-1):
    return bin2str([ '0' if x == HIGH else '1' for x in bitStream])

# encodeNRZ_I: bit stream when bit = 1 the 
# output is toggled and when bit = 0 output
# is keeped
#
def encodeNRZ_I(message, HIGH=1, LOW=-1):
    bitStream = encodeNRZ_L(message, HIGH=HIGH, LOW=LOW)
    encodedBitStream = []
    encodedBitStream.append(bitStream[0])

    for i in range(1, len(bitStream)):
        encodedBitStream.append((LOW if encodedBitStream[i-1] == HIGH else HIGH) if bitStream[i] == LOW else encodedBitStream[i-1])

    return encodedBitStream


# decodeNRZ_I: bit stream when bit toggle the 
# output is 1 and when bit keeps output
# is 0. after string is builded
#
def decodeNRZ_I(encodedBitStream, HIGH=1, LOW=-1):
    bitStream = []
    bitStream.append(encodedBitStream[0])
    
    for i in range(1, len(encodedBitStream)):
        bitStream.append(HIGH if encodedBitStream[i-1] == encodedBitStream[i] else LOW)

    return decodeNRZ_L(bitStream, HIGH=HIGH, LOW=LOW)

# encodeAMI: encode a bit stream that 
# when bit = 0 it's keep 0 but when bit = 1
# it's toggle between a positive and a negative
# HIGH value 
# 
def encodeAMI(message, HIGH=1):
    bitStream = encodeNRZ(message, HIGH=HIGH)
    lastOne = -1
    for i in range(len(bitStream)):
        if bitStream[i] == HIGH:
            lastOne *= -1
            bitStream[i] *= lastOne 

    return bitStream

# decodeAMI: decode a bit stream that 
# when bit = 0 it's keep 0 but when bit = HIGH
# or - HIGH it's 1. after build a string with this
# bit stream
#
def decodeAMI(bitStream, HIGH=1):
    for i in range(len(bitStream)):
        bitStream[i] = abs(bitStream[i]) 

    return decodeNRZ(bitStream, HIGH=HIGH)




message = 'UERGS'

print(encodeAMI(message))
print(decodeAMI(encodeAMI(message)))
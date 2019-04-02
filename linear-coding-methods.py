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

# encode2B1Q: the message is encoded to a bitstream, after,
# all data are encoded according a logic that transform 
# each couple of bits is a code according this system:
# when 10 => HIGH2, 11 => HIGH1, 01 => LOW1, 00 => LOW2,
# 
def encode2B1Q(message, HIGH1=1, HIGH2=2, LOW1=-1, LOW2=-2):
    bitStream = str2bin(message)

    encodedBitStream = []
    for i in range(0, len(bitStream),2):
        if bitStream[i:i+2] == ['1','0']:
            encodedBitStream.append(HIGH2)
        elif bitStream[i:i+2] == ['1','1']:
            encodedBitStream.append(HIGH1)
        elif bitStream[i:i+2] == ['0','1']:
            encodedBitStream.append(LOW1)
        elif bitStream[i:i+2] == ['0','0']:
            encodedBitStream.append(LOW2)

    return  encodedBitStream

# decode2B1Q: the message is decoded from a bitstream
# encoded following this system:
# when 10 => HIGH2, 11 => HIGH1, 01 => LOW1, 00 => LOW2,
# after this bitStream is decoded to the origina message
# 
def decode2B1Q(encodedBitStream, HIGH1=1, HIGH2=2, LOW1=-1, LOW2=-2):
    bitStream = []
    for x in encodedBitStream:
        if   x == HIGH2:
            bitStream.extend(['1','0'])
        elif x == HIGH1:
            bitStream.extend(['1','1'])
        elif x == LOW1:
            bitStream.extend(['0','1'])
        elif x == LOW2:
            bitStream.extend(['0','0'])
    
    message = bin2str(bitStream)
    return message

# encodeMLT_3: code message following a
# logic that encode bitstream. if input bit
# is 0, keeps the previus output value and 
# if input bit is 1, output change according this logic: 
# 0 => HIGH, HIGH => 0, 0 => LOW, LOW => 0
# we can think this. like a circular queue that contains
# values [0, HIGH, 0, LOW]
#
def encodeMLT_3(message, HIGH=1, LOW=-1):
    bitStream = str2bin(message)
    states = [0, HIGH, 0, LOW]
    stateCounter = 0
    
    encodedBitStream = []
    for x in bitStream:
        if x == '1':
            stateCounter += 1

        encodedBitStream.append(states[stateCounter % len(states)])

    return encodedBitStream

# decodeMLT_3: decode a bitstream following
# this logic: if bit
# is 0, keeps the previus output value and 
# if input bit is 1, output change according this logic: 
# 0 => HIGH, HIGH => 0, 0 => LOW, LOW => 0
# we can think this. like a circular queue that contains
# values [0, HIGH, 0, LOW]
#
def decodeMLT_3(encodedBitStream, HIGH=1, LOW=-1):
    bitStream = []
    bitStream.append(encodedBitStream[0])

    for i in range(1, len(encodedBitStream)):
        if encodedBitStream[i-1] != encodedBitStream[i]:
            bitStream.append('1')
        else:  
            bitStream.append('0')

    message = bin2str(bitStream)
    return message


# testing algorithms

message = 'UERGS'
print(message)
print(decodeNRZ(encodeNRZ(message)))
print(decodeNRZ_L(encodeNRZ_L(message)))
print(decodeNRZ_I(encodeNRZ_I(message)))
print(decodeAMI(encodeAMI(message)))
print(decode2B1Q(encode2B1Q(message)))
print(decodeMLT_3(encodeMLT_3(message)))


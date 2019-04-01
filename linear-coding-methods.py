# str2bin: convert a string to a bit stream
#
# description:
#   a char is represented by a byte, using ascii's representation.
#   each char is converted to a byte and after all char is joined 
#   in a single bit stream
#
def str2bin(message):
    bitStream = ''
    for x in list(map(lambda x: format(ord(x),'08b'), message)):
        bitStream += x

    return  bitStream

# bin2str: convert a bit stream to a string
#
# description:
#   the bitstream content is splited in bytes
#   after these bytes are encoded to chars and
#   these char are join in a single string
#
def bin2str(bitStream):
    message = []
    for b in range(0, len(bitStream) -1, 8):
        message.append(chr(int(bitStream[b:b+8], 2)))

    return ''.join(message)


def encodeNRZ(message, HIGH=1):
    return str2bin(message).replace('1', str(HIGH))
    

def decodeNRZ(message, HIGH=1):
    return bin2str(message.replace(str(HIGH),'1'))


message = 'UERGS'

bitStream = encodeNRZ(message, HIGH=5)

print(bitStream)
print(decodeNRZ(bitStream, HIGH=5))
from struct import unpack, pack

def unpackByte(char):
    return unpack('B', char)[0]


def packByte(code):
    return pack('B', code)
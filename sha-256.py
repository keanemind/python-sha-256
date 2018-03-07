"""This Python module is an implementation of the SHA-256 algorithm."""

def generate_hash(message: str):
    """Return a SHA-256 hash from the message passed.
    The argument should be a string of 0s and 1s that
    are the binary form of the message."""

    # Padding
    length = len(message)
    message += "1"
    while (len(message) + 64) % 512 != 0:
        message += "0"

    length_str = format(length, 'b')
    while len(length_str) < 64:
        length_str = '0' + length_str

    message += length_str

    assert len(message) % 512 == 0, "Padding did not complete properly!"

    # Parsing
    split = [] # contains 512-bit chunks of message
    for i in range(0, len(message), 512):
        split.append(message[i:i+512])

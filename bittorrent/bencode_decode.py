import unittest
import io


class TestCases(unittest.TestCase):

    def test_decode_int(self):
        good_test_cases = [
            (b'i123244e', 123244),
            (b'i67e', 67),
            (b'i0e', 0),
            (b'i-1e', -1)
        ]
        for (input, output) in good_test_cases:
            self.assertEqual(decode_int(io.BytesIO(input)), output)

        bad_test_cases = [
            b'',
            b'i',
            b'1',
            b'i123a',
            b'i-0e',
            b'i04',
        ]
        for input in bad_test_cases:
            with self.assertRaises(DecodeError):
                decode_int(io.BytesIO(input))


class DecodeError(Exception):

    def __init__(self, error_message):
        self.error = error_message


def decode_int(reader):
    buff = []
    if reader.read(1) != b'i':
        raise DecodeError('expected an i')
    while True:
        byte = reader.read(1)
        if byte >= b'0' and byte <= b'9':
            buff.append(byte)
        elif byte != b'e':
            raise DecodeError('expected and e')
        else:
            break
    return int(b''.join(buff))


if __name__ == '__main__':
    unittest.main()

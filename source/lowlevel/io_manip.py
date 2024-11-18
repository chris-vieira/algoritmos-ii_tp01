
BYTE_SIZE = 8
BYTE_MASK = 0xFF

class BitReader:
    def __init__(self,
                 in_file_path: str,
                 bits_per_read: int = BYTE_SIZE,
                 buffer_size: int = None):

        super().__init__()

        if buffer_size is not None:
            self._file = open(in_file_path, "rb", buffering=buffer_size)
        else:
            self._file = open(in_file_path, "rb")

        self._bits_per_read = bits_per_read
        self._read_bit_count = 0
        self._unaligned_rest = 0
        self._eof = False

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self._eof:
            raise StopIteration

        v = self._unaligned_rest

        while self._read_bit_count < self._bits_per_read:
            B = self._file.read(1)
            if B:
                v = B[0] | (v << BYTE_SIZE)
                self._read_bit_count += BYTE_SIZE

            else:
                self._eof = True
                return self._unaligned_rest

        self._read_bit_count -= self._bits_per_read
        self._unaligned_rest = v & (BYTE_MASK >> (BYTE_SIZE - self._read_bit_count))

        v = v >> self._read_bit_count
        return v

    def read(self, bits_per_read: int = None) -> int:
        if bits_per_read is not None:
            self._bits_per_read = bits_per_read
        return self.__next__()

    def set_bits_per_read(self, bits_per_read: int):
        self._bits_per_read = bits_per_read

    def close(self):
        self._file.close()


class BitWriter():
    def __init__(self, out_file_path: str, buffer_size : int = None):
        super().__init__()

        if buffer_size is not None:
            self._file = open(out_file_path, "wb", buffering=buffer_size)
        else:
            self._file = open(out_file_path, "wb")

        self._unalignment = 0
        self._unaligned_rest = 0
        self._B = bytearray(1)

    def write(self, value: int, bits_per_write: int):
        shift = bits_per_write - (BYTE_SIZE - self._unalignment)
        while shift >= 0:
            self._B[0] = (value >> shift) \
                         & (BYTE_MASK >> self._unalignment) \
                         | self._unaligned_rest

            self._file.write(self._B)
            shift -= BYTE_SIZE
            self._unalignment = 0
            self._unaligned_rest = 0

        self._unalignment = shift + BYTE_SIZE
        self._unaligned_rest = (value << (BYTE_SIZE - self._unalignment)) \
            & BYTE_MASK | self._unaligned_rest

    def close(self):
        self._unalignment = 0
        self.write(self._unaligned_rest, BYTE_SIZE)
        self._file.close()


from typing import List

class ByteReader:
    def __init__(self, in_file_path: str, buffer_size: int = None):
        # TODO: Must be read a chunck of data, instead of all the file at once!
        if buffer_size is not None:
            self._file = open(in_file_path, "rb", buffering=buffer_size)
        else:
            self._file = open(in_file_path, "rb")

    def __iter__(self):
        return self

    def __next__(self) -> int:
        c = self._file.read(1)
        if c:
            return c[0]
        raise StopIteration

    def close(self):
        self._file.close()


class ByteWriter:

    def __init__(self, out_file_path: str, buffer_size: int = None):
        if buffer_size is not None:
            self._file = open(out_file_path, "wb", buffering=buffer_size)
        else:
            self._file = open(out_file_path, "wb")

    def write(self, values: List[int]):
        self._file.write(bytearray(values))

    def close(self):
        self._file.close()

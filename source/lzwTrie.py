import os
from typing import List
from typing import Union

from lowlevel.io_manip import BitReader, BitWriter, ByteReader, ByteWriter
from trie.trieCompacta import TrieCompacta

class LZW:
    def __init__(self, max_sz_in_bits = 12):
        super().__init__()
        self._in_file = None
        self._out_file = None
        self._root_mark = -1
        self._init_alphabet_size = 2**8
        self._stream_end_mark = self._init_alphabet_size
        self._max_sz_in_bits = max_sz_in_bits

    def _get_init_alphabet_size(self):
        return self._init_alphabet_size
    
    def _get_root_mark(self):
        return self._root_mark
    
    def _get_stream_end_mark(self):
        return self._stream_end_mark
    
    def _get_max_sz_in_bits(self):
        return self._max_sz_in_bits
    
    def compress(self, in_file_path: str, out_file_path: str) -> bool:
        if not os.path.exists(in_file_path):
            return False

        self._init_compress()
        self._in_file = ByteReader(in_file_path)
        self._out_file = BitWriter(out_file_path)

        seq_parent = self._get_root_mark()
        for c in self._in_file:
            seq = self._get_sequence(seq_parent, c)
            if seq is not None:
                seq_parent = seq
            else:
                self._write_sequence(seq_parent)
                self._insert_next_sequence(seq_parent, c)
                seq_parent = self._get_sequence(self._get_root_mark(), c)

        self._write_sequence(seq_parent)
        self._write_sequence(self._get_stream_end_mark())

        self._in_file.close()
        self._out_file.close()
        return True

    def _init_compress(self):
        self._container = TrieCompacta()
        self._next_sequence_number = 0
        self._current_sequence_bit_count = 0

        for i in range(self._get_init_alphabet_size()):
            self._insert_next_sequence(self._get_root_mark(), i)

        self._insert_next_sequence(self._get_root_mark(), self._get_stream_end_mark())

    def _insert_next_sequence(self, parent_seq: int, edge: int):
        self._container[(parent_seq, edge)] = self._next_sequence_number
        self._current_sequence_bit_count += \
            (self._next_sequence_number >> self._current_sequence_bit_count)
        self._next_sequence_number += 1

    def _get_sequence(self, parent_seq: int, edge: int) -> Union[int, None]:
        return self._container.get((parent_seq, edge), None)

    def _write_sequence(self, seq: int):
        self._out_file.write(seq, self._current_sequence_bit_count)

    def decompress(self, in_file_path: str, out_file_path: str) -> bool:
        if not os.path.exists(in_file_path):
            return False

        self._init_decompress()

        self._in_file = BitReader(in_file_path)
        self._out_file = ByteWriter(out_file_path)

        seq_parent = self._in_file.read(self._current_sequence_bit_count)
        seq_parent_path = self._get_sequence_path(seq_parent)

        self._out_file.write(seq_parent_path)

        seq_path = seq_parent_path
        seq_path_first = seq_parent_path[0]

        for seq in self._in_file:
            if seq == self._get_stream_end_mark():
                break

            is_normal_case = seq < self._next_sequence_number

            if is_normal_case:
                seq_path = self._get_sequence_path(seq)
                seq_path_first = seq_path[0]

            new_seq_path = seq_parent_path + [seq_path_first]

            self._insert_next_sequence_path(new_seq_path)

            if is_normal_case:
                seq_out_path = seq_path
            else:
                seq_out_path = new_seq_path

            self._out_file.write(seq_out_path)
            seq_parent_path = seq_out_path
            self._in_file.set_bits_per_read(self._current_sequence_bit_count)

        self._in_file.close()
        self._out_file.close()
        return True

    def _init_decompress(self):
        self._sequence_table = TrieCompacta()
        self._next_sequence_number = 0
        self._current_sequence_bit_count = 0

        for i in range(self._get_init_alphabet_size()):
            self._insert_next_sequence_path([i])

        self._insert_next_sequence_path([self._get_stream_end_mark()])

    def _insert_next_sequence_path(self, seq_path: List[int]):
        self._sequence_table[self._next_sequence_number] = seq_path

        self._next_sequence_number += 1
        self._current_sequence_bit_count += \
            (self._next_sequence_number >> self._current_sequence_bit_count)

    def _get_sequence_path(self, seq: int) -> List[int]:
        return self._sequence_table[seq]

import os
import sys
import argparse

from lzwTrie import LZW

def file_permission_mask(file: str) -> int:
    return permission_mask(os.stat(file))

def permission_mask(st_result: os.stat_result) -> int:
    return st_result.st_mode & 0o7777

def generate_default_output(input_file, operation):
    base, ext = os.path.splitext(input_file)
    if operation == "compress":
        return f"{base}.lzw"
    elif operation == "decompress":
        return f"{base}_decompressed{ext}"
    return f"{base}_output{ext}"

def compress_file(file_inp, file_out, max_dict_size, verbose):
    if verbose:
        print(f"Compressing file: {file_inp} to {file_out} with max dictionary size: {max_dict_size} entries.")

    if not os.path.exists(file_inp):
        print(f"Error: Input file '{file_inp}' does not exist.", file=sys.stderr)
        sys.exit(1)

    file_stat = os.stat(file_inp)
    uncompressed_size = file_stat.st_size
    perm_mask = permission_mask(file_stat)
    print(f"Going to compress file '", file_inp, "' of size = ", uncompressed_size, "B")
    print(file_inp, file_out)
    LZW(max_dict_size).compress(file_inp, file_out)
    compressed_size = os.path.getsize(file_out)
    if compressed_size < uncompressed_size:
        if compressed_size < uncompressed_size:
            print("--> OK! Compressed file size is lower than the original size")
        else:
            print("Keeping the file even if the size is higher "
                        "than the original size due force flag (-f)")

        os.chmod(file_out, perm_mask)
    else:
        print("--> OPS! Compressed file size is not lower than the original size, "
                    "removing it and keeping the old one")
        os.remove(file_out)

    print(f"File '{file_inp}' compressed successfully to '{file_out}'.")

def decompress_file(file_inp, file_out, max_dict_size, verbose):
    if verbose:
        print(f"Decompressing file: {file_inp} to {file_out} with max dictionary size: {max_dict_size} entries.")

    if not os.path.exists(file_inp):
        print(f"Error: Input file '{file_inp}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if file_inp.endswith('lzw'):
        file_out = file_inp[:(len(file_inp) - len('lzw'))]
        in_place = False
    else:
        print("File '", file_inp, "' doesn't end with ",
                    'lzw',"; skipping it")
        print("'", file_inp, "' skipped")
        sys.exit(1)

    LZW(max_dict_size).decompress(file_inp, file_out)
    print("Decompression finished...")

    perm_mask = file_permission_mask(file_inp)
    os.chmod(file_out, perm_mask)        
    print(f"File '{file_inp}' decompressed successfully to '{file_out}'.")

def main():
    parser = argparse.ArgumentParser(
        description="A simple LZW compression/decompression tool.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument(
        "-c", "--compress", 
        metavar="FILE_PATH", 
        help="Enable compression mode and specify the file to compress."
    )
    parser.add_argument(
        "-d", "--decompress", 
        metavar="FILE_PATH", 
        help="Enable decompression mode and specify the file to decompress."
    )
    parser.add_argument(
        "-o", "--output", 
        metavar="OUTPUT_FILE", 
        help="Specify the output file path. If not provided, a default name will be used."
    )
    parser.add_argument(
        "-v", "--verbose", 
        action="store_true", 
        help="Enable verbose output."
    )
    parser.add_argument(
        "--max-dict-size", 
        type=int, 
        default=12, 
        help="Set the maximum dictionary size (in bits)."
    )
    
    args = parser.parse_args()
    
    if args.compress and args.decompress:
        print("Error: You cannot specify both compression and decompression modes.")
        return
    
    if args.compress:
        input_file = args.compress
        if not os.path.isfile(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
            return
        output_file = args.output if args.output else generate_default_output(input_file, "compress")
        compress_file(input_file, output_file, args.max_dict_size, args.verbose)
    
    elif args.decompress:
        input_file = args.decompress
        if not os.path.isfile(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
            return
        output_file = args.output if args.output else generate_default_output(input_file, "decompress")
        decompress_file(input_file, output_file, args.max_dict_size, args.verbose)
    
    else:
        print("Error: You must specify either -c (compress) or -d (decompress) with a file path.")
        parser.print_help()


if __name__ == '__main__':
    main()

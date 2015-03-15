#!/usr/bin/env python3

import binascii
import os
import argparse


def xor(a, b):
    """Return the XOR of two byte sequences. The length of the result is the length of the shortest."""

    return bytes(x ^ y for (x, y) in zip(a, b))


def encrypt_with_random_pad(input_filename, output_filename):
    try:
        with open(input_filename) as f:
            cleartexts = f.read().splitlines()
    except Exception as e:
        raise Exception("Cannot read {}, error={}".format(input_filename, e))
    pad = os.urandom(max(len(m) for m in cleartexts))
    ciphertexts = [binascii.hexlify(xor(pad, m.encode('ascii'))).decode('ascii') for m in cleartexts]
    try:
        with open(output_filename, "w") as f:
            for c in ciphertexts:
                print(c, file=f)
    except Exception as e:
        raise Exception("Cannot write {}, error={}".format(output_filename, e))
    return pad


def main():
    parser = argparse.ArgumentParser(description="Generate ciphertexts")
    parser.add_argument("--input_filename", type=str,
                        help="Name of the file containing the cleartexts (default: cleartexts.txt)",
                        default="cleartexts.txt")
    parser.add_argument("--output_filename", type=str,
                        help="Name of the destination file for the ciphertexts (default: ciphertexts.txt)",
                        default="ciphertexts.txt")
    parser.add_argument("--debug", action='store_true', help="Output the pad on the standard-output")
    args = parser.parse_args()
    try:
        if args.debug:
            print("Encrypting {} into {}".format(args.input_filename, args.output_filename))
        pad = encrypt_with_random_pad(args.input_filename, args.output_filename)
        if args.debug:
            print("pad=", binascii.hexlify(pad).decode('ascii'), sep="")
            print("len=", len(pad)*8, "bit")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()


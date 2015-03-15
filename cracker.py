#!/usr/bin/env python3

import binascii
import argparse

SPACE = ord(' ')

def countalphas( char, position, ciphertexts ):
    count = 0
    for ciphertext in ciphertexts: 
        if len(ciphertext) > position:
            if chr(ciphertext[position]^char).isalpha(): count+=1
    return count

def main():
    parser = argparse.ArgumentParser(description="Many-time Pad Cracker")
    parser.add_argument("--filename", type=str,
                        help="Name of the file containing the ciphertexts (default: ciphertexts.txt)",
                        default="ciphertexts.txt")
    args = parser.parse_args()
    try:
        with open(args.filename) as f:
            ciphertexts = [binascii.unhexlify(line.rstrip()) for line in f]
            # Cyphertexts puliti (tolgo i vuoti), anche se non è necessario
            # ciphertexts = [c for c in ciphertexts if c]
        cleartexts = [bytearray(b'?' * len(c)) for c in ciphertexts]
    except Exception as e:
        print("Cannot crack {} --- {}".format(args.filename, e))
        raise SystemExit(-1)

    
    # 'a'.isalpha() => true
    # '!'.isalpha() => false
    # ord('z') => 122

    # Prendo il massimo valore di lunghezza, poi itero sulle colonne.
    # Faccio l'XOR solo di ciphertexts con lunghezza adeguata
    for col in range(max([len(x) for x in ciphertexts])):
        for c1 in ciphertexts:
            for c2 in ciphertexts:
                if (len(c1) > col) and (len(c2) > col):
                    if chr(c1[col]^c2[col]).isalpha(): 
                        # Controllo a quale corrispondono più lettere negli altri ciphertext.
                        # Assumo che quello col numero più alto sia quello con lo spazio
                        #
                        # Lo spazio è in c1, quindi c2 ha il carattere, ma invertito
                        # Cerco di ottenere il PAD per quella lettera
                        for k, c in enumerate(ciphertexts):
                            if len(c) > col:
                                if countalphas(c1[col], col, ciphertexts) >= countalphas(c2[col], col, ciphertexts):
                                    cleartexts[k][col] = c1[col]^0b100000^c[col]
                                else:
                                    cleartexts[k][col] = c2[col]^0b100000^c[col]
                                        
                        break

    for line in cleartexts:
        print(line)
    

if __name__ == "__main__":
    main()

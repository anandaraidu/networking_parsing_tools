import random
import binascii
import unittest 

def generate_fill_conent_random_bytes(n,st, en):
    fill = bytes([(random.randint(st,en)) for i in range(n)])
    #print(f"Fill: {fill}")
    return fill

def bytes_2_hex_representation( bites ):
    return binascii.hexlify( bites )

def hex_representation_2_bytes_string( bites ):
    return binascii.unhexlify( bites )

def list_2_bytes( l ):
    return bytes(l)

def list_to_string( l ):
    return ''.join(l)

def bytes_2_list( bites ):
    return list( bites )

def file_to_bytes( fname ):
    with open(fname, 'rb') as f:
        return f.read()

def bytes_to_file( buff,  fname):
    with open(fname, 'wb') as f:
        f.write(buff)

"""
this doesnt look good, this function implementation have to improve
"""
def decimal_to_hex_bytes(v):
    s = '{:x}'.format(v)
    if len(s) % 2 == 1:
        s = '0' + s
    return bytes.fromhex( s )


def int_to_bytes( num, sz , endian='little'):
    return num.to_bytes(sz, byteorder= endian )

def bytes_to_int( bites, endian='little' ):
    #int_val = int.from_bytes(bites , "big")
    int_val = int.from_bytes(bites , endian,  signed=  False)
    print(f"Bites:{bites} = Int:{int_val}")
    return int_val

#Test code added
def overwrite_at_offset(orig, new_bytes, offset):
    newln = len(new_bytes)
    modified = orig[:offset] + new_bytes + orig[offset+newln:]
    assert ( len(orig) == len(modified) )
    return modified

#Test code added
def remove_n_bytes(orig, n, offset):
    assert (n < (len(orig) - offset) )
    return orig[:offset] + orig[offset+n:]

#this needs testing
def add_bytes_at_offset( orig, new_bytes , offset ):
    return orig[:offset] + new_bytes + orig[offset:]

def test_overwrite_at_offset():
    s = 'aaa bbb aaa'.encode()
    finals = 'aaa aaa aaa'.encode()
    newb = 'aaa'.encode()
    modified = overwrite_at_offset(s, newb, 4)
    assert( modified == finals)

def test_remove_n_bytes():
    s = 'aaabbbaaa'.encode()
    modified = remove_n_bytes(s, 3, 3)
    assert(modified == 'aaaaaa'.encode())
    #print(remove_n_bytes(s, 9, 3)) #this will fail

def test_add_bytes_at_offset():
    s = 'aaaaaa'.encode()
    modified = add_bytes_at_offset( s, 'bbb'.encode() , 3 )
    assert( modified == 'aaabbbaaa'.encode())

def test_some_functions():
    test_overwrite_at_offset()
    test_remove_n_bytes()
    test_add_bytes_at_offset()

test_some_functions()

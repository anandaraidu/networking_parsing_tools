from collections import namedtuple
import binary_utils as butils

#field = namedtuple('field', ['offset', 'type', 'len', 'value'] )
#netbios = field( 0, 4, 'struct', 0)
#smb2 = field(4, 'opaque', 64, 0 )
#read_request = field(4, 'opaque', 64, 0 )

SMB_READ_REQ_FILE  = 'readRequest.payload'
SMB_READ_RESP_FILE  = 'readResponse.payload'
reqbuff = butils.file_to_bytes(  SMB_READ_REQ_FILE )
respbuff = butils.file_to_bytes(  SMB_READ_RESP_FILE )

#print( c1[2:4])
#print( butils.bytes_to_int( c1[72:76]))
#print( butils.int_to_bytes (4096, 4))


#new_len = 1024

def modify_read_req_filelen(reqbuff, new_len):
    len_off = 72
    newbytes = butils.int_to_bytes( new_len, 4 )
    return butils.overwrite_at_offset( reqbuff, newbytes, len_off)

def modify_read_resp_filelen( respbuff,  new_len):
    netbios_len_off = 1
    smb_len_off = 72

    #setting in NETBIOS header
    netbios_len = 80 + new_len
    netbios_bytes = butils.decimal_to_hex_bytes( netbios_len )

    if len(netbios_bytes) == 2:
        netbios_len_off = 2
    elif len(netbios_bytes) == 3:
        pass
    else:
        t = 1/0 #should never come here

    t1 = butils.overwrite_at_offset( respbuff, netbios_bytes, netbios_len_off )
    

    #setting in response header of SMB
    newbytes = butils.int_to_bytes( new_len, 4 )
    t2 = butils.overwrite_at_offset( t1, newbytes, smb_len_off)


    payload_off = t2[:84]
    content = ['a'] * new_len
    content_as_str = ''.join(content)
    return t2[:84] + content_as_str.encode()

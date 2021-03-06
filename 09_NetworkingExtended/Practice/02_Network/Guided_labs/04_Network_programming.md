# Converting integers to and from host to network byte order
If you ever need to write a low-level network application, it may be necessary to handle the low-level data transmission over the wire between two machines. This operation requires some sort of conversion of data from the native host operating system to the network format and vice versa. 
This is because each one has its own specific representation of data.

Python's socket library has utilities for converting from a network byte order to host byte order and vice versa. You may want to become familiar with them, for example, ntohl()/htonl().

Let us define the convert_integer() function, where the ntohl()/htonl() socket class functions are used to convert IP address formats.

Listing below shows integer_conversion as follows:
```python
#!/usr/bin/env python 

# This program is optimized for Python 2.7.12 and Python 3.5.2. 
# It may run on any other version with/without modifications. 
 
import socket 
 
def convert_integer(): 
    data = 1234 
    # 32-bit 
    print ("Original: %s => Long  host byte order: %s, Network byte order: %s" %(data, socket.ntohl(data), socket.htonl(data))) 
    # 16-bit 
    print ("Original: %s => Short  host byte order: %s, Network byte order: %s" %(data, socket.ntohs(data), socket.htons(data))) 
 
     
if __name__ == '__main__': 
    convert_integer() 
 ```
If you run this recipe, you will see the following output:

```python
$ python 1_5_integer_conversion.py 
Original: 1234 => Long  host byte order: 3523477504, 
Network byte order: 3523477504
Original: 1234 => Short  host byte order: 53764, 
Network byte order: 53764
```  

## What's Happening:
Here, we take an integer and show how to convert it between network and host byte orders. The ntohl() socket class function converts from the network byte order to host byte order in a long format. Here, n represents network and h represents host; l represents long and s represents short, that is, 16-bit.

























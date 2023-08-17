import base64
import urllib.parse

def main():
    encoding = ("JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm" 
    , "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2" 
    , "JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1")
    pw = ""
    pw = pw.join(encoding) #Concat string together
    
    decoded64 = base64.b64decode(pw) #decode the base64
    print(f'Decoding base64: {decoded64}')
    urlParsed = urllib.parse.unquote(decoded64) #decode the url encoding
    print(f'Parsing URL encoding: {urlParsed}')

main()
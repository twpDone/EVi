#!/usr/bin/python3

import sys
import argparse
try :
    import Image
except:
    from PIL import Image # Deprecated

parser = argparse.ArgumentParser( description='Scan File and View Entropy')
parser.add_argument('inFile', default=None, type=argparse.FileType('r',encoding="latin-1"), help='File to Scan')
parser.add_argument('--outFile', default=None, type=str, help='File to Save the img')
args = parser.parse_args()

def raw2Int(raw):
    return ord(raw)

print("Processing Starts Here (This May Take A While)")

content = args.inFile.read()
args.inFile.close()

size=(256,int((len(content)/256)+1))
im = Image.new('RGB',size)
pix=im.load()

maxint=raw2Int(max(content))
xO=0
yO=0
for b in content:
    v=raw2Int(b)
    try:
            if v < maxint/3:
                    pix[xO,yO]=(v,0,0)
            elif v < 2*(maxint/3):
                    pix[xO,yO]=(0,v,0)
            else:
                    pix[xO,yO]=(0,0,v)
    except Exception as ex:
            print(ex,ex.message)
    xO+=1
    if xO > 255 :
            xO=0
            yO+=1

if args.outFile != None:
    args.outFile+=".png"
    print("Saving Results In "+args.outFile+" !")
    im.save(args.outFile)
im.show()


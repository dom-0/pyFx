
# Image Processing Tool
# 1) Change file type
# 2) Resize
# 3) Decrease Quality / reduce storage
# 4) Rotate along with degree


### Exit codes
#   10 - output file extension is not the same as converted file type...Not that it matters! 
#   11 - source file couldnt be deleted

### Examples
#   python3 imageMod.py -i mmcm.jpg -o as.jpeg -t jpeg  -l 100 -w 100 -r 180 -a 12 -d
#   python3 imageMod.py -i mmcm.jpg -o as.jpeg -t jpeg -r 90 -a 100 -q 25


import argparse
import sys, os
from PIL import Image, ImageFilter

def checkType(typ: str) -> None:
    ''' Checks if the file extension is same as the output file type '''
    if os.path.splitext(outFile)[1].lower() != f".{typ.lower()}":
        print ("Output file extension is not the same as the type")
        exit(10)

def del_srcFile() -> None:
    ''' Deletes source file if -d or --delete is specified '''
    os.remove(inFile) or exit(11)
    print(f"Deleted: {inFile}")

def set_aspectRatio(*args, **kwargs) -> object:
    ''' Adjusts Aspect Ratio as entered '''
    image = args[1]
    (l, w) = image.size
    ar = int(args[0])
    mod_l = l / 100 * ar
    mod_w = w / 100 * ar
    image.thumbnail((mod_l,mod_w))
    print (f"Image size decreased with the entered aspect ratio of: {ar}")
    return (image)

    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="change file type: PNG, JPEG") # DONE
    parser.add_argument("-a", "--aspect", help="keep existing aspect ratio and increase or decrease by percentage eg: 20 or 120") # DONE
    parser.add_argument("-d", "--delete", action="store_true", help="delete the input file") # DONE
    parser.add_argument("-s", "--resize", action="store_true", help="resize")
    parser.add_argument("-l", "--length", help="new length")
    parser.add_argument("-w", "--width", help="new width")
    parser.add_argument("-q", "--quality", help="modify quality to reduce KBs") # DONE
    parser.add_argument("-r", "--rotate", help="rotate the image...specify degrees clockwise") # DONE
    parser.add_argument("-i", "--input", required=True, help="name of the input file") # DONE
    parser.add_argument("-o", "--output", required=True, help="name of the output file") # DONE

    
    args = parser.parse_args()

    ## Checking if output file type is the same as convered type
    
    inFile, outFile = args.input, args.output

    checkType(args.type)
    
    img = Image.open(inFile)
    

    if args.length or args.width:
        (l, w) = img.size
        mod_l = l if not args.length else args.length
        mod_w = w if not args.width else args.width
        mod_l, mod_w = int(mod_l), int(mod_w)
        if args.aspect: 
            img.thumbnail((mod_l,mod_w))
            print("Ignoring value of Aspect Ratio entered since length and width have been entered")
            print("Adjusting new image size to the best possible Aspect Ratio...")
            args.aspect = False
        else: 
            img = img.resize((mod_l,mod_w))


        
    if (args.rotate): img = img.rotate(int(args.rotate))
    
    if (args.aspect): img = set_aspectRatio(args.aspect, img)
    
    if args.type and args.quality:
        img.save(outFile, args.type, quality=int(args.quality))
    elif args.type and not args.quality:
        img.save(outFile, args.type)
    elif args.quality and not args.type:
        img.save(outFile, quality=int(args.quality))
    else:
        img.save(outFile)

    if args.delete: del_srcFile()
    
    print(f"\nNew file has been generated as: {outFile}")
    print(f"Size: {img.size}")
    print(f"Format: {img.format}")
    print(f"Mode: {img.mode}\n")
    
    

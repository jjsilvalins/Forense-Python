from PIL import Image, ExifTags

filename = 'Exemplo.jpg'
img = Image.open(filename)

exifdata = img._getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = ExifTags.TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")

'''
def getHexToHex(file, add1, add2):
    print(add2)

        
def getFileBytes(filename):
    with open(filename, 'rb') as f:
        fileHex = f.read()
    return fileHex

def getHex(decimal):
    hexa = "{0:#0{1}x}".format(decimal,6)
    hexBytes = bytes.fromhex(hexa[2:])
    return hexBytes

decimal = 271
print(getHex(decimal))
fileBytes = getFileBytes(filename)
start = fileBytes.find(getHex(decimal))

with open(filename, 'rb') as f:
    b = f.read()[start:start+80]
texto = "".join([chr(i) if 32 <= i <= 127 else "." for i in b])
print(texto)
'''

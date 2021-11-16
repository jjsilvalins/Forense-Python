magic_numbers = {
    'png': bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
    'jpg': bytes([0xFF, 0xD8, 0xFF, 0xE0]),
    'doc': bytes([0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1]),
    'xls': bytes([0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1]),
    'ppt': bytes([0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1]),
    'docx': bytes([0x50, 0x4B, 0x03, 0x04, 0x14, 0x00, 0x06, 0x00]),
    'xlsx': bytes([0x50, 0x4B, 0x03, 0x04, 0x14, 0x00, 0x06, 0x00]),
    'pptx': bytes([0x50, 0x4B, 0x03, 0x04, 0x14, 0x00, 0x06, 0x00]),
    'pdf': bytes([0x25, 0x50, 0x44, 0x46]),
    'dll': bytes([0x4D, 0x5A, 0x90, 0x00]),
    'exe': bytes([0x4D, 0x5A]),
}

magic_numbers["zip"] = bytes.fromhex("50 4B 03 04")

max_read_size = max(len(m) for m in magic_numbers.values())

filename = "Exemplo.jj"

with open(filename, 'rb') as fd:
    file_head = fd.read(max_read_size)

print(f"Header do arquivo: {file_head} - HEX")
print(f"Header do arquivo: {' '.join(['{:02x}'.format(x) for x in file_head])} - ASCII")

for ext in magic_numbers:
    if file_head.startswith(magic_numbers[ext]):
        print(f"Tipo do Arquivo: .{ext}")

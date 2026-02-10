text = "lactf{REDACTED}"
endian = text.encode(encoding="UTF-16LE").decode(encoding="UTF-8")
# with open("chall.txt", "wb") as file:
#     file.write(endian.encode())


print(endian.encode())
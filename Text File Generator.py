import random as r
import os
import time as t

def CreateTextFile(filename, MBs):
    bytes = MBs * 1024 * 1024
    chunkSize = 1024 * 1024
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 \t\n\r"

    file = open(filename, 'w')
    try:
        for i in range (bytes // chunkSize):
            chunk = os.urandom(chunkSize)
            textChunk = ''.join(chars[b % len(chars)] for b in chunk)
            file.write(textChunk)
    finally:
        file.close()
    
    print(f"File {filename} of size {MBs} MB generated successfully.")

CreateTextFile("Sample 200 MB.txt", 200)
CreateTextFile("Sample 400 MB.txt", 400)
CreateTextFile("Sample 600 MB.txt", 600)
CreateTextFile("Sample 800 MB.txt", 800)
CreateTextFile("Sample 1000 MB.txt", 1000)

print(f"Execution Time : {end - start}")
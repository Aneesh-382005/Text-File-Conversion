import time as t
 
def ConvertToUppercase(inputFile, outputFile):
    input = open(inputFile, 'r')
    output = open(outputFile, 'w')
    try:
        for line in input:
            output.write(line.upper())

    except Exception as e:
        print("Error: ", e)

    finally:
        input.close()
        output.close()

fileSizes = [200, 400, 600, 800, 1000]
executionTimes = {}
if __name__ == "__main__":
    for size in fileSizes:
        inputFile = f"Data\\Input\\Sample {size} MB.txt"
        outputFile = f"Data\\Output\\Sample {size} MB Uppercase.txt"

        startTime = t.time()
        ConvertToUppercase(inputFile, outputFile)
        endTime = t.time()

        executionTimes[f"{size} MB"] = endTime - startTime

        print(f"Python file {size} MB - Execution Time : {endTime - startTime}")

#include <stdio.h>
#include <time.h>
#include <ctype.h>

void convertToUppercase(char *inputFile, char *outputFile)
    {
    	FILE *input = fopen(inputFile, "r");
        FILE *output = fopen(outputFile, "w");

        if (input == NULL || output == NULL)
        {
            printf("Error opening file");
            return;
        }
        char Line[1024];
        while(fgets(Line, sizeof(Line), input))
        {
        	int i;
            for(i = 0; Line [i] != '\0'; i++)
            {
                Line[i] = toupper(Line[i]);
            }
            fprintf(output, "%s", Line);
        }
        fclose(input);
        fclose(output);
	}

int main()
{
    int fileSize[] = {200, 400, 600, 800, 1000};
    clock_t start, end;
    double executionTime;
    int i;
    for(i = 0; i < sizeof(fileSize) / sizeof(fileSize[0]); i++)
    {
        char inputFileName[100];
        char outputFileName[100];
        sprintf(inputFileName, "Data\\Input\\Sample 200 MB.txt", fileSize[i]);
        sprintf(outputFileName, "Data\\Output\\Sample %d MB Uppercase.txt", fileSize[i]);
        start = clock();
        convertToUppercase(inputFileName, outputFileName);
        end = clock();
    } 
}


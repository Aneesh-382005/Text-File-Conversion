package Scripts.java;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileConverter {

    public static void convertToUppercase(String inputFile, String outputFile) {
        try (BufferedReader reader = new BufferedReader(new FileReader(inputFile));
             FileWriter writer = new FileWriter(outputFile)) {

            String line;
            while ((line = reader.readLine()) != null) {
                writer.write(line.toUpperCase());
                writer.write("\n"); // Ensure each line is terminated properly
            }

        } catch (IOException e) {
            System.err.println("Error processing file: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        int[] fileSizes = {200, 400, 600, 800, 1000};
        long startTime, endTime;
        double executionTime;

        for (int size : fileSizes) {
            String inputFileName = String.format("Data/Input/Sample %d MB.txt", size);
            String outputFileName = String.format("Data/Output/Sample %d MB Uppercase.txt", size);

            startTime = System.currentTimeMillis();
            convertToUppercase(inputFileName, outputFileName);
            endTime = System.currentTimeMillis();

            executionTime = (endTime - startTime) / 1000.0; // Convert to seconds
            System.out.printf("Java: %d MB - Execution time: %.2f seconds\n", size, executionTime);
        }
    }
}

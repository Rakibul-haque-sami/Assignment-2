# Assignment 2, Question 1, Task 1 : Extracting text from multiple csv files and store them in a single '.txt' file
#Importing librarys
import csv
import os
import glob

# The targeted csv file having "CSV" in its name should be saved in the current directory.
# Getting all the CSV files in the current directory.
csv_files = glob.glob('CSV*.csv')
#This line will give the list of csv files found in the directory.
print('The found csv files in the directory are-', csv_files)

# Open a text file to write the extracted text
with open('extracted_text.txt', 'w') as outfile:
  for csv_file in csv_files:
    # Open the CSV file
    with open(csv_file, 'r') as infile:
      # Read the CSV file
      reader = csv.reader(infile)

      # Iterate over the rows
      for row in reader:
        # Write the row to the text file
        outfile.write(','.join(row) + '\n')

print("The text file named 'extracted_text.txt' with the extracted text from csv files has been saved in the current directory")

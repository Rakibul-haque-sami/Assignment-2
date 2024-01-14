import pandas as pd
import os

# Assuming all CSV files are in the same folder
folder_path = "C:\\Users\\Chicken Milk\\Desktop\\python\\Assignment 2\\CSV"
output_txt_path = "output.txt"

# List all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

# Specify the column name containing text in your CSV files
text_column_name = "TEXT"

# Extract text from CSV files and store in a single text file
with open(output_txt_path, "w", encoding="utf-8") as output_file:
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        
        # Check if the specified text column exists in the DataFrame
        if text_column_name in df.columns:
            text_column = df[text_column_name]
            
            # Write each text value to the output file
            for text in text_column:
                output_file.write(str(text) + "\n")
        else:
            print(f"Warning: {text_column_name} not found in {file_path}")

print("Extraction and writing to output.txt completed.")

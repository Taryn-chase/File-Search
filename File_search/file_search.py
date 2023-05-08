#!/usr/bin/env python3
import os
import sys
import time
import glob
from pathlib import Path
import multiprocessing as mp

# Function to prompt the user to choose a reference file from a given directory
def choose_reference_file(resources_dir):
    try:
        files = sorted(glob.glob(os.path.join(resources_dir, '*')))
        if not files:
            raise FileNotFoundError("No files found in the given directory.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    while True:
        for idx, file in enumerate(files, 1):
            print(f"{idx}. {os.path.basename(file)}")
        try:
            choice = int(input("Please choose the Reference file: "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            else:
                print("Invalid selection. Please choose a valid file.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to search a given value in the reference file and append the matched lines to the search results file
def search_and_append(value, Reference_file, Search_results):
    print(f"Searching for value: {value}")
    try:
        with open(Reference_file, 'r') as ref_file, open(Search_results, 'a') as output:
            for line in ref_file:
                if value in line:
                    output.write(line)
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")

def main():
    # Define the file and directory paths
    values_file = os.path.expanduser('~/Documents/File_search/Search/Array.txt')
    resources_dir = os.path.expanduser('~/Documents/File_search/Resources')
    try:
        Reference_file = choose_reference_file(resources_dir)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Create a timestamp and output directory
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_dir = os.path.expanduser(f'~/Documents/File_search/Output/output_{timestamp}')
    os.makedirs(output_dir, exist_ok=True)

    # Define the search results output file path
    output_file_name = f'{Path(Reference_file).stem}_{timestamp}_output.txt'
    Search_results = os.path.join(output_dir, output_file_name)

    # Read values from the values_file
    try:
        with open(values_file, 'r') as f:
            values = [line.strip() for line in f]
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Present the user with options for searching
    print("\nChoose an option:")
    print("1. Search for values from the array (file)")
    print("2. Enter a single value to search for")
    option = input()

    # Record the start time of the search process
    start_time = time.time()

    # Perform search based on the user's choice
    if option == '1':
        with mp.Pool(processes=6) as pool:
            pool.starmap(search_and_append, [(value, Reference_file, Search_results) for value in values])
    elif option == '2':
        while True:
            single_value = input("Enter the value to search for (or type 'exit' to finish): ")
            if single_value == 'exit':
                break
            search_and_append(single_value, Reference_file, Search_results)
    else:
        print("Invalid option. Exiting.")
        sys.exit(1)
        
        # Show time elapsed 
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(f"Time elapsed: {time_elapsed} seconds")

    print("File complete")
# Show results in terminal
    with open(Search_results, 'r') as f:
        print(f.read())        
        
if __name__ == '__main__':
    main()

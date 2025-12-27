#!/usr/bin/env python3
"""
Script to read peptide data and search for specific motifs.
This script reads a CSV file containing peptide sequences and their sources,
searches for the motif K..K (Lysine, any two characters, Lysine),
and prints the source of peptides containing this motif.
"""

import csv
import re

def main():
    # Path to the peptide data file
    data_file = 'data/peptides.csv'
    
    # Regular expression pattern for K..K motif
    pattern = re.compile(r'K..K')
    
    print("Searching for peptides containing motif 'K..K'...")
    
    try:
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            # Ensure required columns exist
            if 'sequence' not in reader.fieldnames or 'source' not in reader.fieldnames:
                print("Error: CSV must contain 'sequence' and 'source' columns.")
                return
            
            matches_found = False
            for row in reader:
                sequence = row['sequence']
                source = row['source']
                
                # Search for motif in sequence
                if pattern.search(sequence):
                    print(f"Motif found in peptide from: {source}")
                    matches_found = True
            
            if not matches_found:
                print("No peptides containing the motif 'K..K' were found.")
    
    except FileNotFoundError:
        print(f"Error: File '{data_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
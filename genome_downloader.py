#!/usr/bin/env python3

import subprocess
import sys
import os

# Function to run the download_from_urls script
def run_download_from_urls():
    print("Running the download from URLs script...")
    subprocess.run(["python3", "download_from_urls.py"])

# Function to run the download_from_accession script
def run_download_from_accession():
    print("Running the download from Accession script...")
    subprocess.run(["python3", "download_from_accession.py"])

def main():
    print("Welcome to Genome Downloader!")
    print("Choose the download method:")
    print("1. Download genomes from URLs.")
    print("2. Download genomes from Accessions.")
    
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        run_download_from_urls()
    elif choice == "2":
        run_download_from_accession()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        sys.exit(1)

if __name__ == "__main__":
    main()

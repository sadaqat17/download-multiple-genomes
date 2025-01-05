#!/usr/bin/env python3

import os
import subprocess
import zipfile

def download_file_type(accession, output_folder, file_type):
    print(f"Downloading {file_type} for accession: {accession}")
    command = [
        "datasets", "download", "genome", "accession", accession,
        "--include", file_type
    ]
    try:
        subprocess.run(command, check=True)
        downloaded_file = "ncbi_dataset.zip"
        if os.path.exists(downloaded_file):
            with zipfile.ZipFile(downloaded_file, 'r') as zip_ref:
                zip_ref.extractall(output_folder)
            print(f"{file_type} for accession {accession} extracted and saved to {output_folder}")
            os.remove(downloaded_file)
        else:
            print(f"{file_type} for accession {accession} not found or skipped.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {file_type} for accession {accession}: {e}")

def download_genomes(accession, output_folder):
    file_types = ["genome", "rna", "protein", "cds", "gff3", "gtf", "gbff", "seq-report"]
    for file_type in file_types:
        download_file_type(accession, output_folder, file_type)

def download_genomes_from_accessions(accessions, output_folder):
    for accession in accessions:
        download_genomes(accession, output_folder)

def get_accessions_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            accessions = [line.strip() for line in file if line.strip()]
        return accessions
    except Exception as e:
        print(f"Failed to read accessions from file: {e}")
        return []

def main():
    print("Choose input method:")
    print("1. Enter accessions directly (comma-separated).")
    print("2. Provide a text file with one accession per line.")
    choice = input("Enter 1 or 2: ").strip()

    accessions = []
    if choice == "1":
        accession_input = input("Enter accessions (comma-separated): ").strip()
        accessions = [accession.strip() for accession in accession_input.split(",") if accession.strip()]
    elif choice == "2":
        file_path = input("Enter the path to the text file: ").strip()
        accessions = get_accessions_from_file(file_path)
    else:
        print("Invalid choice. Exiting.")
        return

    if not accessions:
        print("No accessions provided. Exiting.")
        return

    output_folder = input("Enter the folder to save downloaded genomes (default: genomes): ").strip() or "genomes"
    os.makedirs(output_folder, exist_ok=True)
    download_genomes_from_accessions(accessions, output_folder)

if __name__ == "__main__":
    main()

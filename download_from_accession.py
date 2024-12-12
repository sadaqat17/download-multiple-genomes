#!/usr/bin/env python3

import os
import subprocess
import shutil
import zipfile

def download_genomes(accession, output_folder):
    try:
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Print the accession number being downloaded
        print(f"Downloading genome for accession: {accession}")

        # Using the NCBI datasets tool to fetch the genome by accession number
        command = [
            "datasets", "download", "genome", "accession", accession
        ]

        # Execute the command to download the genome
        subprocess.run(command, check=True)

        # After downloading, check for the zip file
        downloaded_file = "ncbi_dataset.zip"
        if os.path.exists(downloaded_file):
            # Extract the contents of the zip file
            with zipfile.ZipFile(downloaded_file, 'r') as zip_ref:
                zip_ref.extractall(output_folder)

            # Move the downloaded files to the user-specified output folder
            print(f"Genome for {accession} extracted and saved to {output_folder}")

            # Remove the zip file if it exists after extraction
            try:
                os.remove(downloaded_file)
            except OSError:
                # Suppress error if the file can't be found or deleted
                pass
        else:
            print(f"Error: Genome file for {accession} was not found.")

    except subprocess.CalledProcessError as e:
        print(f"Failed to download genome for {accession}: {e}")
    except Exception as e:
        print(f"An error occurred for {accession}: {e}")

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
    download_genomes_from_accessions(accessions, output_folder)

if __name__ == "__main__":
    main()

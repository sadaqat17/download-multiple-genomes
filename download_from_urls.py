#!/usr/bin/env python3

import os
import requests
from tqdm import tqdm  # For progress bar

def download_file(url, output_folder):
    try:
        os.makedirs(output_folder, exist_ok=True)
        file_name = url.split("/")[-1]
        file_path = os.path.join(output_folder, file_name)

        print(f"Downloading: {url}")
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name) as pbar:
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                            pbar.update(len(chunk))

        print(f"Saved: {file_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def download_from_urls(urls, output_folder):
    for url in urls:
        download_file(url, output_folder)

def get_urls_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            urls = [line.strip() for line in file if line.strip()]
        return urls
    except Exception as e:
        print(f"Failed to read URLs from file: {e}")
        return []

def main():
    print("Choose input method:")
    print("1. Enter URLs directly (comma-separated).")
    print("2. Provide a text file with one URL per line.")
    choice = input("Enter 1 or 2: ").strip()

    urls = []
    if choice == "1":
        url_input = input("Enter URLs (comma-separated): ").strip()
        urls = [url.strip() for url in url_input.split(",") if url.strip()]
    elif choice == "2":
        file_path = input("Enter the path to the text file: ").strip()
        urls = get_urls_from_file(file_path)
    else:
        print("Invalid choice. Exiting.")
        return

    if not urls:
        print("No URLs provided. Exiting.")
        return

    output_folder = input("Enter the folder to save downloaded files (default: downloads): ").strip() or "downloads"
    download_from_urls(urls, output_folder)

if __name__ == "__main__":
    main()

# Genome Downloader

This repository contains scripts to download multiple genome data either by URLs or accession numbers from NCBI.

## Pre-requisites

Before running the scripts, you need to install the following:

### Required Tools and Libraries:

1. **Python 3**
2. **NCBI Datasets Tool** (for downloading genomes by accession numbers)
3. **Python Libraries**:
   - `requests` (for making HTTP requests)
   - `tqdm` (for progress bar during downloads)
4. **Git** (Optional, only if you plan to clone the repository using Git)

### Installation Commands:

To install the necessary tools and libraries, follow these commands:

#### 1. Install **Python 3**:
Run this into the Conda base:
```bash
conda install python=3.9
```

#### 2. Install **NCBI Datasets Tool**:
You need to install the **NCBI Datasets Tool** using **Conda**. Run the following command:
```bash
conda install -c conda-forge ncbi-datasets-cli
```

#### 3. Install Required Python Libraries:
You can install the required Python libraries using `pip`:
```bash
pip install requests tqdm
```

#### 4. Install **Git** (Optional):
If you plan to clone the repository using Git, you need **Git** installed. You can install Git from here:
- [Git Downloads](https://git-scm.com/downloads)

---

## Scripts

### `download_from_urls.py`
- **Purpose**: This script downloads genomes from a list of URLs that you provide.
- **Usage**: It lets you input URLs directly or through a text file, and it will download the genomes accordingly.

### `download_from_accession.py`
- **Purpose**: Downloads genomes using accession numbers from NCBI via the NCBI Datasets Tool.
- **Usage**: Accepts accession numbers (either entered directly or through a text file) and downloads genomes using the NCBI Datasets Tool.

### `genome_downloader.py`
- **Purpose**: This is the main script that combines the two above scripts. It lets you choose whether you want to download genomes by URLs or by accession numbers.
- **Usage**: When you run this script, you can choose between downloading genomes by URLs or by accession numbers, and the relevant script will be executed.

---

## Input Files (Uploading accessions.txt and urls.txt)

To download genomes, you can use **text files** containing a list of URLs or accession numbers.

1. **URLs File (urls.txt)**:
   - Create a file named `urls.txt` where each line contains a **URL** of a genome to download.
   - Example content of `urls.txt`:
     ```(https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/011/075/055/GCF_011075055.1_CATAS_Mindica_2.1/GCF_011075055.1_CATAS_Mindica_2.1_genomic.fna.gz)
https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/011/075/055/GCF_011075055.1_CATAS_Mindica_2.1/GCF_011075055.1_CATAS_Mindica_2.1_genomic.gtf.gz
     ```
   
2. **Accessions File (accessions.txt)**:
   - Create a file named `accessions.txt` where each line contains a **NCBI accession number** of a genome.
   - Example content of `accessions.txt`:
     ```
     GCA_011075055.1
     GCF_011075055.1
     ```

### How to Upload and Use the Files:

1. **Prepare the Files**:
   - Place the `urls.txt` or `accessions.txt` file in the same directory as the script or provide the full path to the file when prompted by the script.

2. **Running the Script**:
   - When you run `genome_downloader.py`, the script will prompt you to choose the input method.
   
   - **Option 1**: Enter URLs directly or provide a file (`urls.txt`).
     - If you choose this, you can enter URLs manually or specify the path to the `urls.txt` file when prompted.
   
   - **Option 2**: Enter accessions directly or provide a file (`accessions.txt`).
     - If you choose this, you can input accession numbers manually or provide the path to the `accessions.txt` file.

3. **Example of Running the Script**:
   - If you have a `urls.txt` file in your directory, you can run the following:
     ```bash
     python3 genome_downloader.py
     ```
     - The script will ask you whether to download from URLs or accessions. Choose the relevant option and provide the `urls.txt` file when prompted.

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/sadaqat17/genome-downloader.git
   ```
1. Clone the repository (Manual downloading) if git clone is not working
 ```bash
   Manually download the .zip file
   ```
   If it not working then manually download the .zip file

3. Navigate to the project directory:
   ```bash
   cd download-multiple-genomes-main
   ```

4. Run the main script:
   ```bash
   python3 genome_downloader.py
   ```

5. The script will prompt you to choose between:
   - **Option 1**: Download genomes from URLs.
   - **Option 2**: Download genomes from accession numbers.

Based on your choice, the relevant script will run and you can follow the prompts to complete the download.

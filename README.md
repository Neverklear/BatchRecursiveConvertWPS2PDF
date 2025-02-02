# WPS to PDF Converter using LibreOffice (soffice)

## Overview  
This script recursively scans a folder and its subdirectories for `.wps` (Microsoft Works Document) files and converts them into `.pdf` using LibreOffice (soffice).  
The script preserves the folder structure, saving each PDF in the same location as its original WPS file.

## Features  
- Recursively scans directories – Finds all `.wps` files in a given folder and subfolders.  
- Batch conversion – Uses `soffice` (LibreOffice) to convert `.wps` to `.pdf`.  
- Maintains folder structure – Saves PDFs in the same directory as their original WPS files.  
- Verbose output – Displays progress, errors, and success messages for each conversion.  

## Requirements  

### Install Python (if not already installed)  
- Download & Install Python: [Python Downloads](https://www.python.org/downloads/)  
- Ensure Python is added to the system PATH.  

### Install LibreOffice  
- Download & Install LibreOffice: [LibreOffice Download](https://www.libreoffice.org/download/download/)  
- Ensure LibreOffice's `soffice` command is available in your system’s PATH.  

To verify, open Command Prompt (cmd) and run:  
```
soffice --version
```
If this outputs a version number, LibreOffice is correctly installed.  

## Usage  

### Clone this repository  
```
git clone https://github.com/YOUR_GITHUB_USERNAME/wps-to-pdf.git
cd wps-to-pdf
```

### Set your target folder  
Open `convert.py` and update the `root_folder` variable:  
```
root_folder = "D:\Recipes"
```
(Change `"D:\Recipes"` to the actual folder where your `.wps` files are stored.)  

### Run the script  
```
python convert.py
```

## Expected Output  
The script will display progress while scanning and converting files:  
```
[*] Scanning for .wps files in: D:\Recipes
[!] Found 142 .wps files to convert.

[+] Converting: D:\Recipesolder1
ecipe1.wps → D:\Recipesolder1
ecipe1.pdf
[✔] Success: D:\Recipesolder1
ecipe1.pdf

[+] Converting: D:\Recipesolder2
ecipe2.wps → D:\Recipesolder2
ecipe2.pdf
[✔] Success: D:\Recipesolder2
ecipe2.pdf

...
[✔] All conversions completed!
```

## Troubleshooting  

### "soffice is not recognized" error  
Ensure LibreOffice is installed and added to the system PATH.  
Test if LibreOffice is accessible:  
```
"C:\Program Files\LibreOffice\program\soffice.exe" --version
```
If this works, but `soffice --version` does not, add LibreOffice to PATH:  
1. Press `Win + R`, type `sysdm.cpl`, and press Enter.  
2. Go to the Advanced tab → Environment Variables.  
3. Edit Path → Add the following:  
   ```
   C:\Program Files\LibreOffice\program
   ```
4. Click OK, restart your PC, and try again.  

### No `.wps` files found  
- Manually check if `.wps` files exist by searching `*.wps` in File Explorer.  
- Ensure the `root_folder` in the script is set correctly.  

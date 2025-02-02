import os
import subprocess

def convert_wps_to_pdf(input_path):
    """
    Convert a .wps file to a .pdf using LibreOffice (soffice) and print progress.
    """
    output_dir = os.path.dirname(input_path)  # Keep the PDF in the same folder
    output_file = os.path.splitext(os.path.basename(input_path))[0] + '.pdf'
    output_path = os.path.join(output_dir, output_file)

    print(f"[+] Converting: {input_path} → {output_path}")

    try:
        # Convert the file using LibreOffice (soffice)
        subprocess.run([
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            input_path,
            "--outdir",
            output_dir
        ], check=True)

        print(f"[✔] Success: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"[✖] Error converting {input_path}: {e}")

def find_wps_files(root_folder):
    """
    Recursively find all .wps files in a root folder and its subdirectories.
    """
    wps_files = []
    print(f"[*] Scanning for .wps files in: {root_folder}")

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith('.wps'):
                file_path = os.path.join(dirpath, filename)
                wps_files.append(file_path)

    print(f"[!] Found {len(wps_files)} .wps files to convert.\n")
    return wps_files

def main():
    # Change this to your main 'recipes' folder path
    root_folder = "D:\\Recipes"

    wps_files = find_wps_files(root_folder)

    if not wps_files:
        print("[!] No .wps files found. Exiting.")
        return

    for wps_file in wps_files:
        convert_wps_to_pdf(wps_file)

    print("\n[✔] All conversions completed!")

if __name__ == "__main__":
    main()

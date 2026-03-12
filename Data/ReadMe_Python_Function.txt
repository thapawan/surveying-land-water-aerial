README: Automatic Leica .m00 to RINEX Conversion (Python Drag-and-Drop)
This guide provides clear, easy-to-follow steps to automatically convert Leica .m00 GNSS raw data files to RINEX format (.obs and .nav) using the provided Python script (convert_to_rinex.py) and TEQC executable.

                                                 Step-by-Step Guide
 Step 1: Set Up Python Environment (Important!)
Make sure you have Python installed:

Download Python from the official site:
https://www.python.org/downloads/

After installation:

☑ Add Python to PATH
If Python is already installed and you missed adding it to PATH:

Search for "Edit the system environment variables" in Windows Search.

Click on Environment Variables.

Under System Variables, find and select Path, then click Edit.

Click New and paste the path to your Python installation, typically:

C:\Users\YourUsername\AppData\Local\Programs\Python\Python312\python.exe


Click OK on all open windows to confirm.

 Step 2: Prepare the Conversion Folder
Create a clearly named folder on your desktop or elsewhere, e.g.:

C:\RINEX_Converter\
Copy both required files clearly into this folder:

teqc.exe (download from UNAVCO TEQC)

convert_to_rinex.py (provided Python script)

Your final structure clearly:

C:\RINEX_Converter\
   ├── teqc.exe
   └── convert_to_rinex.py

Step 3: Convert Leica .m00 Files to RINEX
Clearly locate your .m00 file anywhere on your computer.

Drag-and-drop your .m00 file directly onto the convert_to_rinex.py script.

This automatically creates the .obs and .nav files next to your original .m00 file.

Step 4: Verify Conversion Results
Check the same folder as your original .m00 file for two new files:

your_filename.obs
your_filename.nav
Now you're ready to upload these files to OPUS or other RINEX-compatible services.

Quick Troubleshooting:
If the conversion fails or produces zero-size files:

Double-check Python installation and your environmental variables.

Ensure both teqc.exe and convert_to_rinex.py remain together in the same folder.


You're all set for fast and automatic .m00 to RINEX file conversions!
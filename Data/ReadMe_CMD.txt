HOW TO CONVERT LEICA .M00 GNSS FILES TO RINEX USING TEQC
Follow these clear and simple steps to convert your Leica GNSS base station files (.m00 format) to RINEX (.obs and .nav) format using TEQC:

 Setup your TEQC Folder
Download the TEQC executable for Windows from:

https://www.unavco.org/software/data-processing/teqc/teqc.html

Extract teqc.exe clearly into a simple folder, for example:

Step 1: Create a Working Folder

Create a folder named "TEQC" in your desired location on your computer.
Example: C:\TEQC

Step 2: Copy teqc.exe and Your File

Place the downloaded "teqc.exe" into your TEQC folder (C:\TEQC).

Also, copy your Leica ".m00" file into this same folder.

Your folder should look similar to this:

C:\TEQC
│
├── teqc.exe
└── your_file.m00

Step 3: Open the Command Prompt

Press the Windows Key, type "cmd", and press Enter to open the Command Prompt.

Navigate to your TEQC folder by typing:
cd C:\TEQC

Step 4: Run the Conversion Command

Run the following command, making sure to replace "your_file.m00" with your actual file name:

teqc.exe -leica mdb +nav your_file.nav your_file.m00 > your_file.obs

For example, if your file name is "4734_0920_085736.m00", your command is:

teqc.exe -leica mdb +nav 4734_0920_085736.nav 4734_0920_085736.m00 > 4734_0920_085736.obs

Step 5: Verify Converted Files

After the command finishes, you will see two new files created in the folder:

your_file.obs (RINEX observation file)

your_file.nav (RINEX navigation file)

Make sure these files have size greater than 0 KB to confirm successful conversion.

Step 6: Submit Files to OPUS

Visit the OPUS website at https://geodesy.noaa.gov/OPUS/
Upload your newly generated ".obs" file for corrections.

COMMON ISSUES:

Zero-sized output files:
Ensure the ".m00" file and "teqc.exe" are correctly located in the same folder, and you correctly navigated (cd) to that folder in Command Prompt.

Error messages:
Check file names carefully and ensure no typing errors occurred.

You're now ready to consistently convert your Leica GNSS files easily and effectively using TEQC.








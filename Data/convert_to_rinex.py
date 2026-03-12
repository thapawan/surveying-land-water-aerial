import subprocess, sys, os

def convert_to_rinex(m00_file):
    m00_file = os.path.abspath(m00_file)
    base_dir = os.path.dirname(m00_file)
    base_name = os.path.splitext(os.path.basename(m00_file))[0]

    nav_file = base_name + '.nav'
    obs_file = base_name + '.obs'

    # Automatically find teqc.exe located in the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    teqc_executable = os.path.join(script_dir, "teqc.exe")

    # Build the command clearly
    cmd = f'"{teqc_executable}" -leica mdb +nav "{nav_file}" "{m00_file}" > "{obs_file}"'

    # Run subprocess with working directory explicitly set
    subprocess.run(cmd, shell=True, cwd=base_dir)

    # Check results and provide clear feedback
    obs_path = os.path.join(base_dir, obs_file)
    nav_path = os.path.join(base_dir, nav_file)

    if os.path.exists(obs_path) and os.path.getsize(obs_path) > 0:
        print(f"Conversion succeeded!\nOBS file: {obs_path}\nNAV file: {nav_path}")
    else:
        print("Conversion failed or produced zero-sized files.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Drag and drop your .m00 file onto this Python script to convert it.")
        sys.exit()

    convert_to_rinex(sys.argv[1])


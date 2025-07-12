import os
import sys
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# Get the folder path from command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 checkmp3.py /path/to/mp3/folder")
    sys.exit(1)

root_folder = sys.argv[1]

if not os.path.isdir(root_folder):
    print(f"❌ The path '{root_folder}' is not a valid directory.")
    sys.exit(1)

bad_files = []
total_checked = 0

print(f"🔍 Scanning for MP3s in: {root_folder}\n")

for dirpath, _, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.lower().endswith(".mp3"):
            total_checked += 1
            full_path = os.path.join(dirpath, filename)
            print(f"[{total_checked}] Testing: {full_path}")
            try:
                audio = AudioSegment.from_mp3(full_path)
            except CouldntDecodeError:
                print("  ❌ Could not decode (bad MP3)")
                bad_files.append(full_path)
            except Exception as e:
                print(f"  ❌ Error: {str(e)}")
                bad_files.append(f"{full_path} - Error: {str(e)}")
            else:
                print("  ✅ OK")

# Save the list of bad files
with open("bad_mp3s.txt", "w") as f:
    for bad_file in bad_files:
        f.write(bad_file + "\n")

print(f"\n✅ Scan complete. {total_checked} files checked. {len(bad_files)} bad files written to bad_mp3s.txt.")

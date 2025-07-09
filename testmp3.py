import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# Set your root folder path here
root_folder = "/path/to/your/mp3/folder"
bad_files = []

for dirpath, _, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.lower().endswith(".mp3"):
            full_path = os.path.join(dirpath, filename)
            try:
                audio = AudioSegment.from_mp3(full_path)
            except CouldntDecodeError:
                bad_files.append(full_path)
            except Exception as e:
                bad_files.append(f"{full_path} - Error: {str(e)}")

# Save the list of bad files
with open("bad_mp3s.txt", "w") as f:
    for bad_file in bad_files:
        f.write(bad_file + "\n")

print(f"✅ Scan complete. {len(bad_files)} bad files written to bad_mp3s.txt.")

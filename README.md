# 🎵 MP3 File Validator (Python + Pydub)

This script scans a folder (and all its subfolders) for `.mp3` files, attempts to decode them using `pydub`, and logs any corrupted or unplayable files to a `bad_mp3s.txt` file.

📄 Output
The script creates a file called bad_mp3s.txt in the current directory.

Each line contains the full path to a file that could not be decoded.
---

pip install pydub
brew install ffmpeg
sudo apt update && sudo apt install ffmpeg

## 🛠️ macOS Setup & Usage Instructions

### 1. ✅ Install Homebrew (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. ✅ Install `ffmpeg`
```bash
brew install ffmpeg
```

### 3. ✅ Install Python & `pydub`
If you don’t have Python 3, install it via Homebrew:

```bash
brew install python
```

Then install `pydub`:

```bash
pip3 install pydub
```

### 4. ✅ Create and Run the Script

1. Open Terminal.
2. Save the following script as `check_mp3s.py`:
```python
import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# Change this to your folder path
root_folder = "/Users/yourname/Music/MyMP3s"
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
```

3. Run it:
```bash
python3 check_mp3s.py
```

This will output a file called `bad_mp3s.txt` in your current directory, listing all broken or unplayable MP3 files.


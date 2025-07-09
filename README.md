# 🎵 MP3 File Validator (Python + Pydub)

This script scans a folder (and all its subfolders) for `.mp3` files, attempts to decode them using `pydub`, and logs any corrupted or unplayable files to a `bad_mp3s.txt` file.

📄 Output
The script creates a file called bad_mp3s.txt in the current directory.

Each line contains the full path to a file that could not be decoded.
---

pip install pydub
brew install ffmpeg
sudo apt update && sudo apt install ffmpeg

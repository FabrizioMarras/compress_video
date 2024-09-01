import os
import subprocess
import sys

def compress_videos_in_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".mp4"):
                file_path = os.path.join(root, file)
                compressed_file_path = os.path.join(root, f"{os.path.splitext(file)[0]}_compressed.mp4")
                
                # Check if the compressed file already exists
                if os.path.exists(compressed_file_path):
                    print(f"Skipping {file_path} as {compressed_file_path} already exists.")
                    continue
                
                # FFMPEG command to compress video
                command = [
                    'ffmpeg',
                    '-i', file_path,
                    compressed_file_path
                ]
                
                print(f"Compressing {file_path} to {compressed_file_path}")
                subprocess.run(command, check=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compress_videos.py /path/to/main_folder")
        sys.exit(1)
    
    main_folder = sys.argv[1]
    compress_videos_in_folder(main_folder)

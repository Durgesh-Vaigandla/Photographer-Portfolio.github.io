import os
import subprocess

# Path to the single image
source_dir = r'D:\Code Files\Photographer-Portfolio.github.io-1\images'
filename = 'img-1-1.jpg'

# Path to cwebp executable
cwebp_path = r'C:\Program Files\WebP\cwebp.exe'

# Paths for input and output files
input_file = os.path.join(source_dir, filename)
output_file = os.path.join(source_dir, os.path.splitext(filename)[0] + '.webp')

# Construct command to convert the image to WebP
command = [cwebp_path, input_file, '-o', output_file]

# Execute the command
result = subprocess.run(command, capture_output=True, text=True)

# Print output and errors (if any)
if result.returncode == 0:
    print(f"Converted {filename} successfully.")
else:
    print(f"Failed to convert {filename}. Error: {result.stderr}")

print("Conversion completed.")

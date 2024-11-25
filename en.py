import subprocess
import os

def encode_to_av1(input_file, output_file, crf=30, preset="8"):
    """
    Encode MP4 to AV1-encoded AVI using SVT-AV1 for faster encoding.
    
    Parameters:
        input_file (str): Path to the input MP4 file.
        output_file (str): Path to the output AVI file (AV1 encoded).
        crf (int): Constant Rate Factor (lower value = better quality).
        preset (str): Speed/quality trade-off (range: "0"=best, "8"=fastest).
    """
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    command = [
        "ffmpeg", "-y", "-i", input_file,   # Input MP4 file (overwrite output)
        "-c:v", "libsvtav1",                # Use SVT-AV1 codec for faster encoding
        "-crf", str(crf),                   # Set quality level
        "-preset", preset,                  # Set encoding speed (0=slowest, 8=fastest)
        output_file                         # Output AVI file
    ]

    try:
        print(f"Encoding {input_file} to {output_file}...")
        subprocess.run(command, check=True)
        print(f"Encoding complete. Saved as: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Encoding failed: {e}")

if __name__ == "__main__":
    input_file = input("Enter the file path in input file path in mp4 format:")  # Input MP4 file
    output_file = input("Enter the path t store the (.avi) format:")  # Output AVI (AV1 encoded)
    encode_to_av1(input_file, output_file)

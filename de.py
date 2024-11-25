import cv2
import numpy as np
import os  # To get file sizes

def decode_avi_to_mp4(input_file, output_file):
    """
    Decode an AVI (AV1 encoded) file and save it as an MP4.
    
    Parameters:
        input_file (str): Path to the input AVI file (AV1 encoded).
        output_file (str): Path to the output MP4 file.
    """
    # Open the input AVI file
    cap = cv2.VideoCapture(input_file)
    if not cap.isOpened():
        print(f"Error: Unable to open input file '{input_file}'.")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Set codec and create VideoWriter for MP4 output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height), isColor=True)

    print(f"Decoding {input_file} to {output_file}...")

    # Process each frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Exit loop when no more frames are available

        # Validate frame content
        if frame is None or frame.size == 0:
            print("Warning: Empty frame encountered, skipping...")
            continue

        # Write the valid frame to the MP4 output
        out.write(frame)

    # Release resources
    cap.release()
    out.release()
    print(f"Decoding complete. Saved to: {output_file}")

    # Calculate and print compression ratio
    input_size = os.path.getsize(input_file)
    output_size = os.path.getsize(output_file)

    compression_ratio = input_size / output_size if output_size > 0 else float('inf')
    print(f"Compression Ratio: {compression_ratio:.2f}")

if __name__ == "__main__":
    input_file = input("Enter the path of the avi file: ")  # Encoded input AVI file
    output_file = input("Enter the path of the decompressed file in (.mp4) format: ")  # Decoded MP4 output
    decode_avi_to_mp4(input_file, output_file)

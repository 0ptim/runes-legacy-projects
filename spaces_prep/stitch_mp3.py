import os
import re
import subprocess


def stitch_mp3():
    # Regular expression to match files like "part1 (enhanced).wav", "part2 (enhanced).wav", etc.
    file_pattern = re.compile(r"^part(\d+) \(enhanced\)\.wav$")

    # List to hold files that match the pattern
    files_to_stitch = []

    # Iterate over files in the current directory
    for file in os.listdir("."):
        if file_pattern.match(file):
            # Add file to the list
            files_to_stitch.append(file)

    # Sort files by the numeric part, ensuring they are concatenated in the correct order
    files_to_stitch.sort(key=lambda x: int(file_pattern.match(x).group(1)))

    # Create a temporary file listing all the files to concatenate
    with open("concat_list.txt", "w") as f:
        for file in files_to_stitch:
            f.write(f"file '{file}'\n")

    # Use FFmpeg to concatenate the files and encode to MP3
    output_file = "stitched_output.mp3"
    command = [
        "ffmpeg",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        "concat_list.txt",
        "-c:a",
        "libmp3lame",
        output_file,
    ]
    subprocess.run(command)

    print(f"Stitching completed. Output file: {output_file}")

    # Clean up the temporary file list
    os.remove("concat_list.txt")


if __name__ == "__main__":
    stitch_mp3()

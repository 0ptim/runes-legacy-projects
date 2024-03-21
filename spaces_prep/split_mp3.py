import subprocess
import sys
import math


def split_mp3(input_file):
    # Length of each chunk in seconds (30 minutes * 60 seconds)
    chunk_length = 30 * 60

    # Get the duration of the input file in seconds using ffprobe
    command = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        input_file,
    ]
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    duration = float(result.stdout)

    # Calculate the number of chunks
    num_chunks = math.ceil(duration / chunk_length)

    for i in range(num_chunks):
        start_time = i * chunk_length
        # Using FFmpeg to extract the chunk
        output_file = f"part{i + 1}.mp3"
        command = [
            "ffmpeg",
            "-i",
            input_file,
            "-ss",
            str(start_time),
            "-t",
            str(chunk_length),
            "-acodec",
            "copy",
            output_file,
        ]
        subprocess.run(command)
        print(f"Generated: {output_file}")

    print("Splitting completed.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_mp3.py <input_file>")
        sys.exit(1)
    split_mp3(sys.argv[1])

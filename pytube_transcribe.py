import sys
import datetime as date
import whisper
import pytube


# Download & Convert to audio file
def download_youtube_vid(url: str):
    # Greek: url = 'https://www.youtube.com/watch?v=IJ3S44yJJU4'
    # Hindi: url = https://www.youtube.com/watch?v=xJYsEOdA2cc
    data = pytube.YouTube(url)
    audio = data.streams.get_audio_only()
    filepath = audio.download(output_path="./output")
    print(f"FilePath: {filepath}")

    return filepath


def transcribe_audio(filepath: str):
    start = date.datetime.now()
    model = whisper.load_model("medium")
    result = model.transcribe(filepath)
    end = date.datetime.now()
    print(f'Total Time: {end - start}')
    print(result)


if __name__ == "__main__":
    sysargs = sys.argv[1:]
    args = {}
    for arg in sysargs:
        arg_key, arg_value = arg.split("=", 1)
        args[arg_key] = arg_value

    if "--url" in args:
        filepath = download_youtube_vid(args["--url"])
        transcribe_audio(filepath)


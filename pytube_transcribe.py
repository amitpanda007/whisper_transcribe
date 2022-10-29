import sys
import datetime as date
import whisper
import pytube


# Download & Convert to audio file
def download_youtube_vid(url: str):
    # Greek: url = https://www.youtube.com/watch?v=IJ3S44yJJU4
    # Hindi: url = https://www.youtube.com/watch?v=xJYsEOdA2cc
    print(f"Gathering Youtube audio: {url}")
    data = pytube.YouTube(url)
    audio = data.streams.get_audio_only()
    filepath = audio.download(output_path="output")
    print(f"FilePath: {filepath}")

    return filepath


def transcribe_audio(filepath: str, language=None):
    print(f"Starting Transcription: {filepath}")
    start = date.datetime.now()
    model = whisper.load_model("large")
    result = model.transcribe(filepath, language=language)
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
        # filepath = download_youtube_vid(args["--url"])
        # transcribe_audio(filepath)
        transcribe_audio("F:\CODING\PYTHON\whisper_transcribe\output\OnePlus Nord CE 2 5G Unboxing And First Impressions⚡Confused Edition.mp4", language="hindi")


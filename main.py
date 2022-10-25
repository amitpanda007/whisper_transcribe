import whisper
import json
import datetime as date


def transcribe_data(filename: str):
    name, ext = filename.split(".")

    start = date.datetime.now()
    # Model Type & Options: tiny, base, small, medium, large
    model = whisper.load_model('medium')
    # To run only on PC set fp16=False. eg. model.transcribe(f'./input/{filename}', fp16=False)
    out = model.transcribe(f'./input/{filename}')
    with open(f'./output/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=4)
    end = date.datetime.now()
    print(f'Total Time: {end - start}')


# transcribe_data("Docker_Introduction.mp4")

if __name__ == "__main__":
    transcribe_data("Family Guy S16E01 Emmy-Winning Episode.mp4")
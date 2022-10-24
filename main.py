import whisper
import json
import datetime as date


def transcribe_data(filename: str):
    name, ext = filename.split(".")

    start = date.datetime.now()
    model = whisper.load_model('medium')
    out = model.transcribe(f'./input/{filename}', fp16=False)
    with open(f'./output/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=4)
    end = date.datetime.now()
    print(f'Total Time: {end - start}')


# transcribe_data("Docker_Introduction.mp4")

if __name__ == "__main__":
    transcribe_data("Docker_Introduction.mp4")
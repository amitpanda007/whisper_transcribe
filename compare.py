import re
import json
import time
import datetime


def compare_file(src: str, destination: str):
    if src != "":
        with open(src) as f1:
            source_data = re.split(' |\n', f1.read())

    if destination != "":
        with open(destination) as f2:
            destination_data = re.split(' |\n', f2.read())

    print(source_data)
    print(destination_data)


def create_srt_file(filename: str, outfile: str):
    """
    Creates a srt file & saves into disk with below format:
        1
        00:00:03,400 --> 00:00:06,177
        In this lesson, we're going to
        be talking about finance. And

        2
        00:00:06,177 --> 00:00:10,009
        one of the most important aspects
        of finance is interest.

    :param filename: name of the source json file
    :return: None
    """
    with open(f'.\\output\\{filename}') as f:
        data = f.read()
        content = json.loads(data)

    segments = content["segments"]

    index = 1
    for item in segments:
        # print(item)

        start_time = datetime.timedelta(seconds=item["start"])
        if "." in str(start_time):
            start, start_milli = str(start_time).split(".")
            final_start = start + "," + start_milli[:3]
        else:
            final_start = str(start_time) + ",000"

        end_time = datetime.timedelta(seconds=item["end"])
        if "." in str(end_time):
            end, end_milli = str(end_time).split(".")
            final_end = end + "," + end_milli[:3]
        else:
            final_end = str(end_time) + ",000"

        text = item["text"]

        with open(f'.\\output\\{outfile}', 'a', encoding='utf-8') as f:
            f.write(str(index) + "\n")
            f.writelines(f'{final_start} --> {final_end}' + "\n")
            f.writelines(text.strip() + "\n")
            f.writelines("\n")

        index += 1


if __name__ == "__main__":
    # compare_file("",".\\input\\test.txt")
    create_srt_file("Docker_Introduction.json", "Docker_Introduction.srt")
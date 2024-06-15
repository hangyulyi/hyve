'''
.srt files are formated like the following and this will parse according to that format.

1
00:00:00,340 --> 00:00:02,390
[subtitle here]

2
00:00:02,391 --> 00:00:04,116
[subtitle here]

...

'''

import re
import json

# TODO: Add append to a file instead of rewriting

'''
iterate through .srt file to record start time, end time, and text
'''
def parse_srt(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # REGEX for timestamp in srt files
    PATTERN = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n((?:.+\n?)+)')
    matches = PATTERN.findall(content)

    subtitles = []
    for match in matches:
        index, start_time, end_time, text = match
        text = text.strip()
        subtitles.append({
            'start_time': start_time,
            'end_time': end_time,
            'text': text
        })

    return subtitles

'''
Combines two different lists by comparing start_time
if they have the same start, then they are compiled into one
'''
def combine_subtitles(eng, kor):
    combined = []
    i, j = 0, 0

    while i < len(eng) and j < len(kor):
        eng_start = eng[i]['start_time']
        eng_end = eng[i]['end_time']
        kor_start = kor[j]['start_time']
        kor_end = kor[j]['end_time']

        if eng_start == kor_start and eng_end == kor_end:
            combined.append({
                'eng': eng[i]['text'],
                'kr': kor[j]['text']
            })
            i += 1
            j += 1
        elif eng_start < kor_start:
            i += 1
        else:
            j += 1

    return combined

def main():
    eng_srt = ''
    kor_srt = ''

    eng_sub = parse_srt(eng_srt)
    kor_sub = parse_srt(kor_srt)

    combined = combine_subtitles(eng_sub, kor_sub)

    file = 'data.json'

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
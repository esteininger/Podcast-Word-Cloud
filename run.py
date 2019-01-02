from transcriber import transcribe
import subprocess
import operator
import os
from tqdm import tqdm

file_output = 'podcast.mp3'
url = 'http://hwcdn.libsyn.com/p/6/1/f/61f9d221a13a5b75/p1220.mp3?c_id=29945528&cs_id=29945528&expiration=1545858570&hwt=282b299d3a000ad2ef5a9745c58b9e3c'
flac_folder = '/home/ethan/Desktop/Sandbox/podcast/files/flacs'
incr = '50'

def create_file(url, file_output):
    output = subprocess.check_output(['./scripts/converter.sh', url, file_output, incr])

def transcription_to_str(file, time_slot):
    transcription = transcribe(file_name=file)
    str_transcription = ''.join(transcription)
    d = '"{}", {}'.format(str_transcription, time_slot)
    return d

def get_word_count(str, time_slot):
    word_counts = dict()
    for word in str['str']:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=operator.itemgetter(1))
    d = {}
    d['time_slot'] = time_slot
    d['word_count'] = dict(sorted_words)

    return d

def write_to_file(input, output):
    f = open('{}.txt'.format(output), 'a')# just put 'w' if you want to write to the file
    f.write(str(input) + '\n')
    f.close()

if __name__ == "__main__":
    create_file(url=url, file_output=file_output)
    time_inter = 0
    directory_list = os.listdir(flac_folder)
    for file in tqdm(directory_list):
        try:
            transcription = transcription_to_str('{}/{}'.format(flac_folder,file), time_inter)
            write_to_file(input=transcription, output="./output/transcription_output")
        except Exception as e:
            print (e)
            pass

        time_inter += int(incr)

    #when finished
    subprocess.check_output(['./scripts/clear.sh'])

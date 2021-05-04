from transcriber import transcribe
from persister import persist
import datetime
import subprocess
import operator
import os
from tqdm import tqdm

file_output = 'podcast.mp3'
flac_folder = 'files/flacs'   #See scripts/converter.sh
incr = '10'
job_timestamp = datetime.datetime.now()

# Swap out different MP3 for testing (see samples.py). I should probably put these in a database :-)...
url = 'https://play.podtrac.com/510318/edge1.pod.npr.org/anon.npr-mp3/npr/upfirst/2021/04/20210428_upfirst_new_uf_042821.mp3'
trackback = 'https://www.npr.org/2021/04/25/990705794/nc-police-shooting-doj-investigates-louisville-police-cdc-mask-guidelines'
description = 'President Biden will make the case for his American Families Plan" to a joint session of Congress tonight, the White House says it will make the US economy more fair. Today, a court is considering whether to release body camera footage from the police killing of Black man last week in Elizabeth City, North Carolina. And, Michigan has the highest COVID-19 case rate in the country, some hospitals are overflowing with cases.'
title = "Up First"
episode = "Biden's American Families Plan, North Carolina Police Shooting, Michigan COVID Spike"
duration = "14:55"
episode_type = "podcast"
category = "News"


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

    # Store episode metadata
    # //persist_metadata(title=title, episode=episode, duration=duration, episode_type=episode_type, category=category, job_timestamp=job_timestamp)

    for file in tqdm(directory_list):
        # Let's just process 150 seconds for demo
        if time_inter <= 15000:
            try:
                transcription = transcription_to_str('{}/{}'.format(flac_folder,file), time_inter)
                # write_to_file(input=transcription, output="./output/transcription_output")
                persist(transcription=transcription, title=title, episode=episode, duration=duration, episode_type=episode_type, category=category, time_inter=time_inter, job_timestamp=job_timestamp)
            except Exception as e:
                print (e)
                pass

            time_inter += int(incr)

        

    #when finished
    subprocess.check_output(['./scripts/clear.sh'])

# Podcast Word Cloud
Podcast transcription for rich search.

## Technologies
* [Python 3](https://www.python.org/) 
* [wget](https://www.gnu.org/software/wget/)
* [FFmpeg](https://www.ffmpeg.org/)
* [Google Cloud Speech to Text](https://cloud.google.com/speech-to-text)
* [MongoDB Atlas Search](https://www.mongodb.com/atlas/search)

## Process Overview
This script uses [wget](https://www.gnu.org/software/wget/) to download a podcast from a URL you provide. [FFmpeg](https://www.ffmpeg.org/) is used to split the podcast into configureable time increments (e.g., 10 seconds). FFmpeg is also used to covert those framents to [FLAC](https://xiph.org/flac/) files for submission to [Google Cloud Speech to Text](https://cloud.google.com/speech-to-text) for processing. As the audio segments are transcribed, the results are saved to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).  

## Installation

This app requires Python 3+ v4+ to run, so install that first

1. Install the Python dependencies:

```python
pip install -r requirements.txt
```

2. [Create a Google Speech API key](https://cloud.google.com/speech-to-text/docs/reference/libraries#client-libraries-install-python)

3. Add the credentials as an environmental variable: 

```sh
$ export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

4. Add your MongoDB Atlas connection string and transcription database to `params.py`:

```python
# Atlas Connection String
atlas_conn_string = 'mongodb+srv://<username>:<password>@<host>/<transcription_database>?retryWrites=true&w=majority'
transcription_database = 'test'
```

5. Add the Podcast URL and metadata to run.py:
```python
# Swap out different MP3 for testing (see samples.py). I should probably put these in a database :-)...
url = 'https://play.podtrac.com/510318/edge1.pod.npr.org/anon.npr-mp3/npr/upfirst/2021/04/20210428_upfirst_new_uf_042821.mp3'
trackback = 'https://www.npr.org/2021/04/25/990705794/nc-police-shooting-doj-investigates-louisville-police-cdc-mask-guidelines'
description = 'President Biden will make the case for his American Families Plan" to a joint session of Congress tonight, the White House says it will make the US economy more fair. Today, a court is considering whether to release body camera footage from the police killing of Black man last week in Elizabeth City, North Carolina. And, Michigan has the highest COVID-19 case rate in the country, some hospitals are overflowing with cases.'
title = "Up First"
episode = "Biden's American Families Plan, North Carolina Police Shooting, Michigan COVID Spike"
duration = "14:55"
episode_type = "podcast"
category = "News"
```

5. Run:

```python
python run.py
```

6. Create a Search Index on the `speech` collection in the configured transcription_database.

## To Do
* Move the metadata to its own collection

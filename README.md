# Podcast-Word-Cloud
Podcast transcription

### Installation

This app requires Python 3+ v4+ to run, so install that first

1. Install the dependencies:

```python
$ pip install -r requirements.txt
```

2. [Create a Google Speech API key](https://cloud.google.com/speech-to-text/docs/reference/libraries#client-libraries-install-python)

3. Add the credentials as an environmental variable: 

```sh
$ export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

4. Change the variables in run.py:

file_output = 'NAME OF OUTPUT MP3 FILE'
url = 'DIRECT MP3 FILE OF PODCAST TO TRANSCRIBE'
flac_folder = 'WHERE YOU WANT TO SAVE YOUR FLACS'
incr = '50'

5. Run:

```python
$ python run.py
```

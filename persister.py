import params
from pymongo import MongoClient


# Establish connections to Atlas
mongo_client = MongoClient(params.atlas_conn_string)
transcription_db = mongo_client[params.transcription_database]

def persist(transcription, title, episode, duration, episode_type, category, time_inter, job_timestamp):
    id = title + "_" + episode + "_" + str(time_inter)
    record = {}
    record['_id'] = id
    record['transcription'] = transcription
    record['title'] = title
    record['episode'] = episode
    record['duration'] = duration
    record['type'] = episode_type
    record['category'] = category
    record['time_interval'] = time_inter
    record['job_timestamp'] = job_timestamp
    transcription_db.speech.update_one({'_id':id}, {"$set": record}, upsert=True)
    print("\nPersisted transcript to MongoDB\n")



    
    



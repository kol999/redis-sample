import redis
import os 

REDIS_URL_READER = os.environ.get('REDIS_URL_READER')
REDIS_URL_WRITER = os.environ.get('REDIS_URL_WRITER')
# redis_client = redis.Redis(host='localhost', port=6379, db=0) 
redis_writer= redis.Redis(host=REDIS_URL_WRITER, port=6379, db=0) 
redis_reader = redis.Redis(host=REDIS_URL_READER, port=6379)

for k in ['a','b','c','d','e','f','g']:
    assert redis_writer.get(k) == redis_reader.get(k) 

# print("This is a value %s" % str(redis_client.get('a')) )



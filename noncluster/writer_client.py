import redis
from random import randint 
# import sys

REDIS_URL_WRITER = os.environ.get('REDIS_URL_WRITER')
# redis_client = redis.Redis(host='localhost', port=6379, db=0) 
redis_writer = redis.Redis(host=REDIS_URL_WRITER, port=6379, db=0) 

# valueA=sys.argv[1]
for k in ['a','b','c','d','e','f','g']:
    value = randint(0,1000) 
    redis_writer.set(k, value)

# print("This is a value %s" % str(redis_client.get('a')) )




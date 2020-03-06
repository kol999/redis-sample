import os 
import redis
from random import randint


REDIS_URL = "redis-cluster.e1oqld.clustercfg.euw1.cache.amazonaws.com"

# redis_client = redis.Redis(host='localhost', port=6379, db=0) 
try: 
    redis_cluster= redis.Redis.from_url(REDIS_URL) 
except Exception as e:
    print("Error connecting to cluster:" + str(e)) 


for k in ['a','b','c','d','e','f','g' ]:
    value = randint(0,1000)
    try:
        redis_cluster.set(k, value) 
    except Exception as e:
        print("Error:" + str(e)) 

# print("This is a value %s" % str(redis_client.get('a')) )




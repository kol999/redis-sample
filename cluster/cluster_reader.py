import os 
import redis


REDIS_URL = "redis-cluster.e1oqld.clustercfg.euw1.cache.amazonaws.com"

# redis_client = redis.Redis(host='localhost', port=6379, db=0) 
try: 
    redis_cluster= redis.Redis.from_url(REDIS_URL) 
except Exception as e:
    print("Error connecting to cluster:" + str(e)) 


for k in ['a','b','c','d','e','f','g' ]:
    try:
        print(str(redis_cluster.get(k))) 
    except Exception as e:
        print("Error:" + str(e)) 





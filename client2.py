import redis

# redis_client = redis.Redis(host='localhost', port=6379, db=0) 
redis_writer= redis.Redis(host='redis-singlenode.e1oqld.ng.0001.euw1.cache.amazonaws.com', port=6379, db=0) 
redis_reader = redis.Redis(host='redis-singlenode-ro.e1oqld.ng.0001.euw1.cache.amazonaws.com', port=6379)

for k in ['a','b','c','d','e','f','g']:
    print(redis_reader.get(k))  
    # assert redis_writer.get(k) == redis_reader.get(k) 

# print("This is a value %s" % str(redis_client.get('a')) )



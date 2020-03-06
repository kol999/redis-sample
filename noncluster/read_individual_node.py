import redis

# redis_client = redis.Redis(host='localhost', port=6379, db=0) 
REDIS_URL_READER1 = os.environ.get('REDIS_URL_READER_NODE1')
REDIS_URL_READER2 = os.environ.get('REDIS_URL_READER_NODE2')


redis_node1 = redis.Redis(host=REDIS_URL_READER1, port=6379, db=0) 
redis_node2 = redis.Redis(host=REDIS_URL_READER2, port=6379, db-0) 
# redis_reader = redis.Redis(host='redis-singlenode-ro.e1oqld.ng.0001.euw1.cache.amazonaws.com', port=6379)

for k in ['a','b','c','d','e','f','g']:
    # print("This is the node %s" % str(redis_node1.get(k)))
    assert redis_node1.get(k) == redis_node2.get(k) 




import redis

if __name__ == '__main__':
    r = redis.Redis('redis')
    r.set('key', 'value')
    assert r.get('key') == 'value'
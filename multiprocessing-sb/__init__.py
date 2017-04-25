from multiprocessing.dummy import Pool as ThreadPool
from time import time

import requests

urls = [
    'https://www.google.com',
    'https://www.bing.com',
    'https://www.python.org',
    'https://github.com',
    'http://www.yahoo.com',
    'https://www.amazon.com',
    'https://en.wikipedia.org',
    'https://pypi.python.org/pypi/websocket-client',
    'https://www.postgresql.org/docs/9.6/static/app-createuser.html',
    'https://pymotw.com/2/threading/',
    'https://www.twilio.com',
    'https://www.tensorflow.org',
    'http://nd4j.org/',
    'http://www.twitter.com',
    'http://mixpanel.com',
    'https://stats.stackexchange.com',
    'https://trello.com'
]


if __name__ == '__main__':
    # single thread
    t0 = time()
    results = [requests.get(url) for url in urls]
    t1 = time()
    print(results)
    print('Took {} sec for {}'.format(t1 - t0, 'single thread'))

    # 2 threads
    t0 = time()
    pool = ThreadPool(2)  # Make pool of workers
    results = pool.map(requests.get, urls)  # Open each url in its own thread
    t1 = time()
    print('Took {} sec for {}'.format(t1 - t0, '2 threads'))
    pool.close()  # Close the pool
    pool.join()  # Wait for work to finish
    print('Pool joined. Done')

    # 4 threads
    t0 = time()
    pool = ThreadPool(4)  # Make pool of workers
    results = pool.map(requests.get, urls)  # Open each url in its own thread
    t1 = time()
    print('Took {} sec for {}'.format(t1 - t0, '4 threads'))
    pool.close()  # Close the pool
    pool.join()  # Wait for work to finish
    print('Pool joined. Done')

    # 8 threads
    t0 = time()
    pool = ThreadPool(8)  # Make pool of workers
    results = pool.map(requests.get, urls)  # Open each url in its own thread
    t1 = time()
    print('Took {} sec for {}'.format(t1 - t0, '8 threads'))
    pool.close()  # Close the pool
    pool.join()  # Wait for work to finish
    print('Pool joined. Done')

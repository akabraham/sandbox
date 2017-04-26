from multiprocessing.dummy import Pool as ThreadPool
from timeit import default_timer as timer

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
    print('Starting single thread ...')
    t0 = timer()
    results = [requests.get(url) for url in urls]
    t1 = timer()
    print(results)
    print('Took {} sec for single thread'.format(t1 - t0))

    # 2 threads
    print('Starting 2 threads ...')
    t0 = timer()
    pool = ThreadPool(2)  # Make pool of workers
    results = pool.map(requests.get, urls)  # Open each url in its own thread
    pool.close()  # Close the pool
    pool.join()  # Wait for work to finish
    t1 = timer()
    print('Took {} sec for 2 threads'.format(t1 - t0))

    # 4 threads
    print('Starting 4 threads ...')
    t0 = timer()
    pool = ThreadPool(4)
    results = pool.map(requests.get, urls)
    pool.close()
    pool.join()
    t1 = timer()
    print('Took {} sec for 4 threads'.format(t1 - t0))

    # 8 threads
    print('Starting 8 threads ...')
    t0 = timer()
    pool = ThreadPool(8)
    results = pool.map(requests.get, urls)
    pool.close()
    pool.join()
    t1 = timer()
    print('Took {} sec for 8 threads'.format(t1 - t0))

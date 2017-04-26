from datetime import datetime, timedelta

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError


INDEX = 'test-index'

es = Elasticsearch(hosts=['localhost:9200'])

docs = [{
    'author': 'Stephen Hawking',
    'text': 'A Brief History of Time Travel',
    'timestamp': datetime.now()
}, {
    'author': 'Dr. Seuss',
    'text': 'The Cat in the Hat',
    'timestamp': datetime.now() - timedelta(hours=1)
}, {
    'author': 'Dan Brown',
    'text': 'The DaVinci Code',
    'timestamp': datetime.now() - timedelta(hours=3)
}]


if __name__ == '__main__':
    try:
        es.indices.delete(INDEX)
        print('Deleting index ...')
    except NotFoundError:
        print('Index not found. Skipping')
        pass

    print('Building index ...')
    for i, doc in enumerate(docs):
        rv = es.index(index=INDEX, doc_type='tweet', id=i+1, body=doc)
        print(rv)

    print('Index built')

    # rv = es.get(index=INDEX, doc_type='tweet', id=1)

    es.indices.refresh(index=INDEX)
    print('Index refreshed')

    # q = {
    #     'match_all': {
    #         'boost': 1.2
    #     }
    # }

    # q = {
    #     'match_none': {}
    # }

    q = {
        'match': {
            'text': 'the'
        }
    }

    print('-----------------------')
    print('Query: {}'.format(q))

    rv = es.search(index=INDEX, body={'query': q})
    print('Raw Results: {}'.format(rv))
    print('Got {} hit(s)'.format(rv['hits']['total']))

    for hit in rv['hits']['hits']:
        print('Score: {} for source {}'.format(hit['_score'], hit['_source']))

import os

import boto3


# ENDPOINT = 'https://runtime.lex.us-east-1.amazonaws.com/'
AUDIO_FPATH = \
    '/Users/andrewabraham/projects/task-stick/task_stick/tests/assets/audio.wav'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_REGION_NAME = 'us-east-1'

client = boto3.client(
    'lex-runtime',
    region_name=AWS_REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def post():
    with open(AUDIO_FPATH, 'rb') as f:
        client.post_content(
            botName='test',
            botAlias='test',
            userId='TODO:developerId',
            contentType='audio/l16; rate=16000; channels=1',
            accept='text/plain; charset=utf-8',
            inputStream=f
        )


if __name__ == '__main__':
    post()

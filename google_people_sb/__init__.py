import httplib2
import os

from googleapiclient.discovery import build
from oauth2client.file import Storage
from oauth2client import client
from oauth2client.tools import run_flow


def people_auth():
    """Handles Google OAuth2 process and initiates people service.
    
    :returns: people service
    """
    # Set up a Flow object to be used if we need to authenticate. This
    # sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
    # the information it needs to authenticate. Note that it is called
    # the Web Server Flow, but it can also handle the flow for
    # installed applications.
    #
    # Go to the Google API Console, open your application's
    # credentials page, and copy the client ID and client secret.
    # Then paste them into the following code.
    flow = client.OAuth2WebServerFlow(
        client_id=os.environ['GOOGLE_CLIENT_ID'],
        client_secret=os.environ['GOOGLE_CLIENT_SECRET'],
        scope='https://www.googleapis.com/auth/contacts.readonly',
        user_agent='My Project/0.1',
        redirect_uri=client.OOB_CALLBACK_URN
    )

    # If the Credentials don't exist or are invalid, run through the
    # installed application flow. The Storage object will ensure that,
    # if successful, the good Credentials will get written back to a
    # file.
    storage = Storage('credentials.json')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)

    # Create an httplib2.Http object to handle our HTTP requests and
    # authorize it with our good Credentials.
    http = httplib2.Http()
    http = credentials.authorize(http)

    # Build a service object for interacting with the API. To get an API key for
    # your application, visit the Google API Console
    # and look at your application's credentials page.
    people_service = build(serviceName='people', version='v1', http=http)
    return people_service


if __name__ == '__main__':
    service = people_auth()
    req = service.people().connections().list(resourceName='people/me')
    contacts = req.execute()
    print(contacts)

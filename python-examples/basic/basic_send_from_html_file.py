import json
import os

from socketlabs.injectionapi import SocketLabsClient
from socketlabs.injectionapi.message.__imports__ import \
    BasicMessage, EmailAddress


# build the message
message = BasicMessage()

message.subject = "Sending An Email With Body From Html File"

with open("../html/SimpleEmail.html", 'rb') as f:
    data = f.read()
    f.close()
message.html_body = data.decode('UTF-8')

message.from_email_address = EmailAddress("from@example.com")
message.add_to_email_address("recipient@example.com")


# get credentials from environment variables
server_id = int(os.environ.get('SOCKETLABS_SERVER_ID'))
api_key = os.environ.get('SOCKETLABS_INJECTION_API_KEY')

# create the client
client = SocketLabsClient(server_id, api_key)

# send the message
response = client.send(message)

print(json.dumps(response.to_json(), indent=2))

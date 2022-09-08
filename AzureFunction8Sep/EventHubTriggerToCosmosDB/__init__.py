import logging

import azure.functions as func
from typing import List


# def main(event: func.EventHubEvent):
#     logging.info('Python EventHub trigger processed an event: %s',
#                  event.get_body().decode('utf-8'))
def main(events: List[func.EventHubEvent],
         outputDocument: func.Out[func.Document]):

    for event in events:
        json_data = event.get_body()
        outputDocument.set(func.Document.from_json(json_data))

        logging.info("Event has been written to tweets in CosmosDB")
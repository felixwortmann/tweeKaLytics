# tweeKaLytics
Twitter Analytics with Kafka

## Run
- Apply for the Twitter API
  - Put the API Key in api_request/api_key.txt
  - Put the API Key secret in api_request/api_key_secret.txt
  - Put the Bearer Token in api_request/bearer_token.txt
  - Put the Access Token Secret in api_request/access_token_secret.txt
  - Put the Access Token in api_request/access_token.txt
- `docker-compose up --build`

| Directory      | Function                                                     |
| -------------- | ------------------------------------------------------------ |
| api_request    | Python Code to request data from the Twitter API             |
| middleware     | Python Code to Consume Data from Kafka and put it into Mongo |
| visualize_data | Jupyter Notebook to Visualize the Data                       |

## Services
- kafka-service-tweekalytics
- mongo-service-tweekalytics
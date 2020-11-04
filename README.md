# tweeKaLytics
Twitter Analytics with Kafka

## Run
- Apply for the Twitter API
  - Put the API Key in api_request/keys/api_key
  - Put the API Key secret in api_request/keys/api_key_secret
  - Put the Bearer Token in api_request/keys/bearer_token
- `docker-compose up --build`

| Directory      | Function                                                     |
| -------------- | ------------------------------------------------------------ |
| api_request    | Python Code to request data from the Twitter API             |
| middleware     | Python Code to Consume Data from Kafka and put it into Mongo |
| visualize_data | Jupyter Notebook to Visualize the Data                       |

## Services
- kafka-service-tweekalytics
- mongo-service-tweekalytics
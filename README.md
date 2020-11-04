# tweeKaLytics
Twitter Analytics with Kafka

## Run
`docker-compose up --build`
<!-- ### Setup
- Run `pip3 install -r requirements.txt`
- Run `mkdir keys`
- Apply for the Twitter API
  - Put the API Key in keys/api_key
  - Put the API Key secret in keys/api_key_secret
  - Put the Bearer Token in keys/bearer_token -->

| Directory      | Function                                                     |
| -------------- | ------------------------------------------------------------ |
| api_request    | Python Code to request data from the Twitter API             |
| middleware     | Python Code to Consume Data from Kafka and put it into Mongo |
| visualize_data | Jupyter Notebook to Visualize the Data                       |

## Services
- kafka-service-tweekalytics
- mongo-service-tweekalytics
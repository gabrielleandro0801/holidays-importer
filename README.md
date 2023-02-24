# Holidays Importer :calendar: :brazil:

AWS Lambda Function to import Febraban holidays from API **[Brasil API](https://brasilapi.com.br/docs#tag/Brasil-API)** and save them in a DynamoDB table using **Localstack**.

## Setup
1. In order to run Localstack, you will need to have *Docker* installed in your machine. 
You can follow this [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-pt) to install.
2. Then, you will need to install Localstack itself. 
This [link](https://github.com/localstack/localstack) may help you.
3. After this, you should install *awscli-local* by following this [link](https://pypi.org/project/awscli-local/) or just running this command:
``` shell
pip3 install awscli-local
```

## Running :computer:
1. Start Localstack
``` shell
LAMBDA_REMOTE_DOCKER=0 DEBUG=1 localstack start
```

2. Install the dependencies to the lambda
``` shell
pip3 install -r requirements.txt -t .
```

3. Zip your code and create an artifact
``` shell
 zip -qr my_zip.zip .
```

4. Create the Lambda Function
``` shell
awslocal lambda create-function --function-name holidays_importer \
    --code S3Bucket="__local__",S3Key="$(pwd)" \
    --handler src/entrypoint/handler.main \
    --runtime python3.8 \
    --role bla \
    --zip-file fileb://my_zip.zip
```

5. Create the DynamoDB table
``` shell
awslocal dynamodb create-table --table-name my_holidays \
    --attribute-definitions AttributeName=date,AttributeType=S \
    --key-schema AttributeName=date,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST
```

6. Invoke the lambda function
``` shell
awslocal lambda invoke --function-name holidays_importer --payload '{}' output.txt
```
or
``` shell
awslocal lambda invoke --function-name holidays_importer --payload '{"year": 2021}' output.txt
```

7. Scan the DynamoDB table
``` shell
awslocal dynamodb scan --table-name my_holidays
```

If the scan command returns some holidays, congrats, the execution went well! :smile:

If you need to delete the lambda function for any reason:
``` shell
awslocal lambda delete-function --function-name holidays_importer
```

## Running Unit Tests :computer:
``` shell
coverage run -m unittest
```
or, if you want to see the report
``` shell
coverage run -m unittest && coverage report
```
or, if you want to see the HTML report
``` shell
coverage run -m unittest && coverage html
```

### Acknowledgments :clap:
Those links below helped me during the development.

- [link 1](https://www.rtancman.com.br/python/aws/organizando-aws-lambda-escrito-python.html)
- [link 2](https://python.plainenglish.io/a-quick-intro-to-to-test-coverage-in-python-9bf299711c6c)
- [link 3](https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory)

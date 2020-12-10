import json

#def lambda_handler():
def lambda_handler(event, context):
    print('run:\n')
    return {
        'statusCode': 200,
        'body': json.dumps('hello')
    }
#print (lambda_handler())

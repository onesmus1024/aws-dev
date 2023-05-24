import boto3


class DynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.available_tables = self._get_all_tables_names()


    def _get_all_tables_names(self):
        return [table.name for table in self.dynamodb.tables.all()]
    
    def list_tables(self):
        for table in self.dynamodb.tables.all():
            print(table.name)

    def create_table(self, table_name):
        try:
            if table_name in self._get_all_tables_names():
                print('Table already exists')
                return
            self.dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
        except Exception as e:
            raise e
        

    def delete_table(self, table_name):
        try:
            if table_name not in self._get_all_tables_names():
                print('Table does not exist')
                return
            self.dynamodb.Table(table_name).delete()
        except Exception as e:
            raise e
        

    def insert_item(self, table_name, item):
        try:
            if table_name not in self._get_all_tables_names():
                print('Table does not exist')
                return
            self.dynamodb.Table(table_name).put_item(Item=item)
        except Exception as e:
            raise e
        

    def get_item(self, table_name, item_id):
        try:
            if table_name not in self._get_all_tables_names():
                print('Table does not exist')
                return
            return self.dynamodb.Table(table_name).get_item(Key={'id': item_id})
        except Exception as e:
            raise e

    def delete_item(self, table_name, item_id):
        try:
            if table_name not in self._get_all_tables_names():
                print('Table does not exist')
                return
            self.dynamodb.Table(table_name).delete_item(Key={'id': item_id})
        except Exception as e:
            raise e
        
    def list_items(self, table_name):
        try:
            if table_name not in self._get_all_tables_names():
                print('Table does not exist')
                return
            return self.dynamodb.Table(table_name).scan()['Items']
        except Exception as e:
            raise e
        
    def update_item(self, table_name, item_id, update_expression, expression_attribute_values):
        try:
            if table_name not in self._get_all_tables_names():
                print('Table does not exist')
                return
            self.dynamodb.Table(table_name).update_item(
                Key={'id': item_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
        except Exception as e:
            raise e
    def query_items(self, table_name, key_condition_expression, expression_attribute_values):
        try:
            if table_name not in self._get_all_tables_names():
                print('Table does not exist')
                return
            return self.dynamodb.Table(table_name).query(
                KeyConditionExpression=key_condition_expression,
                ExpressionAttributeValues=expression_attribute_values
            )['Items']
        except Exception as e:
            raise e

if __name__ == '__main__':

    try:

        dynamoDB = DynamoDB()

        print('List tables')
        dynamoDB.list_tables()

        print('='*50)
        print('Create table')
        dynamoDB.create_table('test_table')

        print('='*50)
        print('List tables')
        dynamoDB.list_tables()

        print('='*50)
        print('delete table')
        dynamoDB.delete_table('test_table')

        print('='*50)
        print('List tables')
        dynamoDB.list_tables()


    except Exception as e:

        print('Something went wrong')
        print(e)

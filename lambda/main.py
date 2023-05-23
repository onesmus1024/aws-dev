import boto3




class Lambda:

    def __init__(self):
        self.lambda_client = boto3.client('lambda')
        self.available_functions = self._get_all_functions_names()
    
    # get all lambda functions
    def _get_all_functions_names(self):
        return [function['FunctionName'] for function in self.lambda_client.list_functions()['Functions']]
    
    











if __name__ == '__main__':
    lambda_handle = Lambda()

    print(lambda_handle.available_functions)

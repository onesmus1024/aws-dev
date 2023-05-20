import boto3


class SQS:

    def __init__(self):
        self.sqs = boto3.resource('sqs')

    def create_queue(self, queue_name):
        self.sqs.create_queue(QueueName=queue_name)
    
    def delete_queue(self, queue_name):
        self.sqs.get_queue_by_name(QueueName=queue_name).delete()

    def list_queues(self):
        for queue in self.sqs.queues.all():
            print("Queue URL: {0}".format(queue.url))
    
    def send_message(self, queue_name, message):
        self.sqs.get_queue_by_name(QueueName=queue_name).send_message(MessageBody=message)

    def receive_messages(self, queue_name):
        for message in self.sqs.get_queue_by_name(QueueName=queue_name).receive_messages():
            print(message.body)
            message.delete()
    


if __name__ == '__main__':
    sqs = SQS()
    sqs.list_queues()
    print('='*50)
    print('Creating queue')
    sqs.create_queue('my-queue')
    print('='*50)
    print('Listing queues after creating queue')
    sqs.list_queues()
    print('='*50)
    print('Sending message to queue')
    sqs.send_message('my-queue', 'Hello World')
    print('='*50)
    print('Receiving message from queue')
    sqs.receive_messages('my-queue')
    print('='*50)
    print('Deleting queue')
    sqs.delete_queue('my-queue')
    print('='*50)
    print('Listing queues after deleting queue')
    sqs.list_queues()
    print('='*50)
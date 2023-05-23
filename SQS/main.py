import boto3


class SQS:
    def __init__(self):
        self.sqs = boto3.resource('sqs')
        self.available_queues = self._get_all_queues_names()

    def _get_all_queues_names(self):
        return [queue.url.split('/')[-1] for queue in self.sqs.queues.all()]

    def create_queue(self, queue_name):
        try:
            if queue_name in self.available_queues:
                print('Queue already exists')
                return
            self.sqs.create_queue(QueueName=queue_name)
        except Exception as e:
            print("Error creating queue:", str(e))

    def delete_queue(self, queue_name):
        try:
            if queue_name not in self.available_queues:
                print('Queue does not exist')
                return
            self.sqs.get_queue_by_name(QueueName=queue_name).delete()
        except Exception as e:
            print("Error deleting queue:", str(e))

    def list_queues(self):
        try:

            for queue in self.sqs.queues.all():
                print("Queue URL: {0}".format(queue.url))
                print("Queue Name: {0}".format(queue.url.split('/')[-1]))
                print("Queue ARN: {0}".format(
                    queue.attributes.get('QueueArn')))
                print("Queue Approximate Number of Messages: {0}".format(
                    queue.attributes.get('ApproximateNumberOfMessages')))

                print("="*50)
        except Exception as e:
            print("Error listing queues:", str(e))

    def message_formated(self, message, queue_name):
        print("Queue Name: {0}".format(queue_name))
        print("Message Body: {0}".format(message.body))
        print("Message ID: {0}".format(message.message_id))
        # delete the message
        message.delete()

        print("="*50)

    def send_message(self, queue_name, message):
        try:
            if queue_name not in self.available_queues:
                print('Queue does not exist')
                return
            self.sqs.get_queue_by_name(
                QueueName=queue_name).send_message(MessageBody=message)
        except Exception as e:
            print("Error sending message:", str(e))

    def receive_messages(self, queue_name=None):
        # get messages from available queues
        try:
            if queue_name is None:
                # get messages from available queues
                for queue_name in self.available_queues:
                    queue = self.sqs.get_queue_by_name(QueueName=queue_name)
                    while True:
                        try:
                            message = queue.receive_messages()
                            massage_id = message[0].message_id
                            self.message_formated(message[0], queue_name)
                        except Exception as e:
                            break
            else:
                # get messages from a specific queue
                queue = self.sqs.get_queue_by_name(QueueName=queue_name)
                while True:
                    try:
                        message = queue.receive_messages()
                        massage_id = message[0].message_id
                        self.message_formated(message[0], queue_name)
                    except Exception as e:
                        break
        except Exception as e:
            print("Error receiving messages:", str(e))


if __name__ == '__main__':
    sqs = SQS()

    # sqs.send_message('onesmus_program_queue', 'Hello test')
    # sqs.send_message('onesmus_program_queue', 'Hello World')
    # # get messages from onesmus_program_queue
    sqs.receive_messages('onesmus_program_queue')

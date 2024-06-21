import json


class JSON:
    with open('test_data.json', 'r') as json_file:
        credentials = json.load(json_file)

    @staticmethod
    def get_credentials(cred):
        return JSON.credentials[cred]

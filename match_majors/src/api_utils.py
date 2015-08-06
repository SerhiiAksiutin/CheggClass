import requests
import json
import os
from ConfigParser import SafeConfigParser


class Config:
    def __init__(self):
        self.parser = SafeConfigParser()
        if os.path.isfile('config.ini'):
            self.parser.read('config.ini')
        else:
            print('No config.ini file found under root folder.')
        self.domain = self.parser.get('Server', 'domain')
        self.endpoint = self.parser.get('Server', 'endpoint')
        self.test_path = self.parser.get('Server', 'test_path')
        self.method = self.parser.get('Server', 'method')


class Response:
    def __init__(self):
        self.http_code = 0
        self.body = dict()
        self.headers = dict()


class Calls:
    def __init__(self):
        self.config = Config()
        self.no_json = 'noJson'

    def match_majors(self, majorIds, schoolid, domain=None, endpoint=None,
                     test_path=None, content_type=None, accept=None,
                     method=None):
        if domain is None:
            domain = self.config.domain
        if endpoint is None:
            endpoint = self.config.endpoint
        if test_path is None:
            test_path = self.config.test_path
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if method is None:
            method = self.config.method

        url = domain + endpoint + schoolid + test_path
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept
        data = dict()
        data['majorIds'] = [majorIds]
        data = json.dumps(data)
        r = requests.request(
          url=url,
          headers=headers,
          data=data,
          method=method
          )

        try:
            json_resp = json.loads(r.content)
        except ValueError:
            if method == 'OPTIONS':
                json_resp = r.content
            else:
                json_resp = self.no_json

        r.json = json_resp
        print('\n' + ''.join(
            r.json['result']['matchedMajors']) + '\n' + majorIds)

        if ''.join(r.json['result']['matchedMajors']) == majorIds:
            print('Pass - Match')
        else:
            print('Pass - Not a Match')

        response = Response()
        response.http_code = r.status_code
        response.body = r.json
        response.headers = r.headers
        print('\n' + str(response.http_code))
        return response
        print(response.body)

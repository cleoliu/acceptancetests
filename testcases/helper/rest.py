import requests
import json as JSON


def check_operation_http_status(status, expected_status):
    if status not in expected_status:
        raise RuntimeError('Failed to operation resource by rest')


class rest:
    API_PREFIX = 'uHutt'
    endpoint = ''
    port = 9966
    is_https = False

    methods = {
        "get": None,
        "post": None,
        "put": None,
        "del": None
    }

    headers = {'Content-Type': 'application/json'}

    def __init__(self, endpoint, user, password):
        self.endpoint = endpoint
        self.user = user
        self.password = password
        self.methods["get"] = self._get
        self.methods["post"] = self._post
        self.methods["put"] = self._put
        self.methods["del"] = self._delete

        self.path = ''
        self.url = ''

        self.create_session()

    def create_session(self):
        try:
            _, resp = self.account.connect.post(json={
                "email": self.user, "password": self.password, "ccap": "captcha"
            })
            self.user_id = resp['result']['user_id']
            self.sign = resp['result']['sign']
            self.headers['user-id'] = self.user_id
            self.headers['sign'] = self.sign
        except Exception as e:
            print e
            raise RuntimeError("Failed to connected server by rest")

    def __getattr__(self, item):
        if item not in self.methods.keys():
            self.path += "{}/".format(item)
            return self
        # remove the last '/' character
        self.url = self._get_base_url() + self.path[:-1]
        self.path = ''
        return self.methods[item]

    def _get(self, id=None, params=None):
        url = "{}/{}".format(self.url, id) if id else self.url
        print("GET {}, params={}".format(url, params))
        resp = requests.get(url=url, headers=self.headers, params=params)
        return rest._pack_response(resp)

    def _post(self, params=None, json=None, data=None):
        print("POST {}, params={}".format(self.url, params))
        resp = requests.post(url=self.url, headers=self.headers, params=params, json=json) if json else \
            requests.post(url=self.url, headers=self.headers,
                          params=params, data=data)
        return rest._pack_response(resp)

    def _put(self, params=None, json=None, data=None):
        print("PUT {}, params={}".format(self.url, params))
        resp = requests.put(url=self.url, headers=self.headers, params=params, json=json) if json else \
            requests.put(url=self.url, headers=self.headers,
                         params=params, data=data)
        return rest._pack_response(resp)

    def _delete(self, id, params=None):
        url = "{}/{}".format(self.url, id)
        print("DELETE {}, params={}".format(url, params))
        resp = requests.delete(url=url, headers=self.headers, params=params)
        return rest._pack_response(resp)

    def _get_base_url(self):
        return "{}://{}:{}/{}/".format('https' if self.is_https else 'http',
                                       self.endpoint,
                                       self.port,
                                       self.API_PREFIX)

    @staticmethod
    def _pack_response(resp):
        try:
            resp_json = JSON.loads(resp.text)
            if resp_json['success']:
                return resp.status_code, resp_json

            return resp.status_code, {
                'success': False,
                'message': rest._compose_error_message(resp_json)
            }
        except ValueError as err:
            return resp.status_code, {
                'success': False,
                'message': "Unable to parse to JSON format: {}".format(resp.text)
            }
        except Exception as e:
            return resp.status_code, {
                'success': False,
                'message': "Unexpected error: {}".format(e)
            }

    @staticmethod
    def _compose_error_message(resp_json):
        return "{}({}): {}".format(resp_json['errorType'], resp_json['errorCode'], resp_json['message'])

    def delete_cowork(self, cowork_name):
        status, resp = self.desktop.get()
        check_operation_http_status(status, [requests.codes.ok])
        desktop_id = resp['result']['dataArr'][0]['matter_id']

        status, resp = self.desktop.tier.post(
            json={'desktop_id': desktop_id})
        check_operation_http_status(status, [requests.codes.ok])

        for matter in resp['result']['dataArr']:
            if matter['title'] == cowork_name and matter['ref_content_type'] == 'work':
                matter_id = matter['matter_id']
                break
        else:
            raise RuntimeError(
                'Failed to find cowork by name %s' % cowork_name)

        status, resp = self.linker.delete.get(id=matter_id)
        check_operation_http_status(status, [requests.codes.ok])

        status, resp = self.linker.drop.get(id=matter_id)
        check_operation_http_status(status, [requests.codes.ok])

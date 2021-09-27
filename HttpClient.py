import requests as requests


class HttpClient:

    def __init__(self, url):
        self.__session = requests.Session()
        self.__url = url

    def __del__(self):
        self.__session.close()

    def set_header(self, header):
        self.__session.headers.update(header)

    def get(self, path, query):
        request = self.__session.get('{0}{1}'.format(self.__url, path), params=query)
        return request if request.status_code == requests.codes.ok else None

    def post(self, path, query):
        request = self.__session.post('{0}{1}'.format(self.__url, path), params=query)
        return request if request.status_code == requests.codes.ok else None
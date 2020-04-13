import requests

class Requester:
    def __init__(self):
        self.CHUNK_SIZE = 8192
        self.timeout = 20

    def get(self, url, headers=None, cookies=None, timeout=None):
        timeout = timeout if timeout else self.timeout
        return requests.get(url, headers=headers, cookies=cookies, timeout=timeout)

    def get_response(self, *args, **kwargs):
        return self.get(*args, **kwargs).text

    def get_file(self, url, headers=None, cookies=None, dir=None, file=None, callback=None):
        file = file if file else self.convert_url_to_file(url)
        file = dir + file if dir else file

        with requests.get(url, stream=True, headers=headers, cookies=cookies) as response:
            total_length = response.headers.get('content-length')
            total_length, dl = int(total_length) if total_length else 1, 0

            with open(file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=self.CHUNK_SIZE):
                    dl += len(chunk)
                    percent = dl / total_length

                    if callback:
                        callback(percent)

                    if chunk:
                        f.write(chunk)
        return file

    @staticmethod
    def convert_url_to_file(url):
        return url.split('/')[-1]

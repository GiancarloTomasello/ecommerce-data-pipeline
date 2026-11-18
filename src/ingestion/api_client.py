from requests import Request,Session, exceptions

class ApiClient:
    s = None

    def __init__(self):
        self.s = Session()

    def call_request(self, ReqType="Get", url="", timeoutTime = 10):
        req = Request(ReqType, url)
        prepped = self.s.prepare_request(req)
        settings = self.s.merge_environment_settings(prepped.url, {}, None, None, None)
        try:
            resp = self.s.send(prepped, **settings, timeout=timeoutTime)
            resp.raise_for_status()
            return resp
        except exceptions.Timeout:
            print("The request has times out")
        except exceptions.ConnectionError:
            print("Nettwork problem (possible DNS failure)")
        except exceptions.HTTPError as err:
            status = err.response.status_code
            if status in (401,403):
                print("Authetication or permission error")
            elif status == 404:
                    print("Resource not found. Try checking the url")
            elif status >= 500:
                print(f"Server error ({status}). Try again later")
            else:
                print(f"HTTP error occured: {err}")





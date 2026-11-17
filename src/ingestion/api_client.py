from requests import Request,Session, exceptions

class ApiClient:
    s = Session()

    def call_request(self, ReqType="Get", url="", timeoutTime = 10):
        req = Request(ReqType, url)
        prepped = self.s.prepare_request(req)
        settings = self.s.merge_environment_settings(prepped.url, {}, None, None, None)
        try:
            resp = self.s.send(prepped, **settings, timeout=timeoutTime)
        except TimeoutError:
            print("The request has times out")
        except ConnectionError:
            print("Nettwork problem (possible DNS failure)")
        except exceptions.HTTPError as err:
            print(f"HTTP error occured: {err}")
        return resp.json()





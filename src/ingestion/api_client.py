from requests import Request,Session, exceptions
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
import logging
import json

class ApiClient:
    s = None
    logger = None

    def __init__(self):
        self.s = Session()
        retries = Retry(
            total=3,
            backoff_factor=0.1,
            status_forcelist=[502,503,504],
            allowed_methods={'GET'},
        )
        self.s.mount('https://', HTTPAdapter(max_retries=retries))

        self.logger = logging.getLogger('ApiClient_Logger')
        logging.basicConfig(format='%(levelname)s:%(message)s',filename='ApiClient.log', filemode='w', level=logging.DEBUG)
        self.logger.info('Started')

    def call_request(self, ReqType="Get", url="", limit=30, skip=0,timeoutTime = 10):

        req = Request(ReqType, url, params={"limit":limit, "skip":skip})
        prepped = self.s.prepare_request(req)
        print(prepped.url)

        settings = self.s.merge_environment_settings(prepped.url, {}, None, None, None)
        try:
            self.logger.info(f"Request was sent out to url {prepped.url}")
            resp = self.s.send(prepped, **settings, timeout=timeoutTime)
            resp.raise_for_status()
            return resp.json()
        except exceptions.Timeout:
            self.logger.warning("The request has times out")
            #try again?
        except exceptions.ConnectionError:
            self.logger.error("Network problem (possible DNS failure)")
        except exceptions.HTTPError as err:
            status = err.response.status_code
            error_return = {"Error": err.response.status_code}
            if status in (401,403):
                self.logger.warning("Authetication or permission error")
                return 
            elif status == 404:
                self.logger.warning(f"Status code {status}: Resource is not found. Check the url for improper formating")
            elif status >= 500:
                self.logger.warning(f"Server error ({status}). Try again later")
            else:
                self.logger.error(f"HTTP error occured: {err}")

            return json.dumps(error_return)





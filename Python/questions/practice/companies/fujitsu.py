"""

Develop an application which will do third party api call

1. API calls are expensive
2. Unpredicatble latency
3. Third party api are not reliable



1. I will do store duplicate respose and invalidate it when it changes at third party
2. I will create a provision to wait for response form third party in a dynamic way and 
   there should be a threshold for that wait_period. 
3. We should keep backup or alternative for third party apis . And if one is down we should
   call alternate provider .
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

class APIProvider(ABC):
    @abstractmethod
    def get(self, url, api_key):
        pass
    
class API1(APIProvider):
        - url
    def get(self,api_key)
         rest.get(self.url, api)

class API2(APIProvider):
     - url
    def get(self, url, api_key)
         rest.get(self.url, api)

@dataclass
class Response:
    - response: dict
    - last_invalidated: timestamp

@dataclass
class ResponseStore:
    - store: dict["api_name": response]


class APIFactory:
    def __self__(self):
        self.apis = {
            "api_name": API1,
            "api_name": API2,
        }
    def get():

class ThirdPartyAPIManager:
    def __init__(self, store, ResponseStore):
        factory = APIFactory
        
    def get(self, api_name):
        api_prodiver = factory.get(api)
        resp = api_proivder.get()
        
    
    


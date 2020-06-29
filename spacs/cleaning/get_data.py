import pandas as pd
import requests
from bs4 import BeautifulSoup

class DataRetreiver:

    def __init__(self, types='all'):
        self._base_url='https://www.earlybirdcapital.com/spac-transactions/'
        types_dict={'ipos':'completed-spac-ipos','mergers':'completed-spac-mergers',
                'targets':'spacs-currently-seeking-targets'}
        if types=='all':
            keep_keys=list(types_dict.keys())
        elif types=='completed':
            keep_keys=['ipos','mergers']
        elif types=='targets':
            keep_keys=['targets']
        elif types=='mergers':
            keep_keys=['mergers']
        elif types=='ipos':
            keep_keys=['ipos']
        urls=dict()
        for i in keep_keys:
            urls[i]=self._base_url+types_dict[i]
        self._urls=urls

    def _get_spacs(self):
        content=dict()
        for data_source,url in self._urls.items():
            g=requests.get(url)
            content[data_source]=g.content
        self._content=content
    
    def _parse_mergers(self,content):
        s=BeautifulSoup(content)
        spac_title=s.find('h5',attrs={'class':'company-listing-title'}).text
        # get merger target
        # get role
        # get value
        # get merger date
    
    def _parse_ipos(self, content):
        pass
    
    def _parse_targets(self, content):
        pass

    def _parse_spacs(self):
        parsed=dict()
        for data_source,content in self._content.items():
            if data_source=='mergers':
                parsed[data_source]=self._parse_mergers(content)

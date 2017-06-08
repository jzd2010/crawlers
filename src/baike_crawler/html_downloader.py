# coding:utf-8
'''
Created on 2017-6-7

@author: jzd
'''
import urllib2


class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
    
    




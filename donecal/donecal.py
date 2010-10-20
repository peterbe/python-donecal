# -*- coding: utf-8 -*

from time import mktime
import datetime
import anyjson
import urllib2
from urllib import urlencode

BASE_URL = 'http://donecal.com'

class ConnectionError(Exception):
    pass

class AuthorizationError(Exception):
    pass

class DoneCal(object):
    def __init__(self, guid, base_url=BASE_URL):
        self.guid = guid
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        self.base_url = base_url
        
    
    def add_event(self, title, date=None, start=None, end=None, 
                  all_day=None, url=None):
        """return a tuple of the event (as a dict) and whether the event was
        actually created (as opposed to found as a duplicate)"""
        
        if date is not None:
            if not isinstance(date, (datetime.date, datetime.datetime)):
                raise ValueError("date must be a datetime.date or "\
                                 "datetime.datetime instance")
        elif not (start or end):
            date = datetime.date.today()
        else:
            if not (start and end) and (start or end):
                raise ValueError("If not using date, "\
                                 "specify both start and end")
            if not isinstance(start, (datetime.date, datetime.datetime)):
                raise ValueError("start must be a datetime.date or "\
                                 "datetime.datetime instance")
            if not isinstance(end, (datetime.date, datetime.datetime)):
                raise ValueError("end must be a datetime.date or "\
                                 "datetime.datetime instance")
                                 
        return self._add_event(title, date, start, end, all_day, url=url)

                
    def _add_event(self, title, date, start, end, all_day, url=None):
        if isinstance(title, unicode):
            title = title.encode('utf8')
        values = dict(title=title,
                      all_day=all_day and 'true' or 'false',
                      guid=self.guid,
                      )
        if date:
            values['date'] = mktime(date.timetuple())
        else:
            values['start'] = mktime(start.timetuple())
            values['end'] = mktime(end.timetuple())

        if url is not None:
            values['url'] = url
        data = urlencode(values)
        url = self.base_url + '/api/events'
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        content = response.read()
        event = anyjson.deserialize(content)['event']
        self._massage_event(event)
        return event, response.code == 201
    
    def get_events(self, start, end):
        if not isinstance(start, (datetime.date, datetime.datetime)):
            raise ValueError("start must be a datetime.date or datetime.datetime instance")
            
        if not isinstance(end, (datetime.date, datetime.datetime)):
            raise ValueError("end must be a datetime.date or datetime.datetime instance")
        
        return self._get_events(start, end)
        
    def _get_events(self, start, end):
        values = dict(start=mktime(start.timetuple()),
                      end=mktime(end.timetuple()),
                      guid=self.guid,
                      )
        url = self.base_url + '/api/events.json'
        url += '?' + urlencode(values)
        req = urllib2.Request(url)
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError, msg:
            if '403' in str(msg):
                raise AuthorizationError(msg)
            raise
        if response.code != 200:
            msg = "%s: %s" % (response.code, response.read())
            raise ConnectionError(msg)
        content = response.read()
        data = anyjson.deserialize(content)
        for event in data['events']:
            self._massage_event(event)
        return data
    
    def _massage_event(self, event):
        event['start'] = datetime.datetime.fromtimestamp(float(event['start']))
        event['end'] = datetime.datetime.fromtimestamp(float(event['end']))
        event['all_day'] = event.pop('allDay')
        
def test_getting():
    dc = DoneCal('6a971ed0-7105-49a4-9deb-cf1e44d6c718', 'http://worklog')
    data = dc.get_events(datetime.datetime(2010,10,1),
                         datetime.date(2010, 10, 31))
    #from pprint import pprint
    #print("TAGS")
    #pprint(data['tags'])
    #print("EVENTS")
    #pprint(data['events'])
    
def test_getting_with_wrong_guid():
    dc = DoneCal('XXXXXX-XXXX-XXXX-XXXX-XXXXXXX', 'http://worklog')
    try:
        dc.get_events(datetime.datetime(2010,10,1),
                      datetime.date(2010, 10, 31))
    except AuthorizationError:
        pass
    except:
        raise
    

def xtest_posting():
    dc = DoneCal('6a971ed0-7105-49a4-9deb-cf1e44d6c718', 'http://worklog')
    event, created = dc.add_event(u'@API £ testing')
    #print "Created?", created and 'Yes' or 'No'
    #from pprint import pprint
    #pprint(event)
    
    


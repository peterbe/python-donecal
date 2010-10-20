python-donecal
==============

(c) Peter Bengtsson, mail@peterbe.com, 2010
License: BSD

About
-----

This package makes it easy to use the restful HTTP API on
http://donecal.com/

All you need is your `guid` which you can pick up on
http://donecal.com/help/API once you have created an account.

Installation
------------

Install the package with pip or easy_install. Like this:

        pip install python-donecal
        
Usage
-----

The API is working swimingly but it's not very rich at the moment.
Here's some sample code to get you started:

        >>> import datetime
        >>> from donecal import DoneCal
        >>> dc = DoneCal('XXXXXX-XXXX-XXXX-XXXX-XXXXXX')
        >>> data = dc.get_events(datetime.date(2010, 10, 1),
        ...                      datetime.datetime.now())
        >>> print data['tags']
        ['@ProjectX', '@ProjectY']
        >>> from pprint import pprint
        >>> pprint(data['events'][0])
        {'all_day': True,
         'end': datetime.datetime(2010, 10, 20, 0, 0),
         'id': '4cb086b06da6812276000001',
         'start': datetime.datetime(2010, 10, 20, 0, 0),
         'title': "Testing stuff on @ProjectX"}
        >>> # Now to post something
        >>> event, created = dc.add_event("Testing more stuff",
        ...    date=datetime.datetime(2010, 11, 1))
        >>> print "Created?", created and "yes" or "no"
        yes

Limitations
-----------

At the moment there are rate limitations but there might be some time
in the future to ensure fair access for everyone. 


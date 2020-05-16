# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

log_file = r"/Users/Yash/Desktop/app_log.txt"
with open(log_file) as f:
    f = f.readlines()
    look_for = 'werkzeug.exceptions.NotFound: 404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'
    for valid_logs in f:
        if look_for in valid_logs:
            print('Present')
        else:
            print('not present')
            
            
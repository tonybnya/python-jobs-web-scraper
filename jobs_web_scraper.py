#!/usr/bin/env python3
'''
jobs_web_scraper.py - Build a Jobs Web Scraper using parsehub application.
Link: https://www.parsehub.com/
'''

import time
import json
import sys
import requests
import pyperclip


API_KEY = your_api_key
PROJECT_TOKEN = your_project_token
RUN_TOKEN = your_run_token


class Job:
    '''
    A class to model a jobs parsing with parsehub API.
    '''

    def __init__(self, api_key, project_token):
        '''Initialize attributes of Job class.'''

        self.api_key = api_key
        self.project_token = project_token
        self.params = {'api_key': self.api_key}

    def get_jobs(self):
        '''Method to get jobs with parsehub API.'''

        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{your_project_token}/last_ready_run/data', params={'api_key': your_api_key})
        # Call json.loads() to convert JSON data to a Python data structure.
        return json.loads(response.text)


jobs = Job(API_KEY, PROJECT_TOKEN)
# Call the defined method to get all the listed jobs.
data = jobs.get_jobs()

print('MOST RECENT JOBS on https://pythonjobs.github.io/')
# Current date & time.
print(f'Last Update: {time.ctime()}\n')
for i, job in enumerate(data['jobs'], start=1):
    try:
        print(f'Job #{i}:')
        print()
        print('TITLE: ' + job['title'])
        print('COMPANY: ' + job['company'])
        print('LOCATION: ' + job['location'])
        print('ENTRY DATE: ' + job['entry_date'])
        print('TYPE: ' + job['type'])
        print('URL: ' + job['url'])
        # Copy url to the clipboard in case user want to apply.
        pyperclip.copy(job['url'])
        pyperclip.paste()
        print()
        print('-' * 15)
        print()
        print('URL copied to the clipboard.\nPress ENTER to continue.')
        print('Press CTRL-C to quit.')
        # Wait for any clipboard input to continue.
        input()
    except KeyboardInterrupt:
        # Exit prompt.
        sys.exit(1)

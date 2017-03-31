#!/usr/bin/env python

import requests
import lxml.html
import os

#---------------
# Configuration
#

# Term to monitor classes in (YYYYSS)
# YYYY = 4 digit year (e.g. 2017, 2016, 2015)
# SS = 2 digit semester (spring -> 02, summer -> 05, fall -> 08)
TERM = '201708'

# CRNs of courses to monitor
CRNS = ['80662', '86760']

#-----------
# Functions
#

def notify(message):
    print message
    os.system('terminal-notifier -title "Course Watch" -message "' + message + '"')

#------
# Main
#

print ''
print ' ======================== '
print '|| GT Course Watch v0.9 ||'
print '||   By Kevin Abraham   ||'
print ' ======================== '
print ''

print ''
print 'TERM: ' + TERM
print ''

for crn in CRNS:
    print ''
    print 'Fetching course info page from OSCAR...'
    print 'CRN:  ' + crn
    print ''

    html = requests.get('https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched?term_in=' + TERM + '&crn_in=' + crn).text

    print 'Fetched page. Parsing...'

    root = lxml.html.fromstring(html)
    dddefault = root.find_class('dddefault')

    print 'Parsed. Verifying...'

    if len(dddefault) != 7:
        print 'Unexpected results! Check the CRN number!'
        print ''
        continue
    else:
        print 'Verified.'
        print ''

    if int(dddefault[3].text) != 0:
        notify('Seat Available for CRN ' + crn + '!')
    elif int(dddefault[6].text) != 0:
        notify('Waitlist Seat Available for CRN ' + crn + '!')
    else:
        print 'No Seat Available for CRN ' + crn + '.'
    print ''

print ''
print 'All done.'
print ''

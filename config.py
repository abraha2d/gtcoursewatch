#---------------
# Configuration
#

# Term to monitor classes in (YYYYSS)
# YYYY = 4 digit year (e.g. 2017, 2016, 2015)
# SS = 2 digit semester (spring -> 02, summer -> 05, fall -> 08)
TERM = '201705'

# CRNs of courses to monitor
CRNS = ['50130', '50131']

# List of officially supported colleges for GT Course Watch
GT_URL = 'https://oscar.gatech.edu/pls/bprod/'
GGC_URL = 'https://ggc.gabest.usg.edu/pls/B400/'
GPC_URL = 'https://sis.gpc.edu/PROD/'

# URL of college student information system
# e.g. GT_URL for Georgia Tech, GGC_URL for GGC, etc.
# You can also set a custom URL here
URL = GGC_URL

# Waitlist disable. Set to True to disable waitlist checking
WLDIS = False

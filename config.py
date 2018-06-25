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
GSU_URL = 'https://www.gosolar.gsu.edu/bprod/'
KSU_URL = 'https://owlexpress.kennesaw.edu/prodban/'
GTC_URL = 'https://ssb01.gwinnetttech.edu/pls/ban8/'

# URL of college student information system
# e.g. GT_URL for Georgia Tech, GGC_URL for GGC, etc.
# You can also set a custom URL here
URL = GGC_URL

# Waitlist disable. Set to True to disable waitlist checking
WLDIS = False

# Email settings

EMAIL_SERVER = False    # e.g. smtp.gmail.com (for Gmail) or
                        # smtp.mail.me.com (for iCloud).
                        # Set to False to disable email notifications.

EMAIL_ADDRESS = ''      # Your email address.

EMAIL_PASSWORD = ''     # Your email password.
                        # If you have 2-step verification enabled, you
                        # will need to use an app-specific password.
                        # If you're using Gmail, then you may need to
                        # allow access to less secure apps.

EMAIL_TO = ''           # The email you want to send notifications to.
                        # This could be something like xxxxxxxxxx@txt.att.net
                        # or xxxxxxxxxx@vtext.com if you want to send a
                        # text message to your phone.

# GT Course Watch
Get an alert within seconds when a (waitlist/regular) seat opens up in a course section!

List of colleges officially supported:
- Georgia Tech
- Georgia Gwinnett College
- Georgia Perimeter College

Support for other colleges that use the Ellucian system can be easily added. To request that your college be added, log in to your college's registration system and navigate to the "Lookup Classes" link. Make note of the URL, and open an issue with your college name and the URL.

# Prerequisites
Install Python 3 from <https://www.python.org/downloads/>, then run the following in a terminal:
- `pip3 install requests lxml pyqt5`

# Setup
- Download the repository zip file (Clone or download > Download ZIP)
- Extract the zip and open 'config.py' (with a text editor)
- Edit the TERM variable to reflect the term you're registering for
- Edit the CRNS variable to reflect which courses you want to monitor
- Edit the URL variable to reflect which college system to search in
- If you encounter errors with waitlist detection (happens with some courses), set WLDIS to True
- Save, and close

# Instructions
- Inside the downloaded folder, double-click on `gtcoursewatch`
- Accept any security warnings. On Macs, instead of double-clicking, you may have to right-click and then click 'Open' to get past the security warning
- Profit. When GT Course Watch detects that there is a seat available in any of the classes you chose, it will send you a notification on your computer

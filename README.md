# GT Course Watch
Get an alert within seconds when a (waitlist/regular) seat opens up in a course section!
Currently, Georgia Tech students only.

# Prerequisites
Run the following in a terminal. If you see any errors about permissions, prefix the command with `sudo `, run, and enter your password if necessary.
- `pip3 install requests`
- `pip3 install lxml`
- `pip3 install pyqt5`

# Setup
- Download the repository zip file (Clone or download > Download ZIP)
- Open gtcoursewatch.py in a text editor
- Edit the TERM to reflect the term you're registering for
- Edit the CRNS to reflect which courses you want to monitor
- Save, and close

# Instructions
- Open a terminal
- `cd` to where you cloned the repo
  - Most likely `cd ~/Downloads/gtcoursewatch/`
- Run `chmod +x gtcoursewatch.py` (only required once)
- Run `watch ./gtcoursewatch.py`
- Profit. When GT Course Watch detects that there is a seat available in any of the classes you chose, it will send you a notification on your computer.

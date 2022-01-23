# Download of daily foreign exchange transaction and orderbook data from Refinitiv (REST API)

\-----   DESCRIPTION     -----\
The Python code connects to Refinitiv via API, downloads any data that is not currently found in the existing database, and adds the newly downloaded data into the database.

Important: You would need a Refinitiv Datascope account username and password for the code to work. Key in your credentials into "daily_extract.py".

\-----   INSTALLATION    -----
1. Ensure python 3.7.X is available on your local machine. It can
be installed from python.org. You may desire to create a virtual
environment for this project so that python packages installed in
the next step do not conflict with other projects.

2. Open a new terminal/command line session.

3. Install necessary python packages. This can be done by referencing
the requirements file "requirements.txt ". The command is "pip install -r requirements.txt"

4. Finally, to manually download the data, you can double-click "daily_extract.py".

\-----   AUTOMATATION    -----\
You can further automate the download, by creating a .BAT file and schedule periodic runs of the .BAT file on a scheduler (e.g. Task Scheduler on Windows).

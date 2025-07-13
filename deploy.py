# deploy.py

import sys
adminUrl = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
appPath = sys.argv[4]
appName = sys.argv[5]

connect(username, password, adminUrl)
deploy(appName=appName, path=appPath, targets='AdminServer', upload='true')
disconnect()
exit()


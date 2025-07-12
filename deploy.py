import sys
user, pwd, url, war, appName, target = sys.argv[1:]
connect(user, pwd, url)
deploy(appName, war, targets=target, upload='true')
disconnect()
exit()

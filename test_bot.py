import time
import requests
import random
from selenium import webdriver


# List of proxies from free-proxy-list.net will expire eventually
proxies = ["138.121.32.133:23492", 
	"182.253.82.156:35955", 
	"119.82.253.175:31500", 
	"51.158.111.242:8811",
	"15.165.85.203:3128",
	"118.174.232.128:45019",
	"200.255.122.170",
	"61.9.82.34:37892"]

# List of user agents some legit some not
user_agent_list = [
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Kam Hardy'
]

#choosing a random user-agent
for i in range(1,6):
	user_agent = random.choice(user_agent_list)

#choosing a random proxy ip address
for i in range(1,6):
	PROXY = random.choice(proxies)

options = webdriver.ChromeOptions()

#Custom User Agent
#options.add_argument("--user-agent=Kam Hardy")

# Multiple User Agents
options.add_argument("--user-agent=%s" % user_agent)

## Bypass untrusted SSL certificates
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')

# Using a proxy
options.add_argument('--proxy-server=http://%s' % PROXY)


driver = webdriver.Chrome(options=options)  # Optional argument, if not specified will search path.
driver.get('https://blog.proteafinance.com/');
driver.add_cookie({"name":"kam-bot", "value":"its me"})

time.sleep(10) # Let the user actually see something!

driver.quit()
# Used in case certain proxies have expired, you know which
print(PROXY)

import urllib2
import re
import mechanize

matches = []

# Look for codes on the new pages of /r/trove
hdr = { 'User-Agent' : 'Looking for the Trove codes' }
url= 'http://www.reddit.com/r/trove/new.json?sort=new'
req = urllib2.Request(url, headers=hdr)
page = urllib2.urlopen(req)
contents = page.read()
# Very basic regex, could be improved for sure
matches = re.findall('[A-z1-9]{4}-[A-z1-9]{4}-[A-z1-9]{4}-[A-z1-9]{4}-[A-z1-9]{4}', contents)

print "Fetched matches!"

# Setup login to TrionWorlds
browser = mechanize.Browser()
browser.set_handle_refresh(False)
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] 
browser.open("https://session.trionworlds.com/login")
browser.select_form(nr = 0)
print "Selected"
browser.form['username'] = "INSERT EMAIL HERE"
browser.form['password'] = "INSERT PASSWORD HERE"
browser.submit()

print "Got session!"

# Try to apply dem sweet sweet codes

for codes in matches:
	print "Trying code: " + codes
	url = browser.open("https://store.trionworlds.com/commerce/voucher/redeem-voucher-flow")
	browser.select_form(nr = 0)
	browser.form['voucherCode'] = codes
	browser.submit()

print "tried " + str(len(matches)) + " codes!"

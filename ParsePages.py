#######################################################################
### DEMO SCRIPT WITH VARIOUS DECLARATIONS AND EXAMPLES FOR REFERENCE
import pickle
import urllib.request
import string
import os.path

from pathlib import Path
from time import sleep

## if we find StartText, we have results
## then copy that through StopText

StartText = "<span class=\"headerResults\">"
StopText = "<div class=\"footerResults\">"
FailText = "weAreSorry1"


while find agentContainer
	parse
			<div class="strong">

				Classic Insurance

			</div>

			<span class="agencyInfo">2034 Lexington St, Houston, TX 77098<br />(713) 349-8778</span><br />






#######################################################################
### DATA DECLARATIONS

urlprefix = "http://www.progressiveagent.com/findanagent/search-results.aspx?product=Auto&zipCode="

fn_zipsfile = "C:\\Users\\Jerry Hobby\\OneDrive\\Documents\\Python\\zip_code_database.txt"
fn_outprefix = "C:\\Users\\Jerry Hobby\\OneDrive\\Documents\\Python\\progressive\\progressive-"
fn_outsuffix = ".html"

zips = []

#with open(fn_zipsfile, 'r') as f:
#	zips = f.readlines()

zips = open(fn_zipsfile).read().splitlines()
print (len(zips))

# override list for testing
zips = [ "77001", "77002", "77003", "77004", "77005"]

for zip in zips:

	url = urlprefix + zip
	print(zip + ": " + url)

	fn_name = fn_outprefix + zip + fn_outsuffix
	print(zip + ": " + fn_name)

	if not os.path.isfile(fn_name):
		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req)
		html_raw = response.read()
		html_utf = html_raw.decode('utf8')

		openfile = open(fn_name, 'w')
		openfile.write(html_utf)
		openfile.close

		print(zip + ": Page Captured")
		sleep(1)
	else:
		print(zip + ": Skipping, file exists")






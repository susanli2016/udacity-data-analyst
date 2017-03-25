"""
Your task in this exercise is to modify 'extract_carrier()` to get a list of
all airlines. Exclude all of the combination values like "All U.S. Carriers"
from the data that you return. You should return a list of codes for the
carriers.

All your changes should be in the 'extract_carrier()' function. The
'options.html' file in the tab above is a stripped down version of what is
actually on the website, but should provide an example of what you should get
from the full file.

Please note that the function 'make_request()' is provided for your reference
only. You will not be able to to actually use it from within the Udacity web UI.
"""

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_carriers(page):
    data = []

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        carrier_list = soup.find(id='CarrierList')
        for carrier in carrier_list.find_all('option'):
            if carrier['value'][:3] != 'All':
                data.append(carrier['value'])

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': airport,
                          'CarrierList': carrier,
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

if __name__ == "__main__":
    test()

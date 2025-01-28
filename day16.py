# To create virtual environment

#python -m venv venv_name

# To activate venv

# python\scripts\activate    # cmd


# requests

# pip install requests

import requests
r = requests.get("https://www.onlinekhabar.com/smtm/home/trending")
print(r.json())

data = r.json()
final_data = data["response"]
f = open('day.txt', 'a')
for i in final_data:
    a = (
        f"Ticker: {i['ticker']} \n Ticker Name: {i['ticker_name']} \n Latest Price: {i['latest_price']} \n Points Change: {i['points_change']} \n Percentage Change: {i['percentage_change']}"
        )
    f.write(a)
f.close()
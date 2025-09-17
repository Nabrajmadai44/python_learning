# import requests
# r = requests.get("https://www.onlinekhabar.com/smtm/home/trending")
# print(r.json())

# data = r.json()
# final_data = data["response"]
# f = open('day.txt', 'a')
# for i in final_data:
#     a = (
#         f"Ticker: {i['ticker']} \n Ticker Name: {i['ticker_name']} \n Latest Price: {i['latest_price']} \n Points Change: {i['points_change']} \n Percentage Change: {i['percentage_change']}"
#         )
#     f.write(a)
# f.close()



a= [
    {
        "name":"sudan",
        "address":"324"
    },
    {
        "name":"suman",
        "address":"edwer"
    }
]

result = []

for i in a:
    tuple_data = []
    tuple_data.append(i['name'])
    tuple_data.append(i['address'])
    result.append(tuple(tuple_data))
print(result)
    

# final_data = [
#     ("sudan","324"),
#     ("suman","dsfasdf")
# ]
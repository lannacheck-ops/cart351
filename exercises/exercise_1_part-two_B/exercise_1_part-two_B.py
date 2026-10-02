import requests
#my api key -> you should add yours
api_key = "2ba267fc5ab5b4c99201b8efab509d99"
#url to get results with the city added
url_with_city ="http://api.openweathermap.org/data/2.5/weather?q=" 
#url with the api key appeneded
url_to_send = url_with_city + "&APPID=" + api_key 

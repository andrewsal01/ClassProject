# for making get requests

import requests

def fetch_data(zip=None, city=None):

    # base url for fetching the weather
    baseUrl = "http://api.openweathermap.org/data/2.5/weather"
    # api id for the site
    apiid = "7d6b07eda8f8b4be94583a454eb805f6"
    # check if the suer gave the zip code or the city name
    if zip is not None:
                # us at the end id for usa country , change it as required
        baseUrl += "?zip="+str(zip)+",us"
    else:
        baseUrl += "?="+str(city)+",us"
    # finally append the api id
        baseUrl += "&appid="+str(apiid)
    # make get requetss using requests module
    r = requests.get(baseUrl)
    # return the response
    return r

#this method shows teh result in readbale for,

def showResult(resp):
    #this means request was successfull
    if resp.status_code == 200:
        data= resp.json()
        print(data['name'])
        print(f"""{data['name']} Weather Forecast:

        There will be {data['weather'][0]['description']} with wind speed of {data['wind']['speed']}.
        Min. Temp will be {data['main']['temp_min']} and max will be {data['main']['temp_max']}.
        """)

    else:
        print("Request Failed, Try Again Error Code : ",resp.status_code)


def main():
    #runs till exit
    while True:
        inp =int(input("Your options :\n1. By Zip Code\n2. By City Name\n3. Exit\n"))
        if inp == 1:
            #ask for zip code
            try:
                queryData=int(input("Enter zip code : "))
                #call data from zip input
                resp= fetch_data(queryData,None)
                showResult(resp)
            except Exception as ex:
                print("Error : ",ex)
        elif inp == 2:
            try:
                queryData = input("Enter city name : ")
                #call data from city input
                resp= fetch_data(None,queryData)
                showResult(resp)
            except Exception as ex:
                print("Error : ",ex)
        elif inp==3:
            break
        else:
            print("Invalid Choice..\n")

if __name__=="__main__":

    main()
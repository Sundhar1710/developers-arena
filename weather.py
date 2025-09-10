import requests as res
def getweather(city):
    apikey = "b1f2e7dce8c473bf5f6ff4d1df93f403"
              
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
    print("Data Loading please wait ....\n")
    r = res.get(url).json()
    try:
        temp = (r['main']['temp'])
        l = r['name']
        c = (r['weather'][0]['description'])
        print('--------------------------')
        print(f"📍Location: {l}\n🌡 Temperature: {(temp - 273.5):.2f}\u00b0C\n💁 Condition: {c}")
        print('--------------------------\n')
    except:
        print('---------------------------\n')
        print(f'Error: Unable to fetch data for {city}. please check the city name \n')
        print('---------------------------\n')


if __name__ == '__main__':
    print("---- welcome to Weather App ------")
    while True:
        print("enter 'exit' to close the app!")
        c = input("Enter city name: ").lower()

        if c != 'exit':
            getweather(c)
        else:
            print('Bye!')
            break
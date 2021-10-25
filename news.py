from newsapi import NewsApiClient
import pycountry
 
# you have to get your api key from newapi.com and then paste it below
newsapi = NewsApiClient(api_key='cd6a74d24eaf4c9885dcf78ea2c17f67')
 
# now we will take name of country from user as input
input_country = input("Country: ")
input_countries = [f'{input_country.strip()}']
countries = {}
 
# iterate over all the countries in
# the world using pycountry module
for country in pycountry.countries:
 
    # and store the unique code of each country
    # in the dictionary along with it's full name
    countries[country.name] = country.alpha_2
 
# now we will check that the entered country name is
# valid or invalid using the unique code
codes = [countries.get(country.title(), 'Unknown code')
         for country in input_countries]
 
# now we have to display all the categories from which user will
# decide and enter the name of that category
option = input("Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
 
# now we will fetch the new according to the choice of the user
top_headlines = newsapi.get_top_headlines(
 
    # getting top headlines from all the news channels
    category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')
 
  # fetch the top news inder that category
Headlines = top_headlines['articles']
 
   # now we will display the that news with a good readiblity for user
if Headlines:
        for articles in Headlines:
            b = articles['title'][::-1].index("-")
            if "news" in (articles['title'][-b+1:]).lower():
                print(
                    f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
            else:
                print(
                    f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
        else:
            print(
            f"Sorry no articles found for {input_country}, Something Wrong!!!")

        option = input("Do you want to search again[Yes/No]?")
        if option.lower() == 'yes':
            
            for i in range():
                continue
        else:
            exit()

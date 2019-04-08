import requests
import json

import hashlib
import random
import string


#get the weather from open-weather-map
def my_weather():
    api_address = "http://api.openweathermap.org/data/2.5/weather?zip=66202,us&units=imperial&APPID="
    api_code = "2d4cdcba967ce53aae8c4db47fd6b052"
    url = api_address + api_code

    json_data = requests.get(url).json()

    current_weather = json_data['weather'][0]['main']

    icon_code = json_data['weather'][0]['icon']

    icon_url = "http://openweathermap.org/img/w/" + icon_code + ".png"

    current_temp = json_data['main']['temp']

    weather_tuple = (current_weather, icon_url, current_temp)

    return weather_tuple


#make sure the user name given isn't too short or too long
def valid_length(input):
    if len(input) >= 3 and len(input) < 400:
        return True
    else:
        return False


#check that the passwords given in registration match
def valid_match(input1, input2):
    if input1 == input2:
        return True
    else:
        return False

#check that the inputs meet our criteria for use, no spaces, etc
def valid_txt(input1, input2):
    if ' ' in input1 or ' ' in input2:
        return False
    elif '@' in input1 or '@' in input2:
        return False
    elif '.' in input1 or '.' in input2:
        return False
    else:
        return True

#create a salt for our hashed password
def make_salt():
    return ''.join([random.choice(string.ascii_letters) for x in range(5)])


#create the hashed version of the user password to save in our database
def make_hash(password, salt=None):
    if not salt:
        salt = make_salt()
    hash = hashlib.sha256(str.encode(password + salt)).hexdigest()
    return '{0},{1}'.format(hash, salt)


#used to check the hashed & salted password from the database
def check_hash(password, hash):
    salt = hash.split(',')[1]
    
    if make_hash(password, salt) == hash:
        return True
    else:
        return False


#create a main function to run and test at the command line
def main():
    input1 = str(input('What is the first input? '))
    input2 = str(input('What is the second input? '))

    print('input 1 long enough? ', valid_length(input1), '\n')
    print('input 2 long enough? ', valid_length(input2), '\n')

    print('input 1 matches input 2? ', valid_match(input1, input2), '\n')
    print('no funky characters in input1 or input2? ', valid_txt(input1, input2), '\n')


#shield for running at the terminal with command-line input
if __name__ == "__main__":
    main()
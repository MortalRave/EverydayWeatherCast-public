# EverydayWeatherCast-public
Simple app for sending weather casts emails.
Weather information taken with openweathermap.org api - it's free to use.

To use it you only need pip install requests and change few things:

In main.py
API_KEY = "your openweathermap api key"
CITY = "your city"

In sendmail.py
me = "gmail address to send mails"
you = "gmail address to get mails"
mail.login('senders gmail login','senders gmail password')



With pythonanywhere.com it's easy to send it everyday.

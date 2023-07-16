import smtplib
import main

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import date

# me == my email address
# you == recipient's email address
me = "sender@mail.com"
you = "getter@mail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Weather for " + str(date.today())
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = ""
html = f"""\
<html>
  <head>
  </head>
  <body style="background-color: #1b4778; font-family:sans-serif">
    <div id="{main.city_name}" style="text-align:center;color:white;font-size:80px;font-weight:bold;">{main.city_name}</div>
    <div id="Today" style="text-align:center;">
      <div id="srss" style="color:#808080;font-weight:bold;">
        Sunrise: {main.sun_rise}                 Sunset {main.sun_set}
      </div>
      <ol id="timelaps" style="list-style-type:none;margin-left:auto;margin-right:auto;text-align:center;width:fit-content;">
        <div id="today_time" style="background-color:#355e8e;list-style-type:none;float:left;min-width:120px;border-style:solid;border-color:#1b4778;padding:15px;">
          <p id="hour" style="margin:0;font-size:large;font-weight:bold;background-color:gray;">{main.h1.hour}</p>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h1.temp}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h1.weather}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Feel like</p>
              <p style="margin:0;">{main.h1.feeltemp}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Pressure</p>
              <p style="margin:0;">{main.h1.pressure}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Rain lvl</p>
              <p style="margin:0;">{main.h1.rain}</p>
            </div>
          </div>
        </div>
        <div id="today_time" style="background-color:#355e8e;list-style-type:none;float:left;min-width:120px;border-style:solid;border-color:#1b4778;padding:15px;">
          <p id="hour" style="margin:0;font-size:large;font-weight:bold;background-color:gray;">{main.h2.hour}</p>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h2.temp}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h2.weather}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Feel like</p>
              <p style="margin:0;">{main.h2.feeltemp}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Pressure</p>
              <p style="margin:0;">{main.h2.pressure}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Rain lvl</p>
              <p style="margin:0;">{main.h2.rain}</p>
            </div>
          </div>
        </div>
        <div id="today_time" style="background-color:#355e8e;list-style-type:none;float:left;min-width:120px;border-style:solid;border-color:#1b4778;padding:15px;">
          <p id="hour" style="margin:0;font-size:large;font-weight:bold;background-color:gray;">{main.h3.hour}</p>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h3.temp}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h3.weather}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Feel like</p>
              <p style="margin:0;">{main.h3.feeltemp}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Pressure</p>
              <p style="margin:0;">{main.h3.pressure}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Rain lvl</p>
              <p style="margin:0;">{main.h3.rain}</p>
            </div>
          </div>
        </div>
        <div id="today_time" style="background-color:#355e8e;list-style-type:none;float:left;min-width:120px;border-style:solid;border-color:#1b4778;padding:15px;">
          <p id="hour" style="margin:0;font-size:large;font-weight:bold;background-color:gray;">{main.h4.hour}</p>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h4.temp}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h4.weather}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Feel like</p>
              <p style="margin:0;">{main.h4.feeltemp}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Pressure</p>
              <p style="margin:0;">{main.h4.pressure}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Rain lvl</p>
              <p style="margin:0;">{main.h4.rain}</p>
            </div>
          </div>
        </div>
        <div id="today_time" style="background-color:#355e8e;list-style-type:none;float:left;min-width:120px;border-style:solid;border-color:#1b4778;padding:15px;">
          <p id="hour" style="margin:0;font-size:large;font-weight:bold;background-color:gray;">{main.h5.hour}</p>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h5.temp}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h5.weather}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Feel like</p>
              <p style="margin:0;">{main.h5.feeltemp}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Pressure</p>
              <p style="margin:0;">{main.h5.pressure}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Rain lvl</p>
              <p style="margin:0;">{main.h5.rain}</p>
            </div>
          </div>
        </div>
        <div id="today_time" style="background-color:#355e8e;list-style-type:none;float:left;min-width:120px;border-style:solid;border-color:#1b4778;padding:15px;">
          <p id="hour" style="margin:0;font-size:large;font-weight:bold;background-color:gray;">{main.h6.hour}</p>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h6.temp}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h6.weather}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Feel like</p>
              <p style="margin:0;">{main.h6.feeltemp}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Pressure</p>
              <p style="margin:0;">{main.h6.pressure}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Rain lvl</p>
              <p style="margin:0;">{main.h6.rain}</p>
            </div>
          </div>
        </div>
        <div id="today_time" style="background-color:#355e8e;list-style-type:none;float:left;min-width:120px;border-style:solid;border-color:#1b4778;padding:15px;">
          <p id="hour" style="margin:0;font-size:large;font-weight:bold;background-color:gray;">{main.h7.hour}</p>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h7.temp}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h7.weather}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Feel like</p>
              <p style="margin:0;">{main.h7.feeltemp}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Pressure</p>
              <p style="margin:0;">{main.h7.pressure}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Rain lvl</p>
              <p style="margin:0;">{main.h7.rain}</p>
            </div>
          </div>
        </div>
        <div id="today_time" style="background-color:#355e8e;list-style-type:none;float:left;min-width:120px;border-style:solid;border-color:#1b4778;padding:15px;">
          <p id="hour" style="margin:0;font-size:large;font-weight:bold;background-color:gray;">{main.h8.hour}</p>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h8.temp}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h8.weather}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Feel like</p>
              <p style="margin:0;">{main.h8.feeltemp}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Pressure</p>
              <p style="margin:0;">{main.h8.pressure}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Rain lvl</p>
              <p style="margin:0;">{main.h8.rain}</p>
            </div>
          </div>
        </div>
        <div id="today_time" style="background-color:#355e8e;list-style-type:none;float:left;min-width:120px;border-style:solid;border-color:#1b4778;padding:15px;">
          <p id="hour" style="margin:0;font-size:large;font-weight:bold;background-color:gray;">{main.h9.hour}</p>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h9.temp}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>{main.h9.weather}</div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Feel like</p>
              <p style="margin:0;">{main.h9.feeltemp}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Pressure</p>
              <p style="margin:0;">{main.h9.pressure}</p>
            </div>
          </div>
          <div id="hour_disc" style="color:white;font-weight:bold;list-style-type:none;padding:0;border-top-style:solid;border-color:gray;border-width:1px;padding-top:5px;padding-bottom:5px;">
            <div>
              <p style="margin:0;font-size:small; color: #b1b1b1;">Rain lvl</p>
              <p style="margin:0;">{main.h9.rain}</p>
            </div>
          </div>
        </div>
      </ol>
    </div>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('gmaillogin', 'gmailpassword')
mail.sendmail(me, you, msg.as_string())
mail.quit()

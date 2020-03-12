# Science

to login open crosh or command promt and enter `ssh mac@[redacted]` then put the password and then enter `auto` without a `./` to have it run
to view the outputs enter `screen -r science`

# Brain Structure
Left input is multiplied by left number
Right input is multiplied by right number


# Website Access
I just created a google cite, so feel free to go on and edit!!!!

For the website we should create a server api so we can actually get requests from a website - https://stackoverflow.com/questions/8928730/processing-http-get-input-parameter-on-server-side-in-python/8930440 https://stackoverflow.com/questions/5239547/fetching-http-get-variables-in-python/5239594#5239594 https://github.com/dheerajmpai/pyserv/

# Important Breakdown of the Data

- this is one data piece that I pulled from the data and broke down
- The "weather" section could become very useful.
- Also, the "dt" sections are a bit confusing -- One seems to consist of a strung set, consisting of the time and date, while the other appears to be some sort of ID which I can't break down. ----- The dt section is the date and time formatted in unix timestamp https://www.convert-unix-timestamp.com/unixtime/1356998400#.Xl1dO45zy00
{ "city_name":"Untitled",

"lat":42.245931, "lon":-71.282834,

"main":{"temp":-1.01,"temp_min":-2,"temp_max":0,"feels_like":-5.36,"pressure":1011.5,"humidity":60},

"wind":{"speed":2.1,"deg":240},

"snow":{"1h":0},"clouds":{"all":1},

"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],

"dt":1356998400, "dt_iso":"2013-01-01 00:00:00 +0000 UTC",

"timezone":-18000

}

import config
 
city_id = "5128581" 
 
base_url = "https://api.openweathermap.org/data/2.5/weather?" 
final_url = base_url + "appid=" + config.api_key + "&id=" + city_id
humidity = 40
gas = 40000

# Set the humidity baseline to 40%, an optimal indoor humidity.
humidity_baseline = 40.0

# This sets the balance between humidity and gas reading in the 
# calculation of air_quality_score (25:75, humidity:gas)
humidity_weighting = 0.25
gas_weighting = 0.75

gas_reference = 40000
hum_reference = 40
gas_lower_limit = 5000
gas_upper_limit = 50000

if humidity >= 38 and humidity <= 42:
    humidity_score = humidity_weighting * 100
else:
    if humidity < 38:
        humidity_score = humidity_weighting / hum_reference * humidity * 100;
    else:
        humidity_score = ((-humidity_weighting / (100 - hum_reference) * humidity) + 0.416666) * 100;
print("Humidity Score: ", humidity_score)

gas_score = (gas_weighting / (gas_upper_limit - gas_lower_limit) * gas_reference - (gas_lower_limit * (gas_weighting / (gas_upper_limit - gas_lower_limit)))) * 100.00
if gas_score > 75:
    gas_score = 75
if gas_score <  0:
    gas_score = 0
    
print("GasScore: ", gas_score)

air_quality_score = humidity_score + gas_score
print("IAQ: ", air_quality_score)
score = (100-air_quality_score)*5
print(score)


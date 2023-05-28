import streamlit as st
from weather_city_api import get_weather_data


# Title
st.title("Vejret")

# Input
city = st.text_input('Indtast ønsket by', 'Copenhagen')
st.write('Den nuværende by:', city)

# Call weather_city_api function and pass the city parameter
weather_data = get_weather_data(city)


if weather_data is not None:
    # Top metrics
    temp, max, min = st.columns(3)

    with temp:
        st.metric("Nuværende temperatur", "{:.2f} °C".format(weather_data['temp_celsius']))

    with max:
        st.metric("Max temperatur idag", "{:.2f} °C".format(weather_data['temp_max_celsius']))

    with min:
        st.metric("Minimum temperatur idag", "{:.2f} °C".format(weather_data['temp_min_celsius']))

    # Top metrics
    nedgang, opgang = st.columns([1,2])

    with opgang:
        st.metric("Solopgang", weather_data['sunrise_time'])

    with nedgang:
        st.metric("Solnedgang", weather_data['sunset_time'])

    # Top metrics
    vind, fugtig = st.columns([1,2])

    with vind:
        st.metric("Vind hastighed", "{:.2f} m/s".format(weather_data['wind_speed']))

    with fugtig:
        st.metric("Fugtighed", "{}%".format(round(weather_data['humidity'])))

else:
    st.error("By ej fundet")
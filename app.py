import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Provide details of your journey:
'''

columns = st.columns(7)

p_dat = columns[0].date_input(
    'Journey Start Date',
    datetime.date(2019, 7, 6)
    )

p_tim = columns[1].time_input(
    'Journey Start Time',
    datetime.time(8, 45)
    )

p_lon = columns[2].text_input("Pickup Longitude")

p_lat = columns[3].text_input("Pickup Latitude")

d_lon = columns[4].text_input("Dropoff Longitude")

d_lat = columns[5].text_input("Dropoff Latitude")

n_pas = columns[6].text_input("Number of Passengers")


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

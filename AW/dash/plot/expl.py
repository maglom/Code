
import pandas as pd
import plotly.express as px

df = pd.read_csv(r'C:\Users\magnu\Documents\Code\AW\dash\plot\airline_passenger_satisfaction.csv')

df[:30]

df['Gender'][:30]

fig = px.line(df, x=df['ID'][:300], y=df['Seat Comfort'][:300])

fig.show()
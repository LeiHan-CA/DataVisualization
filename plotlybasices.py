# Import required libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Read the airline data into pandas dataframe
airline_data = pd.read_csv('source/airline_data.csv',
                           encoding="ISO-8859-1",
                           dtype={'Div1Airport': str, 'Div1TailNum': str,
                                  'Div2Airport': str, 'Div2TailNum': str})

# random 500 rows data
data = airline_data.sample(n=500, random_state=42)

# First we create a figure using go.Figure and adding trace to it through go.scatter
fig = go.Figure(data=go.Scatter(x=data['Distance'], y=data['DepTime'], mode='markers', marker=dict(color='red')))
# Updating layout through `update_layout`. Here we are adding title to the plot and providing title to x and y axis.
fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DepTime')
# Display the figure
# fig.show()

# Group the data by Month and compute average over arrival delay time.
line_data = data.groupby('Month')['ArrDelay'].mean().reset_index()
print(line_data)

# line plot
fig = go.Figure(
    data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
fig.show()

# bar chart
# Group the data by destination state and reporting airline. Compute total number of flights in each combination
bar_data = data.groupby(['DestState'])['Flights'].sum().reset_index()
bar_data
fig = px.bar(bar_data, x="DestState", y="Flights",
             title='Total number of flights to the destination state split by reporting airline')
fig.show()

# bubble chart
# Group the data by reporting airline and get number of flights
bub_data = data.groupby('Reporting_Airline')['Flights'].sum().reset_index()
fig = px.scatter(bub_data, x='Reporting_Airline', y="Flights", title='Reporting Airline vs Number of Flights',
                 size='Flights', hover_name="Reporting_Airline", size_max=60)
fig.show()

# Histogram
# Set missing values to 0
data['ArrDelay'] = data['ArrDelay'].fillna(0)
fig = px.histogram(data, x="ArrDelay")
fig.show()

# pie chart
# Use px.pie function to create the chart. Input dataset.
# Values parameter will set values associated to the sector. 'Month' feature is passed to it.
# labels for the sector are passed to the `names` parameter.
fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proportion by month')
fig.show()

# Sunburst Charts
fig = px.sunburst(data, path=['Month', 'DestStateName'], values='Flights')
fig.show()

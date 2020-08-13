import pandas as pd
import matplotlib.pyplot as plt
import altair as alt


#Data from EU Open Data Portal
df = pd.read_excel(r'/Users/karolina/Desktop/COVID-19-geographic-disbtribution-worldwide.xlsx')
plt.style.use('seaborn-whitegrid')
countries = ['Germany', 'United_Kingdom', 'Italy', 'France', 'Spain', 'Ukraine', 'Romania', 'Netherlands', 'Belgium', 'Poland']
df = df[df['countriesAndTerritories'].isin(countries)]
interval = alt.selection_interval()

chart1 = alt.Chart(df).mark_circle().encode(
    x=alt.X('dateRep', axis=alt.Axis(title='Date')),
    y=alt.Y('countriesAndTerritories', axis=alt.Axis(title='Country')),
    color=alt.condition(interval, 'countriesAndTerritories', alt.value('lightgray'), legend=alt.Legend(title="Countries")),
    size=alt.Size('cases:Q',
        scale=alt.Scale(range=[0, 1000]),
        legend=alt.Legend(title='Daily new cases')
    )
).properties(
    title='Daily cases of SARS-CoV-2 in top 10 most populated countries in Europe',
    width=800,
    height=400,
    selection=interval
)

chart2 = alt.Chart(df).mark_bar().encode(
    y=alt.Y('countriesAndTerritories', axis=alt.Axis(title='Country')),
    color=alt.Color('countriesAndTerritories', legend=alt.Legend(title="Countries")),
    x=alt.X('sum(cases):Q', axis=alt.Axis(title='Sum of new cases'))
).properties(
    width=1000,
).transform_filter(
    interval
)

(chart1 & chart2).show()
(chart1 & chart2).save('sarscov2_altair.json')





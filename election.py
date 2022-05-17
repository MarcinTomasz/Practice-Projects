#Election dataset from plotly.

import plotly.express as px

election_ds = px.data.election()
geojson = px.data.election_geojson()

#Map of districts and winner in each one.
fig = px.choropleth_mapbox(election_ds, 
                           geojson=geojson,
                           color = "Bergeron",
                           locations= "district",
                           featureidkey = "properties.district",
                           center = {"lat": 45.5517, "lon": -73.7073},
                           mapbox_style= "carto-positron",
                           zoom = 9)
election_ds

px.bar(data_frame=election_ds,
       x = 'district',
       y = 'total',
       facet_col = 'winner',
       labels = {'district': 'District',
                 'total': 'Vote Total',
                 'winner': 'Winner'})

#Bar graph showing each candidate's numbers per district.
fig1 = px.bar(data_frame=election_ds,
       x = 'district',
       y = 'total',
       facet_col = 'winner',
       labels = {'district': 'District',
                 'total': 'Vote Total',
                 'winner': 'Winner'})

#Shows either visualization.
fig.show()
fig1.show()

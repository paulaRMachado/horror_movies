import seaborn as sbn
import matplotlib as plt
import plotly.express as px
import os
import plotly.graph_objects as go
import kaleido
import plotly.io as pio

def img1(merged_df):
    condition_1 = merged_df.US_box_office != 0
    condition_2 = merged_df.budget != 0

    profit_df = merged_df[condition_1 & condition_2]

    fig1 = px.scatter(profit_df, x="imdb_rating", y="profit", hover_data=["title"], title='Relationship of profit and IMDB ratings', labels={
                     "profit": "Profit", "imdb_rating": "IMDB ratings"})
    fig1.update_layout(
    shapes=[dict(type='rect', xref='x', yref='y', x0=0, y0=-float('inf'),
            x1=10, y1=-115000000, fillcolor='rgb(255, 0, 0)', opacity=0.2, line_width=0)])
    fig1.add_shape(type="line", x0=0,y0=70000000,x1=10,y1=70000000)
    fig1.update_layout(annotations=[go.layout.Annotation(
            x=2,  # x position of the label
            y=80000000,  # y position of the label
            text="Profit over 0.7M",  # text of the label
            showarrow=False,  # hide the arrow
            xshift=5,  # shift the label to the right
            yshift=5)])
    pio.write_html(fig1, file='image/fig1.html', auto_open=True)
    fig1.show()
    

def img2(merged_df):
    condition_1 = merged_df.US_box_office != 0
    condition_2 = merged_df.budget != 0

    profit_df = merged_df[condition_1 & condition_2]

    box = px.box(profit_df, y="profit",points="all", hover_data=["title","year_release"], title='Distribution of profit',labels={
                     "profit": "Profit"})
    pio.write_html(box, file='image/box.html', auto_open=True)
    box.show()

def img3(merged_df):
    newdf = merged_df.loc[(merged_df.US_box_office != 0)]
    superdf = newdf.groupby(newdf.year_release)['US_box_office'].mean()
    x_data = range(1952,2023)
    y_data = superdf

    linefig = px.line(x=x_data,y=y_data, title='US box office across time', labels={
                     "y": "US box office", "x": "Years"})
    pio.write_html(linefig, file='image/linefig.html', auto_open=True)
    linefig.show()

def img4(merged_df):
    fig4 = px.scatter(merged_df, x="imdb_rating", y="popularity", hover_data=["title"], title='Relationshiop of IMDB rating and popularity')
    pio.write_html(fig4, file='image/fig4.html', auto_open=True)
    fig4.show()

def img5(merged_df):
    condition_1 = merged_df.US_box_office != 0
    condition_2 = merged_df.budget != 0
    profit_df = merged_df[condition_1 & condition_2]

    fig5 = px.bar(profit_df, x="genre_names", y="profit", hover_data=["title"], orientation='v', title="Total profit by subgenre")
    fig5.update_layout(xaxis = {"categoryorder":"total ascending"})
    pio.write_html(fig5, file='image/fig5.html', auto_open=True)
    fig5.show()
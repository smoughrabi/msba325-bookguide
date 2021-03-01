#Importing Modules
import pandas as pd
import numpy as np
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.offline import iplot
import plotly.express as px
import streamlit as st
import random

#Variables storing Images and Datasets

lineimage = 'msba325-bookguide/line.png'
header = 'msba325-bookguide/header.png'
croppedheader ='msba325-bookguide/cropped-header.jpg'

amazondata = 'msba325-bookguide/amazon_books.csv'
goodreadsdata = 'msba325-bookguide/goodreads_books.csv'
genrebooksdataset= 'msba325-bookguide/bookswithgenres.csv'


#Title
st.image(header)
st.header('''**MSBA 325 Plotly Visualization Assignment**
 **by Sarah El Moughrabi**''')
st.header('**An interactive guide for all your reading needs**')

with st.beta_expander('Expand to Learn More'):
    st.write('''Are you an avid reader looking for your next read? Or perhaps you've recently gotten into the habit and are unsure where to start? FEAR NOT!

See which books are hits among AMAZON and GoodReads users, get acquainted with top authors, and feel free to test out The Book Randomizer for a randomized book recommendation!''')
st.markdown('#')

st.image(lineimage)


##Importing AMAZON Books Dataset##
# this dataset has 550 rows and 7 columns showing the top 50 Amazon best sellers from the year 2009-2019
amazonbooks= pd.read_csv(amazondata)

#Making a new df without book duplicates, this will be used to display the top books based on avg rating
abooks_nodupes = amazonbooks.drop_duplicates(subset='Name')
del abooks_nodupes['Year'] #does not make sense to keep this in this df

#Sorting books by average rating
abooks_nodupes = abooks_nodupes.sort_values('User Rating', ascending=False)

#Splitting into fiction vs non-fiction titles
abooks_fiction = abooks_nodupes[abooks_nodupes['Genre']=='Fiction']
abooks_nonfiction = abooks_nodupes[abooks_nodupes['Genre']=='Non Fiction']

#Top 20 fiction and top 20 non-fiction
abooks_nonfiction = abooks_nonfiction[0:20]
abooks_topfiction = abooks_fiction[0:20]

atopfic_table = go.Figure(data=[go.Table(
    header=dict(values=['Title', 'Author(s)'],
                line_color='darkslategray',
                fill_color='lightgray',
                font_color='black',
                font_size=14,
                align='left'),
    cells=dict(values=[abooks_topfiction['Name'], # 1st column
                       abooks_topfiction['Author']], # 2nd column
               line_color='darkslategray',
               fill_color= 'powderblue',
               font_size=14,
               font_color='black',
               align='left'))
    ])
atopnonfic_table = go.Figure(data=[go.Table(
    header=dict(values=['Title', 'Author(s)'],
                line_color='darkslategray',
                fill_color='lightgray',
                font_size=14,
                font_color='black',
                align='left'),
    cells=dict(values=[abooks_nonfiction['Name'], # 1st column
                       abooks_nonfiction['Author']], # 2nd column
               line_color='darkslategray',
               fill_color= 'mistyrose',
               font_size=14,
               font_color='black',
               align='left'))
    ])


st.header('**Amazon Book Stats**')


st.subheader('Amazon\'s Top Rated')
with st.beta_expander('Based on bestsellers data from 2009-2019, click to view these hot titles!'):
    aselect = st.selectbox(' ',['Choose a category','Fiction','Non-Fiction'])
    if aselect == 'Non-Fiction':
        st.write(' '
    'note: scroll to see more!',atopnonfic_table)
    elif aselect == 'Fiction':
        st.write(' '
    'note: scroll to see more!', atopfic_table)
    else:
        st.write(' ')


abooks_sortedbyreview = abooks_nodupes.sort_values('Reviews', ascending=False)
abooks_sortedbyreview_top = abooks_sortedbyreview[0:10]
labels = abooks_sortedbyreview_top['Name']
values = abooks_sortedbyreview_top['Reviews']
colors = ['mistyrose', 'lightgray', 'lightyellow', 'powderblue','lightpink','navajowhite','lightseagreen','seashell','lavender','salmon']

topreviewedfig = go.Figure(data=[go.Pie(labels=labels, values=values)])
topreviewedfig.update_traces(hoverinfo='label+percent', textinfo='label',insidetextorientation='radial', textfont_size=14,
              marker=dict(colors=colors, line=dict(color='#000000', width=2)))
topreviewedfig.update_layout(
width=1700,
height=650,
)
topreviewedfig.update_layout(showlegend=False)

st.subheader('Amazon\'s Top Reviewed')
with st.beta_expander('Click to see the books that got reviewed the most, real conversation starters!'):
    topreviewedfig


st.subheader('Amazon Bestseller List Regulars')

bestsellernumberoftimes = amazonbooks['Name'].value_counts().rename_axis('Name').reset_index(name='Counts')

threetimes = bestsellernumberoftimes[bestsellernumberoftimes['Counts']==3]
fourtimes = bestsellernumberoftimes[bestsellernumberoftimes['Counts']==4]
fivetimes = bestsellernumberoftimes[bestsellernumberoftimes['Counts']==5]
sixtimes = bestsellernumberoftimes[bestsellernumberoftimes['Counts']==6]
seventimes = bestsellernumberoftimes[bestsellernumberoftimes['Counts']==7]
eighttimes = bestsellernumberoftimes[bestsellernumberoftimes['Counts']==8]

threefig = go.Figure(data=[go.Table(
    header=dict(values=['Title'],
                line_color='darkslategray',
                fill_color='lightgray',
                font_color='black',
                font_size=14,
                align='left'),
    cells=dict(values=[threetimes['Name']],
               line_color='darkslategray',
               fill_color= 'thistle',
               font_size=14,
               font_color='black',
               align='left'))
    ])

fourfig = go.Figure(data=[go.Table(
    header=dict(values=['Title'],
                line_color='darkslategray',
                fill_color='lightgray',
                font_color='black',
                font_size=14,
                align='left'),
    cells=dict(values=[fourtimes['Name']], # 2nd column
               line_color='darkslategray',
               fill_color= 'lightyellow',
               font_size=14,
               font_color='black',
               align='left'))
    ])

fivefig = go.Figure(data=[go.Table(
    header=dict(values=['Title'],
                line_color='darkslategray',
                fill_color='lightgray',
                font_color='black',
                font_size=14,
                align='left'),
    cells=dict(values=[fivetimes['Name']], # 2nd column
               line_color='darkslategray',
               fill_color= 'powderblue',
               font_size=14,
               font_color='black',
               align='left'))
    ])

sixfig = go.Figure(data=[go.Table(
    header=dict(values=['Title'],
                line_color='darkslategray',
                fill_color='lightgray',
                font_color='black',
                font_size=14,
                align='left'),
    cells=dict(values=[sixtimes['Name']], # 2nd column
               line_color='darkslategray',
               fill_color= 'lightseagreen',
               font_size=14,
               font_color='black',
               align='left'))
    ])

sevenfig = go.Figure(data=[go.Table(
    header=dict(values=['Title'],
                line_color='darkslategray',
                fill_color='lightgray',
                font_color='black',
                font_size=14,
                align='left'),
    cells=dict(values=[seventimes['Name']], # 2nd column
               line_color='darkslategray',
               fill_color= 'lightpink',
               font_size=14,
               font_color='black',
               align='left'))
    ])

eightfig = go.Figure(data=[go.Table(
    header=dict(values=['Title'],
                line_color='darkslategray',
                fill_color='lightgray',
                font_color='black',
                font_size=14,
                align='left'),
    cells=dict(values=[eighttimes['Name']], # 2nd column
               line_color='darkslategray',
               fill_color= 'mistyrose',
               font_size=14,
               font_color='black',
               align='left'))
    ])




with st.beta_expander('Click to view books that were best sellers for 3 years or more!'):
    st.write('slide to select X amount of years')
    bestyearsslider = st.slider('',min_value=3, max_value=8)
    if bestyearsslider == 3:
        threefig
    elif bestyearsslider == 4:
        fourfig
    elif bestyearsslider == 5:
        fivefig
    elif bestyearsslider == 6:
        sixfig
    elif bestyearsslider == 7:
        sevenfig
    else:
        eightfig


st.markdown('##')
st.image(lineimage)

#GOODREADS DATASET

st.header('**GoodReads Book Stats**')
st.subheader('Most Published Authors')


goodreads = pd.read_csv(goodreadsdata)
authors_bookcount = goodreads.groupby(['authors']).size().reset_index(name='Number of Books Written')


authorswithmostbooks = authors_bookcount.nlargest(10, ['Number of Books Written'])

authandavgrating = goodreads.filter(['authors','average_rating'],axis=1)
#authandavgratingg = authandavgrating.groupby('authors').mean('average_rating')
authandavgrating['average_rating']=pd.to_numeric(authandavgrating.average_rating, errors='coerce')
authandavgrating.info()

authandavgratingg = authandavgrating.groupby('authors').mean('average_rating')
authandavgratinggsorted = authandavgratingg.sort_values('average_rating',ascending= False)


authandavgratingg = authandavgratingg.reset_index('authors')
authandavgratingg.rename(columns={'average_rating':'Average Rating','authors':'Authors'},inplace=True)

#Used to find avg ratings to be included in the bar chart
pg = authandavgratingg[authandavgratingg['Authors']=='James Patterson']

data = go.Bar(x=authorswithmostbooks.authors,y=authorswithmostbooks['Number of Books Written'], marker=dict(color='#ffcdd2'),hovertext=['4.147 Avg Rating','3.974 Avg Rating','4.187 Avg Rating','3.779 Avg Rating','3.989 Avg Rating','3.717 Avg Rating','4.039 Avg Rating','3.742 Avg Rating','3.962 Avg Rating','3.906 Avg Rating'])
layout = go.Layout(xaxis=dict(title='Author'),yaxis=dict(title='Number of Books'))

with st.beta_expander('Click here to view the top ten most published authors according to Goodreads data'):
    bookswrittenfig= go.Figure(data=data, layout=layout)
    st.markdown('#')
    st.write('Hover over the bar graph to view the authors\' average rating. Is this a case of quantity over quality? You decide')
    bookswrittenfig

topratedauth = authandavgratinggsorted[0:18]
topratedauth.rename(columns={'average_rating':'Average Rating'},inplace=True)
topratedauth= topratedauth.reset_index('authors')

st.subheader('5 Star Rated Authors')
with st.beta_expander('These 18 authors\' average ratings are a perfect 5/5. Click to view.'):
    st.write('note: scroll to see more!')
    st.write('People seem to love these authors\' books! Perhaps they\'re worth looking into')
    fivestarauth = go.Figure(data=[go.Table(
    header=dict(values=['Author Name',],
                line_color='darkslategray',
                fill_color='lightgray',
                font_color='black',
                font_size=14,
                align='left'),
    cells=dict(values=[topratedauth['authors']],
               line_color='darkslategray',
               fill_color= 'lightseagreen',
               font_size=14,
               font_color='black',
               align='left'))
    ])
    fivestarauth


#Top text reviewed books!
st.subheader('Goodreads\' Top Reviewed')
gbooks_sortedbyreview = goodreads.sort_values('text_reviews_count', ascending=False)
gbooks_sortedbyreview_top = gbooks_sortedbyreview[0:10]

labels1= gbooks_sortedbyreview_top['title']
values1= gbooks_sortedbyreview_top['text_reviews_count']

with st.beta_expander('Click here to view the top ten text reviewed books on Goodreads.'):
    st.write('Comparing with Amazon\'s top reviewed books, we can see that they only have one book, \'The Alchemist\' in common' )
    grtopreviewedfig = go.Figure(data=[go.Pie(labels=labels1, values=values1)])
    grtopreviewedfig.update_traces(hoverinfo='label+percent', textinfo='label',insidetextorientation='radial', textfont_size=14, marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    grtopreviewedfig.update_layout(width=1700,height=650)
    grtopreviewedfig.update_layout(showlegend=False)
    grtopreviewedfig


st.image(lineimage)

##############BOOK RANDOMIZER##############


df = pd.read_csv(genrebooksdataset)

genres = ['signal_processing' 'data_science' 'mathematics' 'economics' 'history'
 'science' 'psychology' 'fiction' 'computer_science' 'nonfiction'
 'philosophy' 'comic']

datasciencebooks = df[df['Genre']=='data_science']
mathematicsbooks = df[df['Genre']=='mathematics']
economicsbooks = df[df['Genre']=='economics']
historybooks = df[df['Genre']=='history']
sciencebooks= df[df['Genre']=='science']
psychologybooks= df[df['Genre']=='psychology']
fictionbooks=df[df['Genre']=='fiction']
csbooks=df[df['Genre']=='computer_science']
nonfictionbooks=df[df['Genre']=='nonfiction']
philosophybooks=df[df['Genre']=='philosophy']
comicbooks=df[df['Genre']=='comic']

datasciencebooklist= datasciencebooks['Title'].tolist()
mathematicsbookslist= mathematicsbooks['Title'].tolist()
economicsbookslist = economicsbooks['Title'].tolist()
historybookslist = historybooks['Title'].tolist()
sciencebookslist = sciencebooks['Title'].tolist()
psycologybookslist = psychologybooks['Title'].tolist()
fictionbookslist = fictionbooks['Title'].tolist()
csbookslist =csbooks['Title'].tolist()
nonfictionbookslist = nonfictionbooks['Title'].tolist()
philosophybookslist = philosophybooks['Title'].tolist()
comicbookslist = comicbooks['Title'].tolist()

st.image(croppedheader)
st.header('**Book Randomizer**')
st.write('Follow the below steps to recieve your very own random book recommendation!')
st.markdown('#')
st.write('1. Select a book genre')
genreselect = st.selectbox(' ',['-','Data Science','Mathematics','Economics','History','Science','Psychology','Fiction','Computer Science','Non-Fiction','Philosophy','Comic'])
st.markdown('#')
st.write('2. Select the number of options you want to generate')
n = st.slider('',min_value=1,max_value=5)
st.markdown('#')

generatebutton = st.button('3. Click to generate!')

#IF statement for the book generator
if genreselect == 'Data Science' and generatebutton:
    st.write('Check out these options:',random.sample(datasciencebooklist,k=n))
    st.write('')
elif genreselect == 'Mathematics' and generatebutton:
    st.write('Check out these options:',random.sample(mathematicsbookslist,k=n))
    st.write('')
elif genreselect == 'Economics' and generatebutton:
    st.write('Check out these options:',random.sample(economicsbookslist,k=n))
    st.write('')
elif genreselect == 'History' and generatebutton:
    st.write('Check out these options:',random.sample(historybookslist,k=n))
    st.write('')
elif genreselect == 'Science' and generatebutton:
    st.write('Check out these options:',random.sample(sciencebookslist,k=n))
    st.write('')
elif genreselect == 'Psychology' and generatebutton:
    st.write('Check out these options:',random.sample(psycologybookslist,k=n))
    st.write('')
elif genreselect == 'Fiction' and generatebutton:
    st.write('Check out these options:',random.sample(fictionbookslist,k=n))
    st.write('')
elif genreselect == 'Computer Science' and generatebutton:
    st.write('Check out these options:',random.sample(csbookslist,k=n))
    st.write('')
elif genreselect == 'Non-Fiction' and generatebutton:
    st.write('Check out these options:',random.sample(nonfictionbookslist,k=n))
    st.write('')
elif genreselect == 'Philosophy' and generatebutton:
    st.write('Check out these options:',random.sample(philosophybookslist,k=n))
    st.write('')
elif genreselect == 'Comic' and generatebutton:
    st.write('Check out these options:',random.sample(comicbookslist,k=n))
    st.write('')
else:
    st.write('')

st.image(lineimage)

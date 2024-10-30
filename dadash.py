import pandas as pd
import kagglehub
import dash
from dash import dcc, html
import plotly.express as px
import ast
from collections import Counter

# Download latest version
path = kagglehub.dataset_download("lukebarousse/data-analyst-job-postings-google-search")
posts = pd.read_csv(f'{path}/gsearch_jobs.csv')

# Filter for Data Analyst posts
da_posts = posts[posts['search_term']=='data analyst']

# Select relevant columns
da_filter = da_posts[['title', 
                      'company_name',
                      'location',
                      'via',
                      'posted_at',
                      'schedule_type',
                      'work_from_home',
                      'salary',
                      'salary_pay',
                      'salary_hourly',
                      'salary_yearly',
                      'salary_standardized',
                      'description_tokens']]

# Data preparation for graphs
posted_in = da_filter.groupby('via')['title'].count().reset_index().sort_values(by='title', ascending=False).head(10)

# Fill NaN values for work_from_home
da_filter['work_from_home'].fillna('False', inplace=True)
remote_work = da_filter.groupby('work_from_home', as_index=False)['title'].count()

schedule_type = da_filter.groupby('schedule_type', as_index=False)['title'].count().sort_values(by='title', ascending=False).head()

da_filter['skills'] = da_filter['description_tokens'].apply(lambda x: ast.literal_eval(x) if x != '[]' else [])
flatlist = [item for sublist in da_filter['skills'] for item in sublist]
skill_count = Counter(flatlist)
skill_count_df = pd.DataFrame(skill_count.items(), columns=['skill', 'count'])
skill_count_df = skill_count_df.sort_values(by='count', ascending=False)
top_skills = skill_count_df.head(20)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Job Offers Dashboard"),
    
    # Graph 1: Where Are Job Offers Published?
    dcc.Graph(
        id='posted_in_graph',
        figure=px.bar(posted_in, x='via', y='title', title='WHERE ARE JOB OFFERS PUBLISHED?', color='title', color_continuous_scale='crimson')
    ),
    
    # Graph 2: Remote Jobs
    dcc.Graph(
        id='remote_work_graph',
        figure=px.bar(remote_work, x='work_from_home', y='title', title='IS THE JOB POST REMOTE?', color='title', color_continuous_scale='dark')
    ),
    
    # Graph 3: Type of Schedule
    dcc.Graph(
        id='schedule_type_graph',
        figure=px.bar(schedule_type, x='schedule_type', y='title', title='TYPE OF SCHEDULE', color='title', color_continuous_scale='dark')
    ),
    
    # Graph 4: Most Demanded Skills
    dcc.Graph(
        id='top_skills_graph',
        figure=px.bar(top_skills, x='skill', y='count', title='MOST DEMANDED SKILLS', color='count', color_continuous_scale='dark')
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

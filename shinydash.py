import pandas as pd
import kagglehub
import plotly.express as px
from shiny import App, render, ui, reactive
import ast
from collections import Counter

# Download latest version
path = kagglehub.dataset_download("lukebarousse/data-analyst-job-postings-google-search")
posts = pd.read_csv(f'{path}/gsearch_jobs.csv')

# Filter for "data analyst" jobs
da_posts = posts[posts['search_term'] == 'data analyst']
da_filter = da_posts[['title', 'company_name', 'location', 'via', 'posted_at', 
                      'schedule_type', 'work_from_home', 'salary', 'description_tokens']]

# Prepare data for different sections of the dashboard
da_filter['work_from_home'].fillna('False', inplace=True)
posted_in = da_filter.groupby('via')['title'].count().reset_index().sort_values(by='title', ascending=False).head(10)
remote_work = da_filter.groupby('work_from_home')['title'].count().reset_index()
schedule_type = da_filter.groupby('schedule_type')['title'].count().reset_index().sort_values(by='title', ascending=False).head()

# Skill extraction
da_filter['skills'] = da_filter['description_tokens'].apply(lambda x: ast.literal_eval(x) if x != '[]' else [])
flatlist = [item for sublist in da_filter['skills'] for item in sublist]
skill_count = Counter(flatlist)
skill_count_df = pd.DataFrame(skill_count.items(), columns=['skill', 'count']).sort_values(by='count', ascending=False)
top_skills = skill_count_df.head(20)

# Define the Shiny app
app_ui = ui.page_fluid(
    ui.h1("Data Analyst Job Postings Dashboard"),
    
    ui.layout_sidebar(
        ui.page_sidebar(
            ui.h3("Filter Options"),
            ui.input_select("remote", "Remote Work:", {"All": "All", "True": "True", "False": "False"}),
        ),
        
        ui.panel_main(
            ui.h2("Where are Job Offers Published?"),
            ui.output_plot("posted_in_plot"),
            
            ui.h2("Is the Job Post Remote?"),
            ui.output_plot("remote_work_plot"),
            
            ui.h2("Type of Schedule"),
            ui.output_plot("schedule_type_plot"),
            
            ui.h2("Most Demanded Skills"),
            ui.output_plot("skills_plot")
        )
    )
)

def server(input, output, session):
    # Filtered dataset
    @reactive.Calc
    def filtered_data():
        if input.remote() == "All":
            return da_filter
        else:
            return da_filter[da_filter['work_from_home'] == input.remote()]

    # Plots
    @output
    @render.plot
    def posted_in_plot():
        fig = px.bar(posted_in, x='via', y='title', title='WHERE ARE JOB OFFERS PUBLISHED?', color='title')
        return fig

    @output
    @render.plot
    def remote_work_plot():
        fig = px.bar(remote_work, x='work_from_home', y='title', title='IS THE JOB POST REMOTE?', color='title')
        return fig

    @output
    @render.plot
    def schedule_type_plot():
        fig = px.bar(schedule_type, x='schedule_type', y='title', title='TYPE OF SCHEDULE', color='title')
        return fig

    @output
    @render.plot
    def skills_plot():
        fig = px.bar(top_skills, x='skill', y='count', title='MOST DEMANDED SKILLS', color='count')
        return fig

app = App(app_ui, server)

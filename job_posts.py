import pandas as pd
import kagglehub
from matplotlib import pyplot as plt
import seaborn as sns
import ast
from collections import Counter


import dash
from dash import dcc, html
import plotly.express as px


# Download latest version
path = kagglehub.dataset_download("lukebarousse/data-analyst-job-postings-google-search")
posts = pd.read_csv(f'{path}/gsearch_jobs.csv')

posts.head()
posts.info()

da_posts = posts[posts['search_term']=='data analyst']
da_posts.info()
da_posts.columns.tolist()
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
da_filter.info()

# Prepare data for plot
posted_in = da_filter.groupby('via')['title'].count().reset_index().sort_values(by='title', ascending=False).head(10)
posted_in['via'] = posted_in['via'].str.replace('via ', '', regex=False)
posted_in['via'] = posted_in['via'].str.replace('Jobs ', '', regex=False)
da_filter['work_from_home'].fillna('False', inplace=True)
remote_work = da_filter.groupby('work_from_home', as_index=False)['title'].count()
schedule_type = da_filter.groupby('schedule_type', as_index=False)['title'].count().sort_values(by='title', ascending=False).head()

da_filter['skills'] = da_filter['description_tokens'].apply(lambda x: ast.literal_eval(x) if x != '[]' else [])
flatlist = [item for sublist in da_filter['skills'] for item in sublist]
skill_count = Counter(flatlist)
skill_count_df = pd.DataFrame(skill_count.items(), columns=['skill', 'count']).sort_values(by='count', ascending=False)
top_skills = skill_count_df.head(20)

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

#WHERE ARE JOB OFFERS PUBLISHED?
sns.barplot(data=posted_in, x='via', y='title', color='crimson', ax=axs[0, 0])
axs[0, 0].set_xlabel('Posted In')
axs[0, 0].set_ylabel('Count')
axs[0, 0].set_title('WHERE ARE JOB OFFERS PUBLISHED?')
axs[0, 0].tick_params(axis='x', rotation=30)

#IS THE JOB POST REMOTE?
sns.barplot(data=remote_work, x='work_from_home', y='title', palette='dark', ax=axs[0, 1])
axs[0, 1].set_xlabel('Remote')
axs[0, 1].set_ylabel('Count')
axs[0, 1].set_title('IS THE JOB POST REMOTE?')

#TYPE OF SCHEDULE
sns.barplot(data=schedule_type, x='schedule_type', y='title', palette='dark', ax=axs[1, 0])
axs[1, 0].set_xlabel('Schedule')
axs[1, 0].set_ylabel('Count')
axs[1, 0].set_title('TYPE OF SCHEDULE')
axs[1, 0].tick_params(axis='x', rotation=30)

#MOST DEMANDED SKILLS
sns.barplot(data=top_skills, x='skill', y='count', palette='dark', ax=axs[1, 1])
axs[1, 1].set_xlabel('Skills')
axs[1, 1].set_ylabel('Count')
axs[1, 1].set_title('MOST DEMANDED SKILLS')
axs[1, 1].tick_params(axis='x', rotation=50)

fig.suptitle('DATA ANALYST JOB OFFERS REPORT', fontsize=16)

plt.tight_layout()
plt.show()
report_screen = fig
report_screen.savefig('job_postings_dashboard.jpeg', bbox_inches='tight')
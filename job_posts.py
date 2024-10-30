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

# WHERE ARE THE JOBS?
posted_in = da_filter.groupby('via')['title'].count().reset_index().sort_values(by='title', ascending = False).head(10)
sns.set_style("darkgrid")
plt.figure()
sns.barplot(data=posted_in, x = 'via', y = 'title', color = 'crimson')
plt.xlabel('Posted In')
plt.ylabel('Count')
plt.title('WHERE ARE JOB OFFERS PUBLISHED?')
plt.xticks(rotation=45)
plt.show()
da_filter['work_from_home'].shape


# REMOTE JOBS
da_filter['work_from_home'].fillna('False', inplace=True)
remote_work = da_filter.groupby('work_from_home', as_index = False)['title'].count()
plt.figure()
sns.barplot(data = remote_work, x = 'work_from_home', y = 'title', palette = 'dark')
plt.xlabel('Remote')
plt.ylabel('Count')
plt.title('IS THE JOB POST REMOTE?')
plt.show()

#SALARY 


#SCHEDULE
da_filter['schedule_type'].value_counts()
schedule_type = da_filter.groupby('schedule_type', as_index=False)['title'].count().sort_values(by='title', ascending=False).head()

plt.figure()
sns.barplot(data = schedule_type, x = 'schedule_type', y = 'title', palette = 'dark')
plt.xlabel('Schedule')
plt.ylabel('Count')
plt.title('TYPE OF SCHEDULE')
plt.xticks(rotation=30)
plt.show()



da_filter['skills'] = da_filter['description_tokens'].apply(lambda x: ast.literal_eval(x) if x != '[]' else [])
flatlist = [item for sublist in da_filter['skills'] for item in sublist]
skill_count = Counter(flatlist)
skill_count_df = pd.DataFrame(skill_count.items(), columns=['skill', 'count'])
skill_count_df = skill_count_df.sort_values(by='count', ascending=False)
top_skills = skill_count_df.head(20)

# skills required
plt.figure()
sns.barplot(data=top_skills, x = 'skill', y = 'count', palette = 'dark')
plt.xticks(rotation = 50)
plt.xlabel('Skills')
plt.title('MOST DEMANDED SKILLS')
plt.show()


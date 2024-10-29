import pandas as pd
import kagglehub
from matplotlib import pyplot as plt
import seaborn as sns


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
                      'location','via',
                      'posted_at',
                      'schedule_type',
                      'work_from_home',
                      'salary',
                      'date_time',
                      'search_location',
                      'salary_pay',
                      'salary_hourly',
                      'salary_yearly',
                      'salary_standardized',
                      'description_tokens']]
da_filter.info()

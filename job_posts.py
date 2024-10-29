import pandas as pd
import kagglehub


# Download latest version
path = kagglehub.dataset_download("lukebarousse/data-analyst-job-postings-google-search")
posts = pd.read_csv(f'{path}/gsearch_jobs.csv')

posts.head()
posts.info()

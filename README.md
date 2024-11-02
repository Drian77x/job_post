# DATA ANALYST JOB OFFERS SCANNER
This project uses a job postings database in the data field, updated daily, to gather insights on job vacancy trends, helping job seekers identify where to look and apply to maximize hiring opportunities.

While the database includes information on various fields, I will focus exclusively on Data Analyst positions, which align with my personal interest.

## Objectives
The analysis covers four key aspects:

### **Where to Look**
Identifying the websites with the most postings provides insight into where the highest number of opportunities are available.

### **Remote or Onsite Jobs**
Although the database contains U.S.-based postings only, knowing which positions offer remote work helps broaden access to candidates globally.

### **Type of Schedule**
Are the positions full-time, part-time, or contract-based? This information offers job seekers a better understanding of the expected work schedules.

### **Most Demanded Skills**
Identifying frequently requested skills reveals the tools and knowledge areas job seekers should prioritize for career preparation.

## How Does It Work?

The code first connects to a dataset hosted by Luke Barousse in kaggle (https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search) which is updated daily with new vacancies. After that, filters and processes the data to obtain a graphic answering the objective questions.
Each time the code is run, returns the plot with the updated dataset and a timestamp indicating when it was last refreshed.

 At the time of this iteration the plot was as it follows:
![Data Analyst Job Offers Report](/job_postings_dashboard.jpeg)


## Analysis Results

### 1. **Where Are Job Offers Published?**
The analysis shows that **LinkedIn** is the leading platform for Data Analyst job postings, followed by **Upwork** and **BeBee**. This suggests that job seekers should prioritize these platforms for their applications.

### 2. **Is the Job Post Remote?**
A significant majority of job postings are marked as remote, indicating a trend towards flexible working conditions. This opens opportunities for candidates worldwide, not just those located near job sites.

### 3. **Type of Schedule**
The analysis reveals that most positions are **full-time**, with a smaller number of part-time and contract roles. Job seekers can expect the majority of opportunities to align with full-time employment.

### 4. **Most Demanded Skills**
The most sought-after skills in the job market include **SQL**, **Excel**, and **Python**, followed by **Power BI** and **Tableau**. This information is crucial for aspiring Data Analysts to tailor their skill development and learning paths.

## Conclusions
- LinkedIn and Upwork are the primary platforms for Data Analyst positions, making them essential for job seekers.
- Remote work options are prevalent, providing flexibility for applicants.
- Full-time roles dominate the job market, indicating a strong demand for dedicated professionals.
- Mastering key skills such as SQL, Excel, and Python will enhance employability and align with market needs.

## Recommendations
- **Job Seekers**: Focus your applications on LinkedIn and Upwork. Highlight your skills in SQL, Excel, and Python in your resume and cover letters.
- **Skill Development**: Invest time in learning tools like PowerBI and Tableau to further enhance your skill set.
- **Networking**: Engage with communities on platforms like LinkedIn to stay informed about trends and connect with potential employers.

## Future Work
Although the objectives of this projects were quite specific, this same dataset can be used to answer a wide range of questions such as regional variations in job postings, salary trends, job requirements across different industries or many others.



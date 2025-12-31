# US_data_jobs_2025
This project is a preliminary data analysis and visualization project used with real-time data extracted through adzuna.com using their API. The goal is to extract general patterns of salary distribution across data job categories, titles and seniority levels. 


This project has two primary steps:

1) Data Formation: Extract different types of data-related jobs from adzuna.com using their API using a Python script. Filter data only to US jobs in 2025.
   Tools: Python
2) Data Visualization: Create graphs to showcase impacts of various variables such as job category, job title, seniority and month on maximum salary defined in the job description.
   Tools: Tableau
   Link to Dashboard: https://public.tableau.com/app/profile/betul.erbasi.yilmaz/viz/USDataJobs2025/USDataJobs2025?publish=yes


Data Patterns:

1) IT (including Software Engineers, Data Analyst, Data Engineers) and Engineering jobs (including Structural Engineer, Sales Engineer) categories  have the highest maximum salaries. They are also the only ones with a salary range for all levels available in the data.
   Note: If salary range is 0, that means maximum and minimum salaries were the same for that listing. There are many such jobs in the data, hence I used averages for range visualizations instead of the median.

2) Across categories, senior levels tend to be paid more than mid level. However, in some categories, junior levels get paid more than mid or senior levels. This might be due to a categorization issue in the data. For example, Junior Software Engineer (Graduate) job is categorized as a graduate job, becoming the junior level outlier in this category. However, it would correctly be categorized as an IT job. The other category with this pattern is accounting jobs, where Junior/Entry Budget Analyst has a higher salary as a junior/entry level. It is hard to say why just based on this data. This requires a bigger set of accounting jobs to come to conclusion.

3) The data on salaries by job titles are skewed due to an outlier with $300k max salary while most of the rest is in $150k-$160k range. This can be solved with a more comprehensive data set. 

4) June was the month when jobs with the highest salaries were posted. However, when I look at the real data, this is due to June not having many postings (only 2). There were more jobs posted in December, including the highest salaries. However, since there were also low-salary jobs in that month, the results did not appear as high as June in the visualization. The best solution to determine if these are actual patterns would be to compare data over years. If jobs posted in June consistently have higher max salaries, then we can confirmthis to be a pattern. 



Next Steps:

This is a preliminary analysis on salaries of data jobs in the US in 2025. As mentioned in the patterns sections , a more comprehensive data would yield better results. As the next step, I will work on a bigger data set with at least 100 jobs per category and at least 5 per job title. 



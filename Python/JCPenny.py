# University of Stirling

# ITNPBD2 Representing and Manipulating Data

# Assignment Autumn 2023

# A Consultancy Job for JC Penney

This notebook forms the assignment instructions and submission document of the assignment for ITNPBD2. Read the instructions carefully and enter code into the cells as indicated.

You will need these five files, which were in the Zip file you downloaded from the course webpage:

- jcpenney_reviewers.json
- jcpenney_products.json
- products.csv
- reviews.csv
- users.csv

The data in these files describes products that have been sold by the American retail giant, JC Penney, and reviews by customers who bought them. Note that the product data is real, but the customer data is synthetic.

Your job is to process the data, as requested in the instructions in the markdown cells in this notebook.

# Completing the Assignment

Rename this file to be xxxxxx_BD2 where xxxxxx is your student number, then type your code and narrative description into the boxes provided. Add as many code and markdown cells as you need. The cells should contain:

- **Text narrative describing what you did with the data**
- **The code that performs the task you have described**
- **Comments that explain your code**

# Marking Scheme
The assessment will be marked against the university Common Marking Scheme (CMS)

Here is a summary of what you need to achieve to gain a grade in the major grade bands:

|Grade|Requirement|
|:---|:---|
| Fail | You will fail if your code does not run or does not achieve even the basics of the task. You may also fail if you submit code without either comments or a text explanation of what the code does.|
| Pass | To pass, you must submit sufficient working code to show that you have mastered the basics of the task, even if not everything works completely. You must include some justifications for your choice of methods, but without mentioning alternatives. |
| Merit | For a merit, your code must be mostly correct, with only small problems or parts missing, and your comments must be useful rather than simply re-stating the code in English. Most choices for methods and structures should be explained and alternatives mentioned. |
| Distinction | For a distinction, your code must be working, correct, and well commented and shows an appreciation of style, efficiency and reliability. All choices for methods and structures are concisely justified and alternatives are given well thought considerations. For a distinction, your work should be good enough to present to executives at the company.|

The full details of the CMS can be found here

https://www.stir.ac.uk/about/professional-services/student-academic-and-corporate-services/academic-registry/academic-policy-and-practice/quality-handbook/assessment-policy-and-procedure/appendix-2-postgraduate-common-marking-scheme/

Note that this means there are not certain numbers of marks allocated to each stage of the assignment. Your grade will reflect how well your solutions and comments demonstrate that you have achieved the learning outcomes of the task. 

## Submission
When you are ready to submit, **print** your notebook as PDF (go to File -> Print Preview) in the Jupyter menu. Make sure you have run all the cells and that their output is displayed. Any lines of code or comments that are not visible in the pdf should be broken across several lines. You can then submit the file online.

Late penalties will apply at a rate of three marks per day, up to a maximum of 7 days. After 7 days you will be given a mark of 0. Extensions will be considered under acceptable circumstances outside your control.

## Academic Integrity

This is an individual assignment, and so all submitted work must be fully your own work.

The University of Stirling is committed to protecting the quality and standards of its awards. Consequently, the University seeks to promote and nurture academic integrity, support staff academic integrity, and support students to understand and develop good academic skills that facilitate academic integrity.

In addition, the University deals decisively with all forms of Academic Misconduct.

Where a student does not act with academic integrity, their work or behaviour may demonstrate Poor Academic Practice or it may represent Academic Misconduct.

### Poor Academic Practice

Poor Academic Practice is defined as: "The submission of any type of assessment with a lack of referencing or inadequate referencing which does not effectively acknowledge the origin of words, ideas, images, tables, diagrams, maps, code, sound and any other sources used in the assessment."

### Academic Misconduct

Academic Misconduct is defined as: "any act or attempted act that does not demonstrate academic integrity and that may result in creating an unfair academic advantage for you or another person, or an academic disadvantage for any other member or member of the academic community."

Plagiarism is presenting somebody else’s work as your own **and includes the use of artificial intelligence tools such as GPT or CoPilot**. Plagiarism is a form of academic misconduct and is taken very seriously by the University. Students found to have plagiarised work can have marks deducted and, in serious cases, even be expelled from the University. Do not submit any work that is not entirely your own. Do not collaborate with or get help from anybody else with this assignment.

The University of Stirling's full policy on Academic Integrity can be found at:

https://www.stir.ac.uk/about/professional-services/student-academic-and-corporate-services/academic-registry/academic-policy-and-practice/quality-handbook/academic-integrity-policy-and-academic-misconduct-procedure/

## The Assignment
Your task with this assignment is to use the data provided to demonstrate your Python data manipulation skills.

There are three `.csv` files and two `.json` files so you can process different types of data. The files also contain unstructured data in the form of natural language in English and links to images that you can access from the JC Penney website (use the field called `product_image_urls`).

Start with easy tasks to show you can read in a file, create some variables and data structures, and manipulate their contents. Then move onto something more interesting.

Look at the data that we provided with this assessment and think of something interesting to do with it using whatever libraries you like. Describe what you decide to do with the data and why it might be interesting or useful to the company to do it.

You can add additional data if you need to - either download it or access it using `requests`. Produce working code to implement your ideas in as many cells as you need below. There is no single right answer, the aim is to simply show you are competent in using python for data analysis. Exactly how you do that is up to you.

For a distinction class grade, this must show originality, creative thinking, and insights beyond what you've been taught directly on the module.

## Structure
You may structure the project how you wish, but here is a suggested guideline to help you organise your work:

 1. Data Exploration - Explore the data and show you understand its structure and relations
 2. Data Validation - Check the quality of the data. Is it complete? Are there obvious errors?
 3. Data Visualisation - Gain an overall understanding of the data with visualisations
 4. Data Analysis = Set some questions and use the data to answer them
 5. Data Augmentation - Add new data from another source to bring new insights to the data you already have

# Remember to make sure you are working completely on your own.
# Don't work in a group or with a friend
You may NOT use any automated code generation or analytics tools for this assignment, so do not use tools like GPT. You can look up the syntax for the functions you use, but you must write the code yourself and the comments must provide an insightful analysis of the results.



# Assignment Solutions

I will address the problem by working with the two different files provided namely CSV and JSON, to proffer insights that the organization, JCPenny can use to gain a competitive advantage in whatever way possible. Hence, my workings is structured as follows:
- Working with the CSV Files
- Working with JSON Files

# Working with CSV files

## Data Exploration
First, I will load the dataset consisting users.csv, reviews.csv, and products.csv in a bid to gain an empirical understanding of what they contain. This will aid in comprehending the organisation of the data, including the arrangement of columns and the nature of the information therein.

# Using Panda library, i initiated the process of loading the data for inspection
import pandas as pd
import json

# Parse the CSV files and allocate the resulting data to three distinct variables.
Product_files = pd.read_csv('/Users/Hannah/Documents/JCPenneyFiles/products.csv')
Review_files = pd.read_csv('/Users/Hannah/Documents/JCPenneyFiles/reviews.csv')
User_files = pd.read_csv('/Users/Hannah/Documents/JCPenneyFiles/users.csv')

# Displays the initial few elements of each DataFrame in order to comprehend their structure.
(Product_files.head(), Review_files.head(), User_files.head())


## Insights

An understanding of the file content is summarized as follows:

## User_files
- Username: User identifier
- DOB: Date of birth of the user
- State: State where the user resides

## Review_files
- Uniq_id: Unique identifier for a product
- Username: User identifier (links to user_files)
- Score: Review score given by the user
- Review: Text of the review

## Product_files
- Uniq_id: Unique identifier for a product (links to review_files)
- SKU: Stock Keeping Unit, a unique identifier for each product
- Name: Name of the product
- Description: Description of the product
- Price: Price of the product
- Av_Score: Average score of the product (derived from reviews)

## Data Validation
To accomplish this, I will need to manipulate the data in a manner that facilitates value management, corrects data types and combine data from other files to discover their links. Therefore, the following outline the steps that is taken to validate the data to include:

   - Merging the different data sources to have an understanding of the data we have. For instance, linking user data with their reviews and the products they have reviewed. 
   - Transform DOB in order to get the year for age calculation


# Checking for missing values in each DataFrame
missing_values = {
    "products_missing": Product_files.isnull().sum(),
    "reviews_missing": Review_files.isnull().sum(),
    "users_missing": User_files.isnull().sum()
}

# Checking for duplicate entries
duplicate_counts = {
    "products_duplicates": Product_files.duplicated().sum(),
    "reviews_duplicates": Review_files.duplicated().sum(),
    "users_duplicates": User_files.duplicated().sum()
}

# Checking data types
data_types = {
    "products_data_types": Product_files.dtypes,
    "reviews_data_types": Review_files.dtypes,
    "users_data_types": User_files.dtypes
}

missing_values, duplicate_counts, data_types



Handling missing values in Product_files and data type conversion

# Handling missing values in Product_files
# Create a copy to avoid SettingWithCopyWarning
product_files_clean = Product_files.copy()

# Dropping rows with missing 'SKU' and 'Description'
product_files_clean.dropna(subset=['SKU', 'Description'], inplace=True)

# Filling missing 'Price' with the mean price
mean_price = product_files_clean['Price'].mean()
product_files_clean['Price'].fillna(mean_price, inplace=True)

# Converting 'DOB' in users_df to datetime format
User_files['DOB'] = pd.to_datetime(User_files['DOB'], errors='coerce', format='%d.%m.%Y')

# Rechecking for missing values and data types after cleaning
cleaned_data_info = {
    "products_missing_after": product_files_clean.isnull().sum(),
    "users_data_types_after": User_files.dtypes
}

cleaned_data_info


## Insights
Sequel to the task performed, the resulting outcome showed that the products_missing_after is devoid of entries and the DOB in the user_files converted for further analysis.

Next in the validation process is the construct of three (3) important tasks which will enable the type of analysis envisage with the files as listed below: 
 - Merge products and reviews DataFrames based on their unique identifier
 - Merge the outcome DataFrame from the combination above with the users DataFrame in order to connect the customers with their Username.
 - Convert DOB to datetime and extract year for age calculation

# Combining products and reviews DataFrames based on the unique identifier
products_reviews_files = pd.merge(Product_files, Review_files, on='Uniq_id', how='inner')

# Merging products_reviews_files DataFrame with the users DataFrame based on the 'Username'.
combined_files = pd.merge(products_reviews_files, User_files, on='Username', how='left')

# Convert DOB to datetime and extract year for age calculation
combined_files['DOB'] = pd.to_datetime(combined_files['DOB'], errors='coerce', format='%d.%m.%Y')
current_year = pd.Timestamp.now().year
combined_files['Age'] = current_year - combined_files['DOB'].dt.year

# Show the initial rows of the combined DataFrame.
combined_files.head()

## Insights
The merging of product, review, and user data into a single DataFrame enables a comprehensive analysis of JCPenny's consumer behaviour. In most cases, merging in consumer-related dataset help correlate user demographics (such as age, which is calculated from the DOB) with their preference and purchasing habits.

Also, the identification of demographic trends in product preferences or review tendencies could be a key outcome of this analysis. For example, the analysis may infer that certain products are more popular among certain age groups, or that a user's age influences their proclivity to leave a review. Such information can be extremely useful for targeted marketing, product development, and improving customer satisfaction.

Furthermore, sentiment analysis on the reviews, determining customer satisfaction across different age groups, or analysing the frequency of purchases and reviews based on user demographics can also be deduced from this datasets.

## Data analysis and visualisation
In relation to the aforementioned insights, the proposed analytical suggestions may include. This may involve examining product popularity, review trends, user behaviour and demographics among other factors. And to fully comprehend this, I will employ visual representations to effectively demonstrate these discernments.

The analysis and visualisation is classified into three (3) to posit a meaningful insights:

- Product Analysis
- Review Analysis
- User Demographics

## Products Analysis
I am employing this type of Analysis to enable me examine the distribution of product prices and their average scores for us to ascertain their range.

import matplotlib.pyplot as plt
import seaborn as sns


# Distribution of product prices
plt.figure(figsize=(6, 3))
sns.histplot(product_files_clean['Price'], kde=True)
plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Average rating per product
plt.figure(figsize=(6, 3))
sns.histplot(product_files_clean['Av_Score'], bins=10, kde=True)
plt.title('Distribution of Average Product Ratings')
plt.xlabel('Average Rating')
plt.ylabel('Frequency')
plt.show()


## Insights
- Distribution of Product Prices - The histogram of product prices shows a right-skewed distribution, suggesting that most products are in a lower price range, with fewer products having higher prices.

- Distribution of Average Product Scores - The average product scores are approximately normally distributed, with most products receiving scores around the middle of the range (around 2.5 to 3.5 out of 5). This indicates a general trend of moderate satisfaction among customers.

## Review Analysis
One of the usefulness of this kind of analysis employed is to analyze the distribution of review scores and see if there is any pattern in the review texts related to the scores.

# Review distribution by state
state_review_distribution = combined_files['State'].value_counts().head(10)

# Review distribution by age group
bins = [0, 18, 30, 40, 50, 60, 70, 80, 100]
labels = ['<18', '18-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
combined_files['Age_Group'] = pd.cut(combined_files['Age'], bins=bins, labels=labels, right=False)
age_group_review_distribution = combined_files['Age_Group'].value_counts()

# Setting up the figure for plotting
plt.figure(figsize=(12, 4))

# Plotting review distribution by state
plt.subplot(1, 2, 1)
sns.barplot(x=state_review_distribution.values, y=state_review_distribution.index, palette="coolwarm")
plt.title('Top 10 States by Number of Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('State')

# Plotting review distribution by age group
plt.subplot(1, 2, 2)
age_group_review_distribution.sort_index().plot(kind='bar', color='teal')
plt.title('Number of Reviews by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Reviews')

plt.tight_layout()
plt.show()

This distribution is critical for comprehending customer behaviour across age groups. For example, if a certain age group is more active in writing reviews, it could indicate their purchasing power or interest in JC Penney products. Marketing and product development strategies can be tailored to the preferences and feedback of the most active age groups. As an instance, if the '30-40' age group is the most active, products and marketing campaigns can be tailored to their interests and needs.

## Insights

- Review Distribution by State:
The bar chart depicting the top ten states by number of reviews indicates which geographic areas are most active in product reviews. This could be due to JC Penney's strong customer base or the most effective marketing efforts.

States with a higher number of reviews may represent areas with higher sales volume or brand engagement. This information could be used by JC Penney for targeted marketing campaigns or store promotions.

- Review Distribution by Age Group:
The classification of users into age groups and analysis of their review contributions reveals which age demographics are most active in providing feedback.


- The comparison of state and age group distributions in reviews provides a comprehensive picture of JC Penney's customer engagement across multiple dimensions.

These insights could be critical in developing region- and age-specific strategies, allowing JC Penney to better align its marketing efforts and product offerings with customer preferences and behaviours. It also provides a deeper understanding of the customer base and assists in making  more informed business decisions, ensuring that resources are allocated effectively to meet the needs and preferences of key customer segments.

# Analyzing review scores
plt.figure(figsize=(7,3))
sns.countplot(x='Score', data=Review_files)
plt.title('Distribution of Review Scores')
plt.xlabel('Score')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# Dividing reviews into high and low scores
# Considering scores 4 and 5 as high, and 1 and 2 as low
high_score_reviews = Review_files[Review_files['Score'] >= 4]['Review']
low_score_reviews = Review_files[Review_files['Score'] <= 2]['Review']

(high_score_reviews.head(), low_score_reviews.head())

## Insights
The analysis of review scores indicates a prevalence of high ratings (4 or 5), implying a generally pleasant reception from customers. Moreover, a considerable proportion of reviews exhibit ratings of 1 or 2, suggesting a degree of discontentment among specific customers.

## Text Analytics

Using a python library known as Wordcloud, which helps provide a rapid and visual means to assess the sentiment and repeating motifs in the customer reviews in order to have a comprehensive understanding of the commonly used terms in the  dataset which can be beneficial for JC Penney in effectively addressing consumer complaints and enhancing product descriptions, size recommendations, and return policies where applicable. Hence, The following formed the basis of the analysis carried out:

- Common Words in High Score Reviews
- Common Words in Low Score Reviews

# In order to perform text analytics, python libraries such as wordcloud is imported into the code for the analytics to work
from wordcloud import WordCloud

# This function is used to create and present the most prevalent words in the reviews.
def generate_word_cloud(text_series, title):
    text = ' '.join(review for review in text_series if type(review) == str)
    wordcloud = WordCloud(width=600, height=300, background_color='white').generate(text)
    plt.figure(figsize=(6, 3))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Using wordcloud to review high and low scores.
generate_word_cloud(high_score_reviews, 'Common Words in High Score Reviews')
generate_word_cloud(low_score_reviews, 'Common Words in Low Score Reviews')


## Insights
- The high score reviews demonstrates a notable inclination towards positive words such as "great", "love", "good", and "comfortable". This suggests that contented customers tend to prioritise the product's quality, comfort, and overall favourable attributes.

- Contrastingly, the negative reviews contained terms such as "size", "fit", "return", and "small". This indicates that customers often express unhappiness with issues pertaining to sizing, fit, and potentially the return procedure.

## User Demographics
This is another analysis we implore using the following as our criteria to draw more insights:
- Age Distribution of Users
- State-wise Distribution of Users

## Age Distribution of Users
Analyze the age distribution of users who have provided reviews. We'll need to calculate the age from the date of birth (DOB) provided.

# Plotting the age distribution
plt.figure(figsize=(8, 4))
sns.histplot(combined_files['Age'].dropna(), bins=30, kde=True)  # Dropping NaN values for age
plt.title('Age Distribution of Users')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


## Insights

The histogram displayed the demographic breakdown of reviewers based on their age. Although, the distribution seems to be quite broad, suggesting a heterogeneous range of ages among the users. There is also a conspicuous clustering of users among specific age ranges, which may suggest significant demographic groupings for JC Penney. While there are no missing age values recorded, it was successful computing the ages for all 5,000 users in the dataset. 

Conclusively, the age distribution can serve as a valuable tool for targeted marketing strategies and for determining which age segments exhibit the highest level of engagement when it comes to offering feedback. And by customising product offerings to these key age groups, marketing campaigns and customer service in JC Penney can enhance their ability to cater to their requirements.

## State-wise distribution of users
Understand the geographic distribution of users by analyzing the number of users from each state.

# State-wise distribution of users 
state_counts = User_files['State'].value_counts()

# Plotting the state-wise distribution
plt.figure(figsize=(10, 4))
state_counts.plot(kind='bar')
plt.title('State-wise Distribution of Users')
plt.xlabel('State')
plt.ylabel('Number of Users')
plt.grid(True)
plt.show()

# Getting the top 10 and lowest 5 states
top_10_states = state_counts.head(10)
lowest_5_states = state_counts.tail(5)

# Combining the top 10 and lowest 5 states
combined_states = pd.concat([top_10_states, lowest_5_states])

# Displaying the top 10 and lowest 5 states
print("Top 10 States:\n", top_10_states)
print("\nLowest 5 States:\n", lowest_5_states)



## Insights
The bar chart visually represents the user distribution among various jurisdictions. As it reveals, the user population is dispersed among several states, although certain states are significantly more represented than others as shown in the generated listed, namely top 10 and lowest 5 states.


The widespread distribution of JC Penney's patronage in specific states indicates the presence of regional preferences or market dominance. To this end, regional marketing strategies, inventory distribution, and store selections may find this information to be of great value.

In conclusion, both the age and state-wise distributions offer a more comprehensive insight into JC Penney's client demographic. These insights can be utilised to develop targeted marketing campaigns, enhance customer service, and customise product offers to cater to the requirements of specific demographic segments.

# Working with JSON files

## Data Exploration
Just like the CSV file process above, I will first load the dataset consisting of products.json, and reviewers.json in a bid to gain an empirical understanding of what they contain. This will aid in comprehending the structure of the data, including the arrangement of columns and the nature of the information.

import json
import pandas as pd

# A function that loads json with multiple objects
def load_json_with_multiple_objects(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                json_object = json.loads(line)
                data.append(json_object)
            except json.JSONDecodeError:
                continue  # Skip lines that are not valid JSON
    return data

# Load the JSON files
json_product_data = load_json_with_multiple_objects('/Users/Hannah/Documents/JCPenneyFiles/jcpenney_products.json')
json_review_data = load_json_with_multiple_objects('/Users/Hannah/Documents/JCPenneyFiles/jcpenney_reviewers.json')

# Convert the JSON files to DataFrame
json_product_files = pd.DataFrame(json_product_data)
json_review_files = pd.DataFrame(json_review_data)

# Output the top lines of each DataFrame
(json_product_files.head(), json_review_files.head())


Based on the output, the content reveals DataFrames structure as follows:

 ## json_product_files (Product Information)
 This DataFrame contains detailed information about products. The key columns include:
  - uniq_id: A unique identifier for each product.
  - sku: Stock Keeping Unit, a unique identifier for each product variant.
  - name_title: The name or title of the product.
  - description: A textual description of the product.
  - list_price: The listed price of the product.
  - sale_price: The sale price of the product.
  - category: The category under which the product is listed.
  - category_tree: The hierarchical category path the product belongs to.
  - average_product_rating: The average rating of the product.
  - product_url: The URL of the product on the website.
  - product_image_urls: URLs of images of the product.
  - brand: The brand of the product.
  - total_number_reviews: The total number of reviews for the product.
  - Reviews: A collection of reviews associated with the product.
  - Bought With: Other products often bought with this product.
  
  ## json_review_files (User Information)
 This DataFrame seems to focus on user-related information. The key columns include:
  - Username: A unique identifier or name for the user.
  - DOB: Date of birth of the user.
  - State: The state where the user resides.
  - Reviewed: A list of product IDs that the user has reviewed.

## Insights
- Json_product_files: Contains comprehensive information about the products, including pricing, categorization, and customer reviews which are vital ingredients to conduct product analysis, market trends, and customer sentiment analysis.
- Json_review_files: Provides basic demographic information about the users, including their state of residence and their engagement in terms of product reviews. This data can be instrumental in understanding user demographics and their reviewing habits.

The combination of these DataFrames would allow for a rich analysis of customer behavior, product popularity, and potential market strategies.

# Exploring the structure of the product data
print("Product Data Overview:")
print(json_product_files.info())
print(json_product_files.describe())

# Exploring the structure of the user data
print("\nUser Data Overview:")
print(json_review_files.info())
print(json_review_files.describe())


## Insights
This exploration is an essential first step in this data analysis process as it help assess the quality of the data, understand what kind of cleaning and preprocessing will be required, and gauge what kind of analyses is possible in the given data. This will ensure an understanding of the structure and key statistics of your datasets, you can better plan further analyses, such as identifying trends, performing segmentations, or building predictive models.

## Data Validation
To accomplish this, I will need to manipulate the data in a manner that facilitates value management, data types correction and the merging of data to discover their links. Therefore, the following outline the steps that is taken to validate the data to include:
- Data checking to identify if there is any one with missing values
- Merging the different data sources to have an understanding of the data we have. For instance, linking user data with their reviews and the products they have reviewed.
- Transform DOB in order to get the year for age calculation

# Checking for missing values in product data
print("\nMissing Values in json_product_files:")
print(json_product_files.isnull().sum())

# Checking for missing values in user data
print("\nMissing Values in json_reviews_file:")
print(json_review_files.isnull().sum())

Three important tasks were also carried out in order to construct the type of analysis envisage with the files and they are listed as follows:
- Fill missing values if they exist or drop them in light of the analysis envisage
- Convert DOB to datetime and extract year for age calculation
- Calculate User's Age for Age-related analysis

## Data Processing
This typically consists of several steps, each of which aims to transform raw data into a more useful format, making it suitable for analysis, visualisation, or further processing.

# Fill missing values or drop them based on your analysis
json_product_files = json_product_files.fillna(method='ffill')  # Forward fill as an example
json_review_files = json_review_files.dropna()  # Dropping missing values as an example

# Convert DOB to datetime
json_review_files['DOB'] = pd.to_datetime(json_review_files['DOB'], errors='coerce', format='%d.%m.%Y')

# Calculate Age of Users
current_year = pd.Timestamp.now().year
json_review_files['Age'] = current_year - json_review_files['DOB'].dt.year

## Data analysis and visualisation
In relation to the aforementioned insights, I will analyse the new dataset derived based on the proposed insights. This may involve examining product popularity, review trends, user behaviour and demographics among other factors. And to fully comprehend this, I will employ visual representations to effectively demonstrate these discernments.
The analysis and visualisation is classified in three (3) to posit a meaningful insights:

- User Demographics: Analyze the demographics of users who provided reviews, like age distribution and state-wise distribution.
- Product Analysis: Analyses how products are rated on average, indicating overall customer satisfaction or product quality.
 - Review Analysis: Analyze and visualize the frequency of the words in the reviews submitted by users to see if there is any pattern to help improve customer's satisfaction.
 

import matplotlib.pyplot as plt

# User Age Distribution
plt.figure(figsize=(8, 4))
json_review_files['Age'].hist(bins=range(0, 100, 10))
plt.title('User Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Users')
plt.show()

top_reviewed_products = json_product_files.groupby('name_title')['total_number_reviews'].sum().nlargest(10)
print("\nTop 10 Most Reviewed Products:")
print(top_reviewed_products)

# Average Product Rating by Brand
avg_rating_by_brand = json_product_files.groupby('brand')['average_product_rating'].mean()
print("\nAverage Product Rating by Brand:")
print(avg_rating_by_brand)

## Insights
- User Age Distribution

The histogram displays how many users fall into each age range (0-10, 10-20, ..., 90-100). This visualization helps in understanding the age demographics of the users who are providing reviews. In this gragh, a significant number of users fall into the 30-70 age range, it suggests that this age group is particularly engaged with the products or more inclined to leave reviews.

- Top 10 Most Reviewed Products

By identifying the products with the most reviews, it provides an understanding of which products are receiving the most attention from users. Hence, the high number of reviews indicate popular products that evoke strong opinions (positive or negative) from customers.

- Average Product Rating by Brand

This analysis gives an idea of how different brands are perceived in terms of quality or satisfaction, as reflected by their average product ratings. Higher average ratings for a brand indicate higher customer satisfaction or perceived quality, while lower average ratings pinpoint areas for improvement.

## User Segmentation
Segmenting users by age and visualizing the distribution gives a clear picture of the demographic makeup of the customer base.

# Defines the boundaries of the age
age_bins = [0, 18, 30, 45, 60, 75, 100]

# Defines the labels for each age
labels = ['<18', '18-30', '30-45', '45-60', '60-75', '>75']

# Uses the pandas cut function to categorize the values in the 'Age' column of json_review_files into the defined bins.
json_review_files['Age_Group'] = pd.cut(json_review_files['Age'], bins=age_bins, labels=labels, right=False)

# Plotting user segments
user_segments.plot(kind='bar', figsize=(8,4))
plt.title('User Segmentation by Age')
plt.xlabel('Age Group')
plt.ylabel('Number of Users')
plt.show()

# Count users in each segment and display the output
user_segments = json_review_files['Age_Group'].value_counts()
print("User Segmentation by Age:\n", user_segments)

## Insights
The graph the shows that there is a higher concentration of users in the  '40-60' age groups which indicates that the products or marketing strategies are more appealing to the older folks that the younger ones in the demographic.

This insight can guide targeted marketing and product development strategies. If a significant portion of the customer base falls into a specific age bracket, products and marketing campaigns can be tailored to suit their preferences and needs. Additionally, if certain age segments are underrepresented, it might reveal untapped market potential or the need to adjust the product range or marketing approach to attract these segments.

## Age Distribution of Users

# Count the number of users in each state
state_demographics = json_review_files['State'].value_counts()

# Visualize the state demographics
plt.figure(figsize=(10, 4))
state_demographics.plot(kind='bar')
plt.title('User Distribution Across States')
plt.xlabel('State')
plt.ylabel('Number of Users')
plt.show()

# Display the state demographics
print("Number of Users in Each State:")
print(state_demographics.head(10))

## Insights
The bar chart visually represents the user distribution among various jurisdictions. The user population is dispersed among several states, although certain states are significantly more represented than others.
The widespread distribution of JC Penney's patronage in specific states indicates the presence of regional preferences or market dominance. To this end, regional marketing strategies, inventory distribution, and store selections may find this information to be of great value.

In conclusion,the state-wise distributions offer a more comprehensive insight into JC Penney's client demographic just as the csv file. These insights can be utilised to develop targeted marketing campaigns, enhance customer service, and customise product offers to cater to the requirements of specific demographic segments.

## Product Analysis
In this context, the product analysis of the DataFrames involve examining the various aspects of the product's performance, customer feedback, market trends, and competitive landscape.

import matplotlib.pyplot as plt

# Visualise the product ratings using matplot library
plt.figure(figsize=(8, 4))
json_product_files['average_product_rating'].hist(bins=20)
plt.title('Distribution of Product Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Products')
plt.show()

## Insight 
This provide an overview of how products are rated on average, indicating overall customer satisfaction or product quality.

## Sentiment Analysis
By conducting sentiment analysis on user reviews, it makes it possible to gauge the overall customer satisfaction and identify areas where JCPenny can improve its products. This is usually attainable by tracking changes in sentiment over time to evaluate the effectiveness of any changes made to any given product.

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Concatenate all review texts into a single string
all_reviews = ' '.join(json_product_files['Reviews'].astype(str))

# Define custom stopwords
custom_stopwords = set(STOPWORDS)
custom_words_to_remove = ["Score'", "User'", "JCP", "didn't", "especially", "expected", "child", "son", "Score", "recieved", "run", "daughter", "say"]
custom_stopwords.update(custom_words_to_remove)

# Generate a word cloud image
wordcloud = WordCloud(width = 800, height = 800, 
background_color ='white', stopwords=custom_stopwords, min_font_size = 10).generate(all_reviews)

# Display the generated image
plt.figure(figsize=(6, 6), facecolor=None) 
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# Insights
As it is shown in the graphics, customer's satisfaction seemed to be the obvious in review analysis demonstrating positive inclination towards words like "great", "love", "good", "comfortable" and "fittings". This suggests that contented customers tend to prioritise the product's quality, comfort, and overall size attributes.

However, the review also possess negative tone towards some products which indicate that customers often express unhappiness with issues pertaining designs, product availability and delivery.

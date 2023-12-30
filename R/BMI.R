# 1. Exploratory Data Analysis

# Load necessary libraries
library(tidyverse)
library(readxl)
library(ggplot2)
library(dplyr) 

# Read the data
data <- read_excel("C:/Users/Hanna/Downloads/3301407SportsPeople Data.xlsx")

# Histogram for LBM (Lean Body Mass)
ggplot(data, aes(x = LBM)) +
  geom_histogram(binwidth = 1, fill = "blue", color = "black") +
  theme_minimal() +
  ggtitle("Histogram of LBM (Lean Body Mass)") +
  xlab("LBM") +
  ylab("Frequency")

# Histogram for BMI (Body Mass Index)
ggplot(data, aes(x = BMI)) +
  geom_histogram(binwidth = 0.5, fill = "green", color = "black") +
  theme_minimal() +
  ggtitle("Histogram of BMI (Body Mass Index)") +
  xlab("BMI") +
  ylab("Frequency")

# View the first few rows of the data
head(data)

# Summary of the data
summary(data)

# Structure of the data
str(data)

# The dataset consists of three columns: 'Sex', 'Lean Body Mass (LBM)', and 'Body Mass Index (BMI)'.
# Statistical Summary:
#LBM: Ranges from 41.67 to 94.42, with an average of 61.34 and Median of 60.19.
#BMI: Ranges from 16.78 to 26.19, with an average of 21.75 and Median of 21.33.
# Variable Types:
# Sex  - This is a character variable (male/female).
# LBM & BMI - These are numerical variables.
# Histograms: 
# LBM and BMI suggest the following distributions:
# The LBM distribution is somewhat symmetric, with a slight right-skew.
# The BMI distribution appears relatively symmetric and normal.

# 2. Investigate Difference in Mean LBM between Males and Females
# Solution: 
# The approach to this investigation is to use a t-test to assess whether there's a significant difference in mean LBM between males and females. 

# Performing a t-test to compare mean LBM between males and females
t_test_result <- t.test(LBM ~ Sex, data = data)

# Displaying the result 
print(t_test_result) 

# 3. Correlation Coefficient for LBM and BMI
# Solution:
# The steps taken to address this problem is to calculate the correlation coefficient for LBM and BMI separately for male and female in the dataset.

# Calculating correlation for males 
cor_male <- cor(data %>% filter(Sex == "male") %>% select(LBM, BMI)) 

# Calculating correlation for females 
cor_female <- cor(data %>% filter(Sex == "female") %>% select(LBM, BMI)) 

# Display results 
print(cor_male) 
print(cor_female) 


# 4. Model to Test Relationship between LBM and BMI for Male Sportspeople

# Filter male in the sex class and perform Linear model  and assign it to a new variable
model_male <- lm(LBM ~ BMI, data = data %>% filter(Sex == "male"))


# # Displaying the summary of the model 
summary(model_male)


# Check for model assumptions (e.g., normality, homoscedasticity)
plot(model_male)


# Formal test for linear relationship
anova(model_male)

# 5. Predict LBM for a Male with BMI of 25

# Prediction
predict(model_male, newdata = data.frame(BMI = 25))

# 6. Assess Predictive Performance of the Model

# Assess model performance

# Calculating residuals
residuals <- resid(model_male)

# Calculating Mean Squared Error (MSE)
mse <- mean(residuals^2)

# Display MSE
print(mse)

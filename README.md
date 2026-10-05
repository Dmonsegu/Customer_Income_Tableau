# Loan Risk & Borrower Profile Analysis

## Overview

This project analyzes 252,000 loan applicant records to explore patterns in observed loan risk across borrower demographics, income, employment characteristics, ownership indicators, professions, and geography.

The analysis combines exploratory data analysis with an interactive Tableau dashboard to communicate patterns and support data-driven interpretation.

## Business Question

What borrower characteristics and geographic patterns are associated with observed loan risk, and how can those patterns be communicated through an interactive dashboard?

## Dataset

The dataset contains 252,000 loan applicant records and includes variables such as:

- Income
- Age
- Experience
- Marital status
- House ownership
- Car ownership
- Profession
- City
- State
- Current job years
- Current house years
- Risk Flag

The dataset was sourced from Kaggle.

## Tools

- Tableau
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- GitHub

## Analysis

The project explores:

1. Overall distribution of the observed risk indicator
2. Observed risk across income ranges
3. Geographic differences in observed risk
4. Observed risk across professions
5. Age and income relationships
6. Observed risk across current job tenure

## Tableau Dashboard

The interactive dashboard allows users to explore borrower risk patterns across multiple dimensions.

### Dashboard Components

- Risk Distribution
- Risk by Income
- Risk by State
- Risk by Profession
- Age vs. Income
- Risk by Employment Tenure

## Key Analytical Approach

Because Risk_Flag is a binary variable, its average can be interpreted as the proportion of records belonging to the observed risk category.

For example:

Average Risk_Flag = 0.10

can be interpreted as an observed risk rate of approximately 10% within that group.

## Important Limitation

This project is exploratory and descriptive. The analysis does not establish causal relationships or represent a production credit-risk model.

The Risk_Flag variable is treated as the dataset's provided risk indicator.

## Skills Demonstrated

- Data cleaning and preparation
- Exploratory data analysis
- Data visualization
- Tableau dashboard development
- Aggregation and segmentation
- Business question development
- Geographic analysis
- Interactive dashboard design
- Analytical communication

## Outcome

The final dashboard transforms a large tabular dataset into an interactive visual analysis that allows users to identify differences in observed risk across borrower characteristics and geographic segments.

# Football Performance Analysis Project

## Project Overview

#### This project explores the relationship between my physical activity, measured by steps tracked through a step counter app (Padometer), and my performance in football matches. I track my football performance weekly and combine this data with my daily step count data imported from Google Fit.

### Data Sources

#### Step Counter Data:

#### I use a step counter app called Padometer on my phone, which syncs data to Google Fit. From Google Fit, I export my daily step counts in JSON format.

### Football Performance Data:

#### I maintain a CSV file that tracks my weekly football performance. This file includes metrics such as goals scored, assists, team wins, and whether it was a football day.

## Questions Explored

### Correlation Analysis:

- Is there a relationship between the weekly steps total and the week's football performance? If so, how strong is it?

#### I found a strong positive correlation between weekly steps and metrics like goals scored and team wins.

- Is there a relationship between the total steps on the football day and the football performance? If so, how strong is it?

#### There is a moderate to strong positive correlation between steps on football days and metrics like goals scored, assists, and team wins.

- Which has a stronger correlation to my football performance: total steps on football days or total steps per week?

#### Total steps per week generally showed stronger correlations with metrics like goals scored and team wins. However, for assists, total steps on football days exhibited a stronger correlation.

## Methodology

### Data Import and Preprocessing:

- Imported daily step count data from JSON files downloaded from Google Fit.
- Merged this data with my weekly football performance CSV file using Python and pandas.

## Exploratory Data Analysis:

- Conducted correlation analyses to understand relationships between step counts and football performance metrics.
- Visualized these relationships using scatter plots to identify trends and correlations.

## Conclusion

### This project highlights the impact of physical activity, measured through daily steps, on my football performance. By analyzing correlations between steps and performance metrics, I gain insights into how my physical activity levels influence my gameplay.

# Race Pulse: Predicting Marathon Times with Data Power

## Project Overview

Welcome to Race Pulse, where we combine the power of data and machine learning to predict marathon race times. Our goal is to explore how factors like weather, runner demographics, and pacing strategies impact marathon performance. Along the way, we uncovered good insights and built a model that predicts marathon times with impressive accuracy.

____

### What We Did

1.	Gathering the Data:

    We collected marathon data from 2015 to 2018, including runners’ ages, genders, race splits (like 5k, 10k times), and their final finishing times. We paired this with detailed weather information, such as temperatures, wind speed, and precipitation, for race days.
2.	Cleaning and Organizing

    •	Removed unnecessary columns (like runner IDs and redundant details).

	•	Filled in or dropped missing data where needed.

	•	Converted race times into seconds so we could analyze them consistently.

	•	Merged the marathon data with weather stats, creating one complete dataset for our analysis.

3.	Exploring the Data

	•	Looked at how most runners finished within a certain time range, with a few outliers being super fast or super slow.

	•	Compared male and female runners and saw slight differences in their performance trends.

	•	Studied how weather conditions (e.g., temperature and wind) affected race outcomes.

	•	Discovered that early pacing (like the 5k split) had a strong influence on the final race time.

4.	Building a Predictive Model

	•	Used Random forest and XgBoost, machine learning models, to predict marathon times.

	•	Chose key features like age, gender, early split times, and weather conditions to train the model.

	•	Scaled the data to make everything uniform for the model.

5.	Evaluating the Model

	•	Both the models performed well

	•	R² (R-squared): 0.995 (almost perfect predictions!)

	•	Mean Absolute Error (MAE): About 43.24 vs. 53.86 seconds seconds (on average, the models are only off by less than a minute).

	•	We also used cross-validation to confirm that the model is consistent across different data splits.

6.	Visualizing the Results

    We created easy-to-understand visuals to explain our findings:

    •	Histograms showing the distribution of marathon times.

    •	Comparisons of predicted vs. actual times, which showed how accurate the model is.

    •	Graphs showing how weather and pacing influence performance.

    •	A side-by-side look at top performers’ pacing vs. slower runners.

### Key Takeaways

•	Pacing is Key: Runners who start strong (e.g., fast 5k splits) tend to finish faster overall.

•	Weather Matters: Cooler temperatures and moderate wind conditions lead to better performance.

•	Men vs. Women: Male runners finish slightly faster on average, but the gap narrows among top performers.

•	Accurate Predictions: Our Ridge Regression model can predict marathon times with incredible precision.

### How This Analysis Helps Sponsors

By leveraging our insights, sponsors can better evaluate and prioritize athletes based on their likelihood of strong marathon performances. The ability to predict finishing times with precision allows sponsors to:

• Identify athletes with promising pacing strategies.

• Focus on runners who excel under favorable weather conditions.

• Tailor their sponsorship strategies to specific events or conditions where their sponsored athletes are likely to succeed.

• Evaluate the impact of their support over time by tracking predictions vs actual results.

### Challenges We Faced

•	Missing Data: Some weather variables were incomplete, and certain temperature ranges had no data.

•	Choosing Features: It was tricky deciding which variables to include without overcomplicating the model.

•	Generalizing Results: We need to ensure the model works well on marathons other than the Boston Marathon.


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eG6ocWkI)

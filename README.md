# The Company Cardio Catch Diseases ( CCD )

![alt text](https://github.com/willianmenegatt/Projeto_Cardio_Disease/blob/main/cardio.jpg?raw=true)

Cadio Catch Diseases is a company that specializes in detecting heart disease in the early stages. Its business model is of the Service type, that is, the company offers the early diagnosis of a cardiovascular disease for a certain price.

Currently, the diagnosis of a cardiovascular disease is done manually by a team of specialists. The current accuracy of the diagnosis varies between 55% and 65%, due to the complexity of the diagnosis and also the fatigue of the team that takes turns to minimize the risks. The cost of each diagnosis, including the equipment and the analysts payroll, is around 1,000.00.

The price of the diagnosis, paid by the client, varies according to the precision achieved by the team of specialists. The client pays 500.00. for every 5% of accuracy above 50%. For example, for an accuracy of 55%, the diagnosis costs 500.00 for the customer, for an accuracy of 60%, the value is 1000.00. If the diagnostic accuracy is 50%, the customer does not pay for it.

Note that the variation in the precision given by the team of specialists causes the company to have either an operation with profit, revenue greater than cost, or an operation with a loss, revenue less than cost. This diagnostic instability causes the company to have an unpredictable Cashflow.

The goal as a Data Scientist employed by Cardio Catch Diseases is to create a tool that increases diagnostic accuracy and that accuracy is stable for all diagnoses. Therefore, the job is to create a patient classification tool with stable accuracy. Along with the tool, you need to send a report to the CEO of Cardio Catch Diseases, reporting the results and answering the following questions: ( He will likely ask these questions on the day of your presentation. )

- What is the Accuracy and Precision of the tool?
- How much profit will Cardio Catch Diseases make with the new tool?
- What is the reliability of the result given by the new tool?

**Information about the dataset**

The dataset that will be used to create the solution for Cardio Catch Diseases is available on the Kaggle platform.
This dataset contains 70,000 patient diagnoses.

The link: https://www.kaggle.com/sulianova/cardiovascular-disease-dataset

# Business Problem

The challenge is to help the company in detecting heart diseases in the early stages. The business model is 'sevice', it means that the company offers an early heart disease diagnostic for a price.
Important details:<br>
- Actually, the precision of the diagnostic is between 55% and 65%.
- For each 5% of increasement in accuracy above 50%, the price receives an increase of R$ 500,00.

## Main goal:

Create a tool tha increases diagnostic accuracy, that this accuracy is stable for all diagnostics.

## Secondary goals:

Answer the CEO questions:
1. What is the accuracy and precision of the tool?
2. How much profit the company will have with the new tool?
3. How reliable is the result given by the new tool?

## Strategy guide:
**1.** Collect and load the data;

**2.** Data preparation;
- Check for missing values
- Check the relevance of each feature
- See the statistical metrics of each feature

**3.** Exploratory Data Analysis
- Check the distribution of the attributes
- Treat Outliers
- Filter relevant rows to the case
- Univariate and bivariate analysis

**4.** Hypotheses (Verify with T Test of Student)
- 4.1 Does the 'age' feature affect the number of cases of cardiovascular disease? **Answer: Yes**
- 4.2 Does the 'weight' feature affect the number of cases of cardiovascular disease? **Answer: Yes**
- 4.3 Does the 'ap_hi' feature affect the number of cases of cardiovascular disease? **Answer: Yes**
- 4.4 Does the 'height' feature affect the number of cases of cardiovascular disease? **Answer: Yes**

**5.** Feature Engineering

**6.** Encoding of categorical variables (One-hot-enconding)

**7.** Machine Learning Prediction Model
- Choose the best model between: LogisticRegression, RandomForests and Light-GBM
- Use the cross-validation: n = 5 models
- Translate of the models performance to the business performance

**8.** Deploy via API (Flask)

### Reduce Marketing Spend
The hackathon is hosted by [HackerEarth](https://www.hackerearth.com/).

### Contents

* [Problem Statement](#problem-statement)
  * [Task](#task)
  * [Evaluation Metric](#evaluation-metric)


* [Dataset Description](#dataset-description)
  * [Data Source](#data-source)
  * [Data Dictionary](#data-dictionary)


* [Notebooks](#Notebooks)
  * [Data Cleaning](#data-cleaning)


### Problem Statement
Reduce the spend on marketing campaigns and aim only the customers who will benefit from the product.

This will result in the following:

* Increased business
* New customers who are compatible with your organization
* Seamless transactions with a higher success rate
* More profit with fewer obstacles

#### Task
Predicting the probability percentage that the client will purchase a product based on the available set of features.

#### Evaluation Metric

```python
score = max(0 , 100-np.sqrt(mean_squared_error(actual, predicted)))
```

### Dataset Description

#### Data Source
The dataset is downloaded from [here](https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-reduce-marketing-spend/).


#### Data Dictionary

| Feature               | Description                                                                                                            |
|:----------------------|:-----------------------------------------------------------------------------------------------------------------------|
| Deal_title            | Represents a unique title for each deal                                                                                |
| Lead_name             | Represents the name of a lead                                                                                          |
| Industry              | Represents the Industry that a lead belongs to                                                                         |
| Deal_value            | Represents the value of a deal between a lead and your company (in Dollars)                                            |
| Weighted_amount       | Represents a value that is estimated revenue times a probability                                                       |
| Date_of creation      | Represents the date when a deal's pipeline was created                                                                 |
| Pitch                 | Represents the different types of products that your company offers to a lead                                          |
| Contact_no            | Represents the contact details of a lead (masked)                                                                      |
| Lead_revenue          | Represents the lead company’s revenue (in Dollars)                                                                     |
| Fund_category         | Represents the type of funding that a lead possesses                                                                   |
| Geography             | Represents the geographical location of a lead (country)                                                               |
| Location              | Represents the geographical location of a lead (state or city)                                                         |
| POC_name              | Represents the lead’s point of contact's name                                                                          |
| Designation           | Represents the lead POC’s designation                                                                                  |
| Lead_POC_email        | Represents the lead POC’s email address                                                                                |
| Hiring_candidate_role | Represents the Job role that a lead wants to hire                                                                      |
| Lead_source           | Represents the source from which the lead is generated                                                                 |
| Level_of_meeting      | Represents the level of a meeting with the lead. Level 1: Introductory call Level 2: Demo call Level 3: Pre-sales call |
| Last_lead_update      | Represents the communication update between a lead and your company                                                    |
| Internal_POC          | Represents the name of the employee who has generated the lead                                                         |
| Resource              | Represents whether your company has enough resources to satisfy a lead's requirements                                  |
| Internal_rating       | Represents a rating (1-5) given to a lead                                                                              |
| Success_probability   | Represents the probability that a lead will buy a product or onboard                                                   |

### Notebooks

* [Data Cleaning](https://nbviewer.jupyter.org/github/sank3t/Reduce-Marketing-Spend/blob/main/Data%20Cleaning.ipynb)

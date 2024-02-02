# Clustering-Analysis

## Overview
This repository explores customer segmentation using the Wholesale customers dataset. The goal is to employ clustering techniques to segment clients based on their purchase habits, providing insightful understanding of consumer behavior. 

## Dataset Description

**Dataset:** Wholesale customers dataset - https://archive.ics.uci.edu/dataset/292/wholesale+customers

**Size:** 440 samples, 8 columns

**Features:**

(i) **Continuous features:** Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen

(ii) **Categorical features:** Channel, Region

## Objectives

1. **Segmentation:** Utilize clustering techniques to segment customers based on purchase habits.

2. **Insights:** Gain understanding of consumer behavior, preferences, and traits.

3. **Applications:** Develop specialized marketing plans for targeted customer groups.

## Exploratory Data Analysis (EDA)

**1. Spending by Region, Channel, and Category:**

![image](https://github.com/sunitiarora45/Clustering-Analysis/assets/131208092/208ebfcf-1128-49ed-adf4-61042176cb77)

**2. Spending by Region and Channel:**

![image](https://github.com/sunitiarora45/Clustering-Analysis/assets/131208092/44b4ad10-4d95-42ec-b319-0f36a98222a8)

## Correlation Analysis

![image](https://github.com/sunitiarora45/Clustering-Analysis/assets/131208092/42c92ce5-3ffc-43bb-ac32-632838d25a02)

## Clustering Algorithms:

**1. K-means Clustering:**

![image](https://github.com/sunitiarora45/Clustering-Analysis/assets/131208092/921c78ae-72c0-40b0-a2c6-9003435c6971)

![image](https://github.com/sunitiarora45/Clustering-Analysis/assets/131208092/14a76ac7-b5df-4670-afe8-814539fe2164)

**2. Hierarchical Clustering:**

![image](https://github.com/sunitiarora45/Clustering-Analysis/assets/131208092/fbec2b26-1d48-4563-8823-2d5410d80dc0)

**3. DBSCAN Clustering:**

![image](https://github.com/sunitiarora45/Clustering-Analysis/assets/131208092/267fae01-077d-441f-b621-44c0da97c540)

## Results and Observations

(i)   **Cluster 0:** Customers spend more money on “Fresh” and “Frozen” goods, indicating a preference for perishable goods.

(ii)  **Cluster 1:** This cluster shows consumers who spend a lot of money in all categories, demonstrating that they have a wide range of product needs.

(iii) **Cluster 2:** Customers exhibit modest spending across all categories, indicating fewer needs for purchases.

(iv)  **Cluster 3:** Customers in this cluster place a higher priority on groceries, detergents, and paper goods, showing an emphasis on necessities for the home.

## Performance Comparison

1. **K-means:** Highest Silhouette Coefficient (0.680), well-separated clusters.

2. **Hierarchical:** Silhouette Coefficient (0.678), capturing complex differences.

3. **DBSCAN:** Silhouette Coefficient (0.636), effective with noisy data.

**Overall Performance:** K-means outperforms with a Silhouette Coefficient of 0.680, creating more distinct and well-separated clusters.

**Observations:** K-means shows efficient cluster combination, while hierarchical captures complex differences. DBSCAN manages noise well but struggles with certain data patterns.

## Conclusion

(i)	Customers spending habits vary across various regions and distribution channels. While the Hotel channel exhibits higher overall spending, the Other region emerges as a promising market for wholesale goods.

(ii) “Fresh,” “Grocery,” and “Milk” product categories have a substantial impact on client purchasing decisions, highlighting their relevance in marketing and product offerings.

(iii)	Using clustering analysis, different consumer segments were found based on the preferences and spending habits of the customers.












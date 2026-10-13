# Factory Reallocation & Shipping Optimization Recommendation System

## Project Overview

This project develops a data-driven Factory Reallocation and Shipping Optimization Recommendation System for Nassau Candy Distributor.

The system analyzes product, factory, destination, shipping mode, distance, lead-time scenarios, and profitability indicators to identify potential factory reallocation opportunities.

The project combines data analysis, machine learning, route clustering, scenario simulation, and recommendation scoring to support logistics and operational decision-making.

## Objectives

- Analyze product and shipping data
- Identify current factory-to-destination distances
- Calculate potential distance savings
- Simulate alternative factory assignments
- Estimate scenario-based shipping lead time
- Evaluate potential lead-time reduction
- Identify slow or high-distance route groups
- Generate factory reallocation recommendations
- Build an interactive Streamlit dashboard

## Dataset

The dataset contains order-level information including:

- Order ID
- Order Date
- Ship Date
- Ship Mode
- Customer ID
- Country/Region
- City
- State/Province
- Product Name
- Sales
- Units
- Gross Profit
- Cost

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- OpenPyXL
- Streamlit
- Jupyter Notebook

## Methodology

### 1. Data Preparation

The dataset was cleaned, validated, and transformed for analysis.

### 2. Factory Mapping

Products were mapped to their respective origin factories.

### 3. Distance Analysis

Factory and destination coordinates were used to calculate geographical distance using the Haversine formula.

### 4. Factory Reallocation Analysis

Alternative factories were evaluated to identify scenarios with potential distance savings.

### 5. Lead-Time Scenario Modeling

Scenario-based lead time was estimated using distance and shipping mode assumptions.

### 6. Machine Learning

The following regression models were evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Evaluation metrics:

- RMSE
- MAE
- R²

### 7. Route Clustering

K-Means clustering was used to identify groups of routes based on distance, lead time, lead-time savings, distance reduction, and profit margin.

### 8. Recommendation Engine

A recommendation score was calculated using:

- Lead-Time Reduction
- Distance Reduction
- Profit Margin
- Scenario Confidence

The resulting scenarios were classified into recommendation levels.

## Dashboard

The Streamlit dashboard contains four main sections:

1. Factory Optimization
2. What-If Analysis
3. Recommendations
4. Risk & Impact

Users can filter scenarios by:

- Product
- Region
- Ship Mode
- Current Factory
- Alternative Factory
- Speed Priority

## Project Outputs

The project generates:

- Factory reallocation recommendations
- Route cluster analysis
- KPI summary
- Scenario analysis
- Interactive Streamlit dashboard

## How to Run

Install the required Python libraries:

```bash
```bash
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

## Live Dashboard

Explore the deployed Streamlit application:

**[Open Nassau Candy Factory Optimization Dashboard](https://o569m9ssgtuafuvaxnxyep.streamlit.app/)**

## Machine Learning Model Comparison

Three regression models were evaluated using RMSE, MAE, and R².

| Model | RMSE | MAE | R² |
|---|---:|---:|---:|
| Linear Regression | 1.8041 | 1.5402 | 0.6068 |
| Random Forest Regressor | 0.6685 | 0.4899 | 0.9460 |
| Gradient Boosting Regressor | 0.8682 | 0.6853 | 0.9089 |

Random Forest achieved the lowest RMSE and MAE and the highest R² among the evaluated models.

**Important:** The lead-time target is scenario-generated using distance and shipping-mode assumptions. These metrics measure performance against that generated target, not verified real-world shipping times.

## Repository Files

| File | Description |
|---|---|
| `app.py` | Streamlit dashboard application |
| `requirements.txt` | Python dependencies |
| `ml_model_comparison.csv` | Model evaluation results |
| `final_factory_recommendations.csv` | Factory recommendation output |
| `dashboard_recommendations.csv` | Dashboard recommendation data |
| `product_recommendations.csv` | Product-level recommendation output |
| `project_kpi_summary.csv` | Summary KPIs |
| `route_cluster_analysis.csv` | Route clustering output |
| `Nassau Candy Distributor.xlsx` | Source dataset, subject to sharing permissions |

## Limitations

- Lead-time estimates are scenario-based and depend on the assumptions used.
- Recommendations represent potential opportunities, not confirmed operational savings.
- Actual shipping performance and factory capacity should be validated before implementing a recommendation.
- Recommendation scores use selected policy weights and should not be interpreted as machine-learning feature importance.

## Future Improvements

- Validate lead-time predictions against reliable historical transit-time data.
- Incorporate actual factory capacity, production cost, and shipping rates.
- Add automated scenario comparisons and downloadable reports.
- Evaluate recommendations using real operational outcomes.

## Author

**Shaikh Saniya Afsar**

Project: Factory Reallocation & Shipping Optimization Recommendation System  
Organization: Unified Mentor  
Project Type: Internship Project Report

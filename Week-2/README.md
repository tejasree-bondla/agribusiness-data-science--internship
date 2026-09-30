# Week 2 – Data Acquisition, Cleaning and Preprocessing in Agribusiness

## Objective

The objective of Week 2 is to develop a systematic workflow for acquiring, validating, cleaning, transforming, and standardizing public agribusiness data.

The work focuses on crop production data containing agricultural variables such as district, crop, season, year, cultivated area, production, and yield.

## Data Source

The primary public source selected for this task is the Government of India's Open Government Data (OGD) Platform.

**Dataset:** Area, Production and Yield of Major Crops of Gujarat State

**Publisher:** Directorate of Economics & Statistics, Government of Gujarat

**Source:** https://www.data.gov.in/catalog/area-production-and-yield-major-crops-gujarat-state

A national crop-production dataset from the Ministry of Agriculture and Farmers Welfare was also considered as a complementary source.

## Data Acquisition

The proposed acquisition workflow is:

1. Identify a relevant public government agriculture dataset.
2. Record the dataset title, publisher, source URL, and update information.
3. Download or access the available resource/API.
4. Preserve the raw data without modification.
5. Create a working copy for preprocessing.
6. Inspect the structure, data types, missing values, duplicates, and numerical ranges.

## Data Cleaning

The preprocessing workflow includes:

* Removing unnecessary whitespace
* Standardizing text capitalization
* Converting numerical fields to numeric data types
* Detecting missing values
* Detecting duplicate records
* Detecting negative or invalid agricultural measurements
* Checking inconsistent categories
* Verifying units
* Validating derived yield values

## Missing Values

Missing agricultural measurements are not automatically replaced with zero because a missing value does not necessarily mean that the measured quantity was zero.

The appropriate treatment depends on the reason for missingness and the source documentation.

## Outlier Detection

Potential outliers are identified using:

* Domain validation
* Minimum and maximum range checks
* IQR-based statistical checks where appropriate

Unusual observations are investigated before being removed because an extreme agricultural value may represent a genuine observation.

## Transformation

The planned transformations include:

* Standardizing district, crop, and season names
* Converting year and numerical variables into consistent data types
* Standardizing measurement units
* Creating yield as:

`Yield = Production / Area`

The yield calculation is performed only when area is positive and production is valid.

## Validation

After preprocessing, the dataset should be checked again for:

* Remaining missing values
* Duplicate records
* Invalid numerical values
* Inconsistent categories
* Unit consistency
* Logical relationships between variables

## Important Note

The full government resource was not directly downloadable in the working environment. Therefore, the report does not claim that the complete official dataset was cleaned. A small simulated dirty dataset is used to demonstrate the preprocessing workflow honestly and reproducibly.

## Tools

* Python
* Pandas
* NumPy
* Jupyter Notebook / VS Code
* GitHub

## Week 2 Outcome

This work establishes a reproducible data-preprocessing workflow that can be used as the foundation for later agribusiness exploratory data analysis, visualization, forecasting, and machine-learning tasks.

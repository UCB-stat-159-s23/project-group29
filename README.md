[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s23/project-group29.git/HEAD?labpath=main.ipynb)
.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/UCB-stat-159-s23/project-group29.git/HEAD?labpath=main.ipynb
 
# NBA Dataset Analysis


## Overview

This project is analyzing NBA data that will then be used to build a regression model that will predict NBA Game winners using past performance. The scientific preface of this project is based on normal assumptions in sports, what factors like previous performance and home court advantage have an affect on winning and are we able to accurately predict NBA games won based on these dependencies? The analysis consists of data cleaning, exploratory data analysis, feature engineering and model building.

## Project Website

The website for this project can be found here [https://ucb-stat-159-s23.github.io/project-group29/main.html]

## Dataset

The data was collected using a known and popular API, NBA_API. The data is made available in the repository and all cleaned versions of the data set are available as well in the data folder.

## Repository Structure
This repository is structured this way:

- data/: This folder has the raw and processed datasets used in the analysis.
- tools/: This folder contains utils.py, which are useful functions used in this repository. Inside it is the folder tests/ that hosts test_utils.py, which tests the functions we created
- Data Collection.ipynb: Contains the code that we used to gather the data used in this project.
- Data Cleaning Feature Engineering.ipynb: Here is all the data engineering and cleaning we did in order to obtain a dataset that is usable to build a linear regression model.
- main.ipynb: Contains a summary of all the analysis we made in this project
- prediction model.ipynb: Here is all the code and steps we took to build our linear regression model.
- environment.yml: This file contains all the packages and dependencies used in this project
- Makefile: this file contains all the information needed to build a JupyterBook. 


## License

This project is licensed under the BSD 3-Clause License.







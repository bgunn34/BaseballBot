# Goal: create a macine learning model that provides predictions on the outcomes of baseball games. 
### We want to express the predictions as probabilities so that we can compare our model's predicition to betting lines published by Vegas, Fanduel, Draftkings et al.

## Machine Learning Checklist:
1. Frame the problem and look at the big picture.
	1. The goal is not to build an algorithm that can predict games perfectly. There is too much randomness in baseball for that. The goal is to make probabalistic statements (the Phillies will win this game 45% of the time) and compare those statements to those made by betting institutions. I will be happy if we even come close to their level of accuracy. 
	1. I should note that the only way to measure that accuracy will be against live data during the baseball season, so I am aiming to have this model in production by March 2021.
	1. There are thousands of baseball statistics that are collected every day of the season. Part of the challenge is going to be determining which are important and which are just noise. 
1. Get the data
	1. see data_gathering directory. 
	1. I used pybaseball to scrape 
		1. pitch information from statcast 
		1. team and player information from fangraphs 
		1. lineup, starting pitcher, and outcome information from Retrosheet
		1. **TODO** - for production I will need to get today's lineups and starting pitchers to make predictions against.
1. Explore the data
	1. see data_exploration folder.
	1. I made detailed notes on every feature of the fangraphs data, see fangraphs_variable_description.xlsx
	1. I analyzed win to stat correlations on the team level to glean some guidance on which stats to pay attention to in the massive fangraphs dataset. See Team_Stats_Analysis.ipynb
1. Prepare the data
1. Shortlist promising models
1. Fine-tune the system
1. Launch!

## Resources:
Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn
https://github.com/jldbc/pybaseball - python library to scrape baseball information from Fangraphs, Statcast, Retrosheet, etc. I am also a contributor to this project.

Hands-On Machine Learning with Scikit-Learn, Keras, and Tensorflow by Aurelien Geron

Retrosheet Data Notice

Recipients of Retrosheet data are free to make any desired use of the information, including (but not limited to) selling it, giving it away, or producing a commercial product based upon the data. Retrosheet has one requirement for any such transfer of data or product development, which is that the following statement must appear prominently:

 The information used here was obtained free of
 charge from and is copyrighted by Retrosheet.  Interested
 parties may contact Retrosheet at "www.retrosheet.org".

Retrosheet makes no guarantees of accuracy for the information that is supplied. Much effort is expended to make our website as correct as possible, but Retrosheet shall not be held responsible for any consequences arising from the use the material presented here. All information is subject to corrections as additional data are received. We are grateful to anyone who discovers discrepancies and we appreciate learning of the details.

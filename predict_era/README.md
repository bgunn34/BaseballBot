# Predicting ERA

### The purpose of this folder is to build a sub-algorithm to predict pitcher ERA using statcast data. Once I have that I will have a very good idea of what features to include in pitcher's features in the final dataframe.

This is a supervised learning problem. I am going to match up ERA labels to the input data.
This is a regression problem. We want to predict ERA, which is a continuous variable. 
Batch processing will be fine. While the final algorithm might want to retrain online, the goal of this one is to tell us what features we need. 

### To Do:
- [ ] Pivot the statcast data into pitcher/game tables, taking averages and sums of the data where appropriate. We'll probably lose some features in this step as well.
- [ ] get a game level dataframe of innings pitched and runs allowed. I can calculate ERA from there. 
- [ ] consider using a different rate metric than ERA. We know that if ERA is closely correlated to wins a less arbitrary rate stat (like runs per IP) should be as well. 
- [ ] split data into a train and test set. 
- [ ] do some exploration of the train set. 
- [ ] train some algorithms and look at the results. 
- [ ] tune some hyper parameters following guides in HOML
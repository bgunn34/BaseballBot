##It would be a cool thing to try to predict baseball game outcomes.##
1) scrape roster data, maybe from fangraphs or from statcast
2) get players wOBA for the last 3 years using a threshold to make sure that we don't try to incorporate parital or missing seasons.
3) weight the wOBA for recency against sample size. So last year's wOBA would be worth more than the year before's, etc. Will probably want to figure out how to play with those weights to see which one is best before selecting the one to put in the bot itself.
4) any other metrics for hitters? maybe RC+?
5) choose a metric for pitchers.
6) how do we handle bullpens
7) get a good data set of teams, lineups, pitchers, outcomes.
8) try out different ML algorithms and see what scores most highly.

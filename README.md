##It would be a cool thing to try to predict baseball game outcomes.##
1) scrape roster data, maybe from fangraphs or from statcast
    - pybaseball seems to be a great way to get historical player statisitcs, even up to that day.
    - I can get game outcomes fairly easily using the schedule_and_record function.
    - I still need some way to get a game's lineups and starter, both historically and in future retrosheet.org!
	- get current rosters for bullpen.
2) get players wOBA for the last 3 years using a threshold to make sure that we don't try to incorporate parital or missing seasons.
3) weight the wOBA for recency against sample size. So last year's wOBA would be worth more than the year before's, etc. Will probably want to figure out how to play with those weights to see which one is best before selecting the one to put in the bot itself.
4) any other metrics for hitters? maybe RC+?
5) choose a metric for pitchers.
6) how do we handle bullpens?
7) get a good data set of teams, lineups, pitchers, outcomes. DONE
8) try out different ML algorithms and see what scores most highly.



Retrosheet Data Notice

Recipients of Retrosheet data are free to make any desired use of the information, including (but not limited to) selling it, giving it away, or producing a commercial product based upon the data. Retrosheet has one requirement for any such transfer of data or product development, which is that the following statement must appear prominently:

 The information used here was obtained free of
 charge from and is copyrighted by Retrosheet.  Interested
 parties may contact Retrosheet at "www.retrosheet.org".

Retrosheet makes no guarantees of accuracy for the information that is supplied. Much effort is expended to make our website as correct as possible, but Retrosheet shall not be held responsible for any consequences arising from the use the material presented here. All information is subject to corrections as additional data are received. We are grateful to anyone who discovers discrepancies and we appreciate learning of the details.
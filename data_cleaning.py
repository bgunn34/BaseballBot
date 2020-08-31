import pandas as pd

pd.options.display.max_rows = 1000
pd.options.display.max_colwidth = 50


#### cleaning for retrosheet games, starters, linups, outcomes.
df = pd.read_csv('data\\retrosheet_data.csv')

keep_columns = ['date',
                'game_num',
                'visiting_team',
                'home_team',
                'visiting_score',
                'home_score',
                'visiting_starting_pitcher_id',
                'visiting_starting_pitcher_name',
                'home_starting_pitcher_id',
                'home_starting_pitcher_name',
                'visiting_1_id',
                'visiting_1_name',
                'visiting_1_pos',
                'visiting_2_id',
                'visiting_2_name',
                'visiting_2_pos',
                'visiting_2_id.1',
                'visiting_3_name',
                'visiting_3_pos',
                'visiting_4_id',
                'visiting_4_name',
                'visiting_4_pos',
                'visiting_5_id',
                'visiting_5_name',
                'visiting_5_pos',
                'visiting_6_id',
                'visiting_6_name',
                'visiting_6_pos',
                'visiting_7_id',
                'visiting_7_name',
                'visiting_7_pos',
                'visiting_8_id',
                'visiting_8_name',
                'visiting_8_pos',
                'visiting_9_id',
                'visiting_9_name',
                'visiting_9_pos',
                'home_1_id',
                'home_1_name',
                'home_1_pos',
                'home_2_id',
                'home_2_name',
                'home_2_pos',
                'home_3_id',
                'home_3_name',
                'home_3_pos',
                'home_4_id',
                'home_4_name',
                'home_4_pos',
                'home_5_id',
                'home_5_name',
                'home_5_pos',
                'home_6_id',
                'home_6_name',
                'home_6_pos',
                'home_7_id',
                'home_7_name',
                'home_7_pos',
                'home_8_id',
                'home_8_name',
                'home_8_pos',
                'home_9_id',
                'home_9_name',
                'home_9_pos']
df = df.loc[:,keep_columns]

columns =  ['date',
            'game_num',
            'visiting_team',
            'home_team',
            'visiting_score',
            'home_score',
            'visiting_starting_pitcher_id',
            'visiting_starting_pitcher_name',
            'home_starting_pitcher_id',
            'home_starting_pitcher_name',
            'visiting_1_id',
            'visiting_1_name',
            'visiting_1_pos',
            'visiting_2_id',
            'visiting_2_name',
            'visiting_2_pos',
            'visiting_2_id.1',
            'visiting_3_name',
            'visiting_3_pos',
            'visiting_4_id',
            'visiting_4_name',
            'visiting_4_pos',
            'visiting_5_id',
            'visiting_5_name',
            'visiting_5_pos',
            'visiting_6_id',
            'visiting_6_name',
            'visiting_6_pos',
            'visiting_7_id',
            'visiting_7_name',
            'visiting_7_pos',
            'visiting_8_id',
            'visiting_8_name',
            'visiting_8_pos',
            'visiting_9_id',
            'visiting_9_name',
            'visiting_9_pos',
            'home_1_id',
            'home_1_name',
            'home_1_pos',
            'home_2_id',
            'home_2_name',
            'home_2_pos',
            'home_3_id',
            'home_3_name',
            'home_3_pos',
            'home_4_id',
            'home_4_name',
            'home_4_pos',
            'home_5_id',
            'home_5_name',
            'home_5_pos',
            'home_6_id',
            'home_6_name',
            'home_6_pos',
            'home_7_id',
            'home_7_name',
            'home_7_pos',
            'home_8_id',
            'home_8_name',
            'home_8_pos',
            'home_9_id',
            'home_9_name',
            'home_9_pos']
df.columns = columns
df.to_csv('data\\retro_cleaned.csv')

####cleaning fangraphs data
df = pd.read_csv('data\\baseball_stats.csv')
keep_columns= ['Season',
               'Name',
               'G',
               'PA',
               'R',
               'SO',
               'SF',
               'GDP',
               'SB',
               'CS',
               'LD%',
               'GB%',
               'FB%',
               'wOBA']

df = df.loc[:,keep_columns]
df.to_csv('data\\fangraphs_cleaned.csv')

## I am a little unsure of which features to hang onto from the FG data.
## There are so many. Maybe I'll figure out how to do some kind of randomized 
## test.
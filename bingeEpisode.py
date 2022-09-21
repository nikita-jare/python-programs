import os
import random

show_dir = '/Users/nikitajare/Python-programs/dataset/randomEpisode' #dir in which episodes are stored
os.chdir(show_dir)

#randomly choose among the shows to watch
choose_show = random.choice(os.listdir(show_dir))
show_path = str(os.path.realpath(choose_show))
os.chdir(choose_show)

#randomly choose the season to watch
choose_season = random.choice(os.listdir(show_path))
season_path = str(os.path.realpath(choose_season))
os.chdir(season_path)

#randomly choose episode
choose_episode = random.choice(os.listdir(season_path))

print("Enjoy your Episode!")
print(f"Playing episode {choose_episode} from season {choose_season} of {choose_show}")

os.system("open '" + choose_episode +"'")
#windows user can use os.system("open " + choose_episode) 



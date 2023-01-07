# AutoRewarder

## What is This
Microsoft offer [rewards](https://rewards.bing.com) if you use Edge and Bing regularly. This is a script that 

* Opens Edge
* Performs 10 Bing searches
* Closes Edge

that can be run on a daily/nightly basis to automatically rack up points. It'll only accumulate 55 points per day and 6500 is the threshold for a gift card, so it's not a huge moneymaker! Roughly worth $10 / year :smile:

## How to Use This
1. Enroll in the Microsoft Rewards program [here](https://rewards.bing.com)
2. Download this repo
3. From a windows terminal, run "pip install keyboard" to install the Python keyboard package
4. Edit the RunAutoRewarder.bat script (right-click > edit ... don't double click) and update "C:\Users\maize\Desktop\Nerdy Gaming\GitHub\AutoRewarder\AutoRewarder.py" so that it matches wherever you downloaded the AutoRewarder.py file from this repo
5. Run the batch script manually (double click it from the explorer) to make sure it runs properly (should open Edge, do 10 searches, and close itself)
6. Open the Windows Task Scheduler (windows key > type "task scheduler") so that you can set this up to run daily
7. On the right side of the window, click "Create Basic Task"
    * Name it "Run Auto Rewarder" (or anything, doesn't matter) and type anything into the description
    * Trigger Daily
    * Pick the time of day you want it to run (midnight, 3pm, whatever)
    * Action = Start a Program
    * Click Browse and locate the "RunAutoRewarder.bat" script
    * Next > Finish > Finish
8. You're done! Watch your points trickle in!

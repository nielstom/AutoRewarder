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
3. Download Python (any somewhat modern version is fine. 3.X, not 2.X.)
4. From a windows terminal, run these command to install necessary Python packages: 
    * pip install keyboard   *// Installs the Python keyboard package (tools to emulate clicking keyboard keys)*
    * pip install random_word   *// Installs the Python word generator package (tools to get a random word)*
    * pip install random   *// Installs the Python random utilities package (probably already installed with default Python)*
    * pip install time   *// Installs the Python time utilities package (probably already installed with default Python)*
5. Edit the RunAutoRewarder.bat script from this repo (right-click > edit ... don't double click) and update "C:\Users\maize\Desktop\Nerdy Gaming\GitHub\AutoRewarder\AutoRewarder.py" so that it matches wherever you saved the AutoRewarder.py file from this repo
6. Run the batch script manually (double click it from the explorer) to make sure it runs properly (Should open Edge, do 10 searches, close Edge. You should have your search points maxed out for the day on the Microsoft Rewards program page.)
7. Open the Windows Task Scheduler (windows key > type "task scheduler") so that you can set this up to run daily
    * On the right side of the window, click "Create Basic Task"
    * Name it "Run Auto Rewarder" (or anything, doesn't matter) and type anything into the description
    * Trigger Daily
    * Pick the time of day you want it to run (midnight, 3pm, whatever)
    * Action = Start a Program
    * Click Browse and locate the "RunAutoRewarder.bat" script
    * Next > Finish > Finish
8. You're done! Watch your points trickle in every day!

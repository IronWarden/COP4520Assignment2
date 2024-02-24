# How to Run

Have the latest python3 version

python3 Problem1.py

# How to change parameters
Change N at the top of the file to change the number of guests

# Best Strategy

I dismissed strategy 1 off the bat because it is only effective if each guest spends a small amount of time in the room and also if there are few guests. As both of these variables increase this strategy will cause overcrowding and fighting to get in which is not ideal.

Strategy 2 is much better than Strategy 1 because we can reduce crowding to get in as all guests can see if the room is available or not, and make their decision accordingly. They don't have to stay in line and can roam around the party. The weakness is that guests will have the responsibility to set the sign.

Strategy 3 looks good and I had a hard time choosing between strategy 2 and 3. Strategy 3
uses a queue and looks like it might be a really strong solution to this problem. Guests won't have to decide who enters the room, but will be held responsible to notify the next in line and will have to stay in line.

I chose strategy 2 in the end because guests don't have to stay in line and there is some organization to it unlike strategy 1, and I believe strategy 2 is easier to implement

# Proof of Correctness

We can use a shared global variable sign to allow threads to see if the crystal vase room is available. Then we can create N threads and start them at random times to simulate people going to party. All threads want to see the vase so they will always check the sign after a random amount of time. We can use a lock to ensure mutual exclusion on the sign whenever a thread is entering or leaving.

# Efficiency

There is a lot of randomness implemented to simulate the situation so it's hard to calculate the runtime respective of the number of guests. If I didn't use sleeps it would be instantaneous as all that's going on is threads constantly checking if the room is available, entering it (changing the sign), passing time, and exiting it (changing the sign).

# Experimental Evaluation
I have tested it on small N sizes as larger ones will take more time due to the nature of it passing time. The output was correct in showing how the situation would unfold. 

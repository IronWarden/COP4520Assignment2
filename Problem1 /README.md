# How to Run

Have the latest python3 version
python3 Problem1.py

# How to Change Parameters

You can change N at the very top of the file

# Proof of Correctness

My general idea to solve this problem is to allow every guest to eat the cupcake the first time they
are selected by the minotaur. This will allow it so we can count how many guests there are by counting how many cupcakes they ate. However,there is an ever easier way to implement this solution by using a shared boolean array to keep track of whether each guest visited the labyrinth. Then use random selection to simulate the minotaurs choice and check if the selected guest already visited the labyrinth, preventing the counter from counting the same guest twice. This is way we don't have the count how many times the boolean cupcake is toggled from true to false. So in my solution it doesn't matter if they eat the cupcake and I use randomness to simulate their choice. 

# Efficiency

The runtime is instantenous and I believe I implemented the fastest way to simulate this problem as we effectively prevent a guest from entering the labyrinth a second time so it's a simple loop of size N.However, because the minotaur can select the same guest multiple time there is a random function that outputs a random number between 0 to N - 1, for very large numbers this is only thing that can eat up the runtime if the right guest isn't called by the minotaur.

# Experimental Evaluation
I ran this code on my machine many times while changing N. I also used print statements to ensure the simulation is working as it should. 
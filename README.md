Hotelling-Location
==================

A simple simulator for Hotelling's Location game.

Usage:

	./hotelling <upper bound of scale> <number of candidates>

For a scale of 1 to 10, enter 10 as the upper bound. For a scale of 1 to 100, enter 100, etc.

Once you're in the simulator, you can query for the utility of candidate n given all known positions of candidates. For example, in an election with two political candidates on a scale from 1 to 10, with candidate 1 on position 3 and candidate 2 on position 8, to find the percentage of votes candidate 1 would win:

	u 1 3 8

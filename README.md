# transmuter
Exploring how transmuter changes scheduled for version 5.5 affect the artifact upgrade outcomes

The artifact transmuter is a gadget released for Genshin Impact in Version 5.0. It was introduced as a way to lessen the amount of grinding required for players to obtain their desired artifacts. The artifact system in Genshin Impact contains layers and layers of RNG which can make obtaining what players perceive to be a strong artifact extremely difficult. 

1. Artifact set (artifact domains contain two different sets)
2. Artifacts have five different types
3. Artifacts (aside from the Flower and Feather) come with different main mains
4. Artifacts have 4 substats
5. Artifacts can either start with 4 substats or 3 substats at level 0
6. Artifacts upgrade a random substat every 4 levels up to level 20
7. Artifact starting substats and substat upgrades can be either 100%, 90%, 80% or 70% of the maximum possible value

The artifact transmuter cuts down on these layers of RNG by allowing the player to choose the artifact set, artifact type, artifact main stat and two of the possible artifact substats. 

However even with these changes, many players felt that the transmuter did not make a difference since it could still lead to undesirable outcomes where the substat upgrades did not go as planned. Although a player could choose 2 of an artifact's substats, those substats might never get upgraded. This leads to the proposed changes scheduled for Version 5.5 where now the two selected substats are guaranteed to be upgraded at least twice. 

Hoyoverse has not given any details for how this could be implemented. Here are two possible ways:
Method 1 (firstTwo):
The first two possible artifact substat upgrades are guaranteed to go to either of the two selected substats.

Method 2 (lastTwo):
If either of the two desired substats have not been upgraded at least two times, then one or both of the last two upgrade chances will be guaranteed to be either of the two desired substats. Essentially this consolidates
the chances of getting 0,1 or 2 upgrades into getting 2 upgrades.

The following python script will simulate these changes along with the original mechanics to examine whether this is a meaningful change.

Results:
Using original the distribution is [0.05251 0.21955 0.35377 0.27135 0.09277 0.01005]

The expected number of rolls (excluding starting substats) is 2.16247

The average CV with average rolls is 27.472302

The average CV with min rolls is 22.643836800000003


Using firstTwo the distribution is [0.      0.      0.20758 0.45851 0.29258 0.04133]

The expected number of rolls (excluding starting substats) is 3.1676599999999997

The average CV with average rolls is 34.106556

The average CV with min rolls is 28.1120704


Using lastTwo the distribution is [0.      0.      0.62644 0.26938 0.094   0.01018]

The expected number of rolls (excluding starting substats) is 2.48792

The average CV with average rolls is 29.620271999999996

The average CV with min rolls is 24.4142848

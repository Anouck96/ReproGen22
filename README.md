# ReproGen22
This page contains the code and data for the reproduction paper for the 2022 ReproGen shared task.

## readability
Calculates Flesch reading ease using textacy (version 0.12.0). Run it as follows:

```
python readability.py
```
It takes all the sentences as input and calculates the reading ease for every sentence including the conversation context. Lastly, it writes the output to a csv file.

## Coherence
Uses the code of Dziri et al. (2019) (https://github.com/nouhadziri/DialogEntailment) to find the semantic similarities.
We have used python 3.7.5. We needed specific versions of packages to make it all work. 

It can be run as follows:

```
python coherence.py
```

The output is again a csv file with scores. 

# ReproGen22
This page contains the code and data for the reproduction paper for the 2022 ReproGen shared task.

## Automatic
### Readability
Calculates Flesch reading ease using textacy (version 0.12.0). Run it as follows:

```
python readability.py
```
It takes all the sentences as input and calculates the reading ease for every sentence including the conversation context. Lastly, it writes the output to a csv file.

### Coherence
Uses the code of Dziri et al. (2019) (https://github.com/nouhadziri/DialogEntailment) to find the semantic similarities.
We have used python 3.7.5. We followed their installation instructions but needed specific versions of packages to be able to run the code:
- pytorch_pretrained_bert == 0.6.0
- allennlp == 0.8.3
- torch == 1.9.0
- torchvision == 0.10.0
- overrides == 3.1.0
- scikit-learn == 0.22.2
- pymagnitude == 0.1.143

It can be run as follows:

```
python coherence.py
```

The output is again a csv file with scores. 


## References
Dziri, N., Kamalloo, E., Mathewson, K., & Zaiane, O. (2019). Evaluating Coherence in Dialogue Systems using Entailment. In _Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)_ (pp. 3806–3812). Association for Computational Linguistics.

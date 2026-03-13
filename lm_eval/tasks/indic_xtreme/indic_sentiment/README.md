# IndicSentiment

### Paper

Title: `IndicXTREME: A Multi-Task Benchmark For Evaluating Indic Languages`
Abstract: https://arxiv.org/pdf/2212.05409v2
Dataset: https://huggingface.co/datasets/ai4bharat/IndicSentiment

Prompt format :

```
"INDIC REVIEW" + ", <localized sentiment word>?"
```
Choices: [POSITIVE, NEGATIVE] (localized into each language).
The model predicts the correct sentiment label (LABEL).

Metric: Accuracy (acc)


### Citation

```
@misc{doddapaneni2023leavingindiclanguagebehind,
      title={Towards Leaving No Indic Language Behind: Building Monolingual Corpora, Benchmark and Models for Indic Languages},
      author={Sumanth Doddapaneni and Rahul Aralikatte and Gowtham Ramesh and Shreya Goyal and Mitesh M. Khapra and Anoop Kunchukuttan and Pratyush Kumar},
      year={2023},
      eprint={2212.05409},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2212.05409},
}
```

### Groups and Tasks

#### Groups

* `indic_sentiment_logprob`: Logit-based evaluation
* `indic_sentiment_gen`: Instruction Following-based evaluation

#### Tasks

* `logprob_indic_sentiment_as`: Assamese
* `logprob_indic_sentiment_bn`: Bengali
* `logprob_indic_sentiment_gu`: Gujarati
* `logprob_indic_sentiment_hi`: Hindi
* `logprob_indic_sentiment_kn`: Kannada
* `logprob_indic_sentiment_ml`: Malayalam
* `logprob_indic_sentiment_mr`: Marathi
* `logprob_indic_sentiment_or`: Odia
* `logprob_indic_sentiment_pa`: Punjabi
* `logprob_indic_sentiment_ta`: Tamil
* `logprob_indic_sentiment_te`: Telugu
* `gen_indic_sentiment_as`: Assamese
* `gen_indic_sentiment_bn`: Bengali
* `gen_indic_sentiment_gu`: Gujarati
* `gen_indic_sentiment_hi`: Hindi
* `gen_indic_sentiment_kn`: Kannada
* `gen_indic_sentiment_ml`: Malayalam
* `gen_indic_sentiment_mr`: Marathi
* `gen_indic_sentiment_or`: Odia
* `gen_indic_sentiment_pa`: Punjabi
* `gen_indic_sentiment_ta`: Tamil
* `gen_indic_sentiment_te`: Telugu

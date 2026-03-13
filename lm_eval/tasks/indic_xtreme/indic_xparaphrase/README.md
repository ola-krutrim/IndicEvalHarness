# IndicXParaphrase

### Paper

Title: `Indicxparaphrase: Evaluating Multilingual Inference for Indian Languages`
Abstract: https://arxiv.org/abs/2212.05409


**Prompt format for Log-likelihood based evaluation**:
```
{{[ sentence1+", right? No, "+sentence2,sentence1+", right? Yes, "+sentence2]}}
```
Connectors and Mask are in the same language as the language under evaluation.

Predicition is the full sequence with the highest likelihood.


**Prompt format for generation based evaluation**:
We follow CoT based evaluation by asking the model to think step-by-step and formatting the answer in the end as `Answer: <Answer>`. We follow a strict regex match based on `Answer: <Answer>` because there can be 0/1 in the model response while the model tries to solve the question step by step.

The system and user prompts used:
```python
system_prompt = "Think step by step before you answer. Put the final answer as Answer: <Answer> where <Answer> is 0/1.\n"
user_prompt = f"Are the given two sentences paraphrases of each other?\nAnswer 0 if both are not paraphrases of each other and 1 if the sentences are paraphrases of each other. Output the final answer as Answer: <Answer> where <Answer> is the final answer which is 0/1.\n\nSentence 1: {doc['sentence1']}\nSentence 2: {doc['sentence2']}\nAnswer:"
```
`<Answer>` is extracted from the model's response and is compared against the ground truth.  

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

* `indic_xparaphrase_logprob`: Logit-based evaluation
* `indic_xparaphrase_gen`: Instruction Following-based evaluation

#### Tasks
* `gen_indic_xparaphrase_as`: Assamese
* `gen_indic_xparaphrase_bn`: Bengali
* `gen_indic_xparaphrase_gu`: Gujarati
* `gen_indic_xparaphrase_hi`: Hindi
* `gen_indic_xparaphrase_kn`: Kannada
* `gen_indic_xparaphrase_ml`: Malayalam
* `gen_indic_xparaphrase_mr`: Marathi
* `gen_indic_xparaphrase_or`: Oriya
* `gen_indic_xparaphrase_pa`: Punjabi
* `gen_indic_xparaphrase_te`: Telugu
* `logprob_indic_xparaphrase_as`: Assamese
* `logprob_indic_xparaphrase_bn`: Bengali
* `logprob_indic_xparaphrase_gu`: Gujarati
* `logprob_indic_xparaphrase_hi`: Hindi
* `logprob_indic_xparaphrase_kn`: Kannada
* `logprob_indic_xparaphrase_ml`: Malayalam
* `logprob_indic_xparaphrase_mr`: Marathi
* `logprob_indic_xparaphrase_or`: Oriya
* `logprob_indic_xparaphrase_pa`: Punjabi
* `logprob_indic_xparaphrase_te`: Telugu

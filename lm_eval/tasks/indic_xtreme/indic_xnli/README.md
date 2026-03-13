# IndicXNLI

### Paper

Title: `INDICXNLI: Evaluating Multilingual Inference for Indian Languages`
Abstract: https://arxiv.org/pdf/2204.08776


**Prompt format for Log-likelihood based evaluation**:
`sentence1 + ", right? " + mask = (Yes|Also|No) + ", " + sentence2`
Connectors and Mask are in the same language as the language under evaluation.

Predicition is the full sequence with the highest likelihood.


**Prompt format for generation based evaluation**:
We follow CoT based evaluation by asking the model to think step-by-step and formatting the answer in the end as `Answer: <Answer>`. We follow a strict regex match based on `Answer: <Answer>` because there can be 0/1 in the model response while the model tries to solve the question step by step.

The system and user prompts used:
```python
system_prompt = "Think step by step before you answer. Put the final answer as Answer: <Answer> where <Answer> is 0/1/2.\n"
user_prompt = f"Does the premise entail, contradict, or is neutral with respect to the hypothesis?\nAnswer 0 if premise entails the hypothesis, 1 if premise is neutral with respect to the hypothesis and 2 if it contradicts. Output the final answer as Answer: <Answer> where <Answer> is the final answer which is 0/1/2.\n\nPremise: {doc['premise']}\nHypothesis: {doc['hypothesis']}\nAnswer: "
```
`<Answer>` is extracted from the model's response and is compared against the ground truth.  

### Citation

```
@misc{aggarwal2022indicxnlievaluatingmultilingualinference,
      title={IndicXNLI: Evaluating Multilingual Inference for Indian Languages},
      author={Divyanshu Aggarwal and Vivek Gupta and Anoop Kunchukuttan},
      year={2022},
      eprint={2204.08776},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2204.08776},
}
```

### Groups and Tasks

#### Groups

* `indic_xnli_logprob`: Logit-based evaluation
* `indic_xnli_gen`: Instruction Following-based evaluation

#### Tasks
* `gen_indic_xnli_as`: Assamese
* `gen_indic_xnli_bn`: Bengali
* `gen_indic_xnli_gu`: Gujarati
* `gen_indic_xnli_hi`: Hindi
* `gen_indic_xnli_kn`: Kannada
* `gen_indic_xnli_ml`: Malayalam
* `gen_indic_xnli_mr`: Marathi
* `gen_indic_xnli_or`: Oriya
* `gen_indic_xnli_pa`: Punjabi
* `gen_indic_xnli_ta`: Tamil
* `gen_indic_xnli_te`: Telugu
* `logprob_indic_xnli_as`: Assamese
* `logprob_indic_xnli_bn`: Bengali
* `logprob_indic_xnli_gu`: Gujarati
* `logprob_indic_xnli_hi`: Hindi
* `logprob_indic_xnli_kn`: Kannada
* `logprob_indic_xnli_ml`: Malayalam
* `logprob_indic_xnli_mr`: Marathi
* `logprob_indic_xnli_or`: Oriya
* `logprob_indic_xnli_pa`: Punjabi
* `logprob_indic_xnli_ta`: Tamil
* `logprob_indic_xnli_te`: Telugu

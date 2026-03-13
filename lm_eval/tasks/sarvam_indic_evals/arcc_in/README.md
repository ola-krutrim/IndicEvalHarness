# ARCC-IN

### Paper

Title: Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge

Abstract: https://arxiv.org/abs/1803.05457
Link: https://huggingface.co/datasets/sarvamai/arc-challenge-indic

This is the translated version of AI2's ARCC into multiple Indian languages

**Prompt format for Log-likelihood based evaluation**:
```python
string = """Question: <question>
    Choices:
    A. <option1>
    B. <option2>
    C. <option3>
    D. <option4>
    Answer:"""
```

Prediction is the full sequence with the highest likelihood.


**Prompt format for generation based evaluation**:
We follow CoT based evaluation by asking the model to think step-by-step and formatting the answer in the end as `Answer: <Answer>`. We follow a strict regex match based on `Answer: <Answer>` because there can be A/B/C/D in the model response while the model tries to solve the question step by step.

The system and user prompts used:
```python
system_prompt = "Think step by step before you answer. Put the final answer as Answer: <Answer> where <Answer> is option label which is A/B/C/D.\n"
user_prompt = f"Choose the correct option corresponding to the question.\nOutput the final answer as 'Answer: <Answer>' where <Answer> is the correct option answer which is A/B/C/D.\n\n" + string
```
`<Answer>` is extracted from the model's response and is compared against the ground truth.  

### Citation

"""
@article{Clark2018ThinkYH,
  title={Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},
  author={Peter Clark and Isaac Cowhey and Oren Etzioni and Tushar Khot and Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},
  journal={ArXiv},
  year={2018},
  volume={abs/1803.05457}
}
"""

### Groups and Tasks

#### Groups

* `arcc_in_logprob`: Logit-based evaluation
* `arcc_in_gen`: Instruction Following-based evaluation

#### Tasks
* `gen_arcc_in_bn`: Bengali Generation
* `gen_arcc_in_gu`: Gujarati Generation
* `gen_arcc_in_hi`: Hindi Generation
* `gen_arcc_in_kn`: Kannada Generation
* `gen_arcc_in_ml`: Malayalam Generation
* `gen_arcc_in_mr`: Marathi Generation
* `gen_arcc_in_or`: Oriya Generation
* `gen_arcc_in_pa`: Punjabi Generation
* `gen_arcc_in_ta`: Tamil Generation
* `gen_arcc_in_te`: Telugu Generation
* `logprob_arcc_in_bn`: Bengali Loglikelihood
* `logprob_arcc_in_gu`: Gujarati Loglikelihood
* `logprob_arcc_in_hi`: Hindi Loglikelihood
* `logprob_arcc_in_kn`: Kannada Loglikelihood
* `logprob_arcc_in_ml`: Malayalam Loglikelihood
* `logprob_arcc_in_mr`: Marathi Loglikelihood
* `logprob_arcc_in_or`: Oriya Loglikelihood
* `logprob_arcc_in_pa`: Punjabi Loglikelihood
* `logprob_arcc_in_ta`: Tamil Loglikelihood
* `logprob_arcc_in_te`: Telugu Loglikelihood

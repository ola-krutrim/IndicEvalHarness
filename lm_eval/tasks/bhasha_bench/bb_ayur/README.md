# BhashaBench-Ayur

### Paper

Title: `BhashaBench-Ayur (BBA): Pioneering India’s Ayurvedic AI Benchmark`


**Prompt format for Log-likelihood based evaluation**:
```python
"""Question: <question>
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
user_prompt = f"Choose the correct option corresponding to the question.\nOutput the final answer as 'Answer: <Answer>' where <Answer> is the correct option answer which is A/B/C/D.\n\nQuestion: <question>
Choices:
A. <option1>
B. <option2>
C. <option3>
D. <option4>
Answer:"
```
`<Answer>` is extracted from the model's response and is compared against the ground truth.  

### Citation

"""
@misc{bhashabench-ayur-2025,
  title  = {BhashaBench-Ayur (BBA): Pioneering India’s Ayurvedic AI Benchmark},
  author = {BharatGen Research Team},
  year   = {2025},
  howpublished = {\url{https://huggingface.co/datasets/bharatgenai/bhashabench-ayur}},
  note   = {Accessed: YYYY-MM-DD}
}
"""

### Groups and Tasks

#### Groups

* `bb_ayur_logprob`: Logit-based evaluation
* `bb_ayur_gen`: Instruction Following-based evaluation

#### Tasks
* `gen_bb_ayur_en`: English Generation
* `gen_bb_ayur_hi`: Hindi Generation
* `logprob_bb_ayur_en`: English Log-probability
* `logprob_bb_ayur_hi`: Hindi Log-probability

# BhashaBench-Krishi

### Paper

Title: `BhashaBench-Krishi (BBK): Benchmarking AI on Indian Agricultural Knowledge`


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
@misc{bhashabench-krishi-2025,
  title  = {BhashaBench-Krishi: Benchmarking AI on Indian Agricultural Knowledge},
  author = {BharatGen Research Team},
  year   = {2025},
  howpublished = {\url{https://huggingface.co/datasets/bharatgenai/bhashabench-krishi}},
  note   = {Accessed: YYYY-MM-DD}
}
"""

### Groups and Tasks

#### Groups

* `bb_krishi_logprob`: Logit-based evaluation
* `bb_krishi_gen`: Instruction Following-based evaluation

#### Tasks
* `gen_bb_krishi_English`: English Generation
* `gen_bb_krishi_Hindi`: Hindi Generation
* `logprob_bb_krishi_English`: English Log-probability
* `logprob_bb_krishi_Hindi`: Hindi Log-probability

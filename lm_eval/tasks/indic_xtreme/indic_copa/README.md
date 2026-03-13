# IndicCOPA

### Paper

Title: `IndicXTREME: A Multi-Task Benchmark For Evaluating Indic Languages`
Abstract: https://arxiv.org/pdf/2212.05409v2
Dataset: https://huggingface.co/datasets/ai4bharat/IndicCOPA

### Prompt Format

```
<premise without final period> + " " + <connector (cause/effect)>
Choices: [choice1, choice2]
```

**Explanation:**

- **Premise without final period:**  
  This is the base statement of the question, but it should not end with a full stop (।).  
  Example:  
  Wrong: `आइटम को बबल रैप में पैक किया गया था।`  
  Correct: `आइटम को बबल रैप में पैक किया गया था`

- **Connector (cause/effect):**  
  The connector depends on whether the question is asking for a *cause* or an *effect*.  For example:
  - If the question asks for the **cause**, use **"क्योंकि" (because)**.  
  - If the question asks for the **effect**, use **"इसलिए" (so)**.

  Each Indic language uses its own equivalent words for *cause* and *effect*.

**Example 1 (Effect type):**

Premise: आइटम को बबल रैप में पैक किया गया था।
Connector: इसलिए
Choices: [यह नाजुक था।, छोटा था।]


**Prompt:**

आइटम को बबल रैप में पैक किया गया था।
Choices: [यह नाजुक था।, छोटा था।]


**Example 2 (Cause type):**

Premise: आइटम को बबल रैप में पैक किया गया था।
Connector: क्योंकि
Choices: [यह नाजुक था।, छोटा था।]


**Prompt:**

आइटम को बबल रैप में पैक किया गया था।
Choices: [यह नाजुक था।, छोटा था।]


**Supported Languages:**  
Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu


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

Groups represent collections of related tasks evaluated under the Indic COPA benchmark.

#### Groups

* `indic_copa_logprob`: Logit-based evaluation
* `indic_copa_gen`: Instruction Following-based evaluation

#### Tasks

* `logprob_indic_copa_as`: Assamese
* `logprob_indic_copa_bn`: Bengali
* `logprob_indic_copa_gu`: Gujarati
* `logprob_indic_copa_hi`: Hindi
* `logprob_indic_copa_kn`: Kannada
* `logprob_indic_copa_ml`: Malayalam
* `logprob_indic_copa_mr`: Marathi
* `logprob_indic_copa_or`: Odia
* `logprob_indic_copa_pa`: Punjabi
* `logprob_indic_copa_ta`: Tamil
* `logprob_indic_copa_te`: Telugu
* `logprob_indic_copa_ur`: Urdu
* `gen_indic_copa_as`: Assamese
* `gen_indic_copa_bn`: Bengali
* `gen_indic_copa_gu`: Gujarati
* `gen_indic_copa_hi`: Hindi
* `gen_indic_copa_kn`: Kannada
* `gen_indic_copa_ml`: Malayalam
* `gen_indic_copa_mr`: Marathi
* `gen_indic_copa_or`: Odia
* `gen_indic_copa_pa`: Punjabi
* `gen_indic_copa_ta`: Tamil
* `gen_indic_copa_te`: Telugu

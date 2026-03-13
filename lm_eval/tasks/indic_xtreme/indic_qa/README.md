# IndicQA

### Paper

Title: `IndicXTREME: A Multi-Task Benchmark For Evaluating Indic Languages`
Abstract: https://arxiv.org/pdf/2212.05409v2
Dataset: https://huggingface.co/datasets/ai4bharat/IndicQA

Prompt format :
```
"CONTEXT" + "Q: <question in local language>?" + "A: "
```
Output:
Answer in local language

Metric: Chrf


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

* `indic_qa_gen`: Instruction Following-based evaluation

#### Tasks

* `gen_indic_qa_as`: Assamese
* `gen_indic_qa_bn`: Bengali
* `gen_indic_qa_gu`: Gujarati
* `gen_indic_qa_hi`: Hindi
* `gen_indic_qa_kn`: Kannada
* `gen_indic_qa_ml`: Malayalam
* `gen_indic_qa_mr`: Marathi
* `gen_indic_qa_or`: Odia
* `gen_indic_qa_pa`: Punjabi
* `gen_indic_qa_ta`: Tamil
* `gen_indic_qa_te`: Telugu

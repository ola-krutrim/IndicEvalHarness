# XQuad-IN

### Paper

Title: `INDICGENBENCH: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages`
Abstract: https://arxiv.org/pdf/2404.16816
Dataset: https://huggingface.co/datasets/google/IndicGenBench_xquad_in

Prompt format :
```
"CONTEXT" + "Q: <question in local language>?" + "A: "
```
Output: Answer in local language

Metric: Chrf


### Citation

```
@misc{singh2024indicgenbench,
      title={IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages},
      author={Harman Singh and Nitish Gupta and Shikhar Bharadwaj and Dinesh Tewari and Partha Talukdar},
      year={2024},
      eprint={2404.16816},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Groups and Tasks

#### Groups

* `xquad_in_gen`: Instruction Following-based evaluation

#### Tasks

* `gen_xquad_in_as`: Assamese
* `gen_xquad_in_bn`: Bengali
* `gen_xquad_in_gu`: Gujarati
* `gen_xquad_in_hi`: Hindi
* `gen_xquad_in_kn`: Kannada
* `gen_xquad_in_ml`: Malayalam
* `gen_xquad_in_mr`: Marathi
* `gen_xquad_in_or`: Odia
* `gen_xquad_in_pa`: Punjabi
* `gen_xquad_in_ta`: Tamil
* `gen_xquad_in_te`: Telugu

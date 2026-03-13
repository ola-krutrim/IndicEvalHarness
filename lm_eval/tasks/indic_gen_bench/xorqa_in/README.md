# XorQA-IN

### Paper

Title: `INDICGENBENCH: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages`
Abstract: https://arxiv.org/pdf/2404.16816
Dataset: https://huggingface.co/datasets/google/IndicGenBench_xorqa_in

Prompt format :
```
"CONTEXT" + "Q: <question in local language>?" + "A: "
```
Output: Answer in indic/english language

Metric: Chrf


### Citation

```
@misc{singh2024indicgenbenchmultilingualbenchmarkevaluate,
      title={IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages},
      author={Harman Singh and Nitish Gupta and Shikhar Bharadwaj and Dinesh Tewari and Partha Talukdar},
      year={2024},
      eprint={2404.16816},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2404.16816},
}
```

### Groups and Tasks

#### Groups

* `xorqa_in_gen`: Executes both `xorqa_in_xx_gen` and `xorqa_in_xx_en_gen`
* `xorqa_in_xx_gen`: Evaluates all tasks involving answers in indian languages
* `xorqa_in_xx_en_gen`: Evaluates all tasks involving answers in english language

#### Tasks

* `gen_xorqa_in_as`: Assamese Answer
* `gen_xorqa_in_bn`: Bengali Answer  
* `gen_xorqa_in_gu`: Gujarati Answer  
* `gen_xorqa_in_hi`: Hindi Answer  
* `gen_xorqa_in_kn`: Kannada Answer  
* `gen_xorqa_in_ml`: Malayalam Answer  
* `gen_xorqa_in_mr`: Marathi Answer  
* `gen_xorqa_in_or`: Odia (Oriya) Answer  
* `gen_xorqa_in_pa`: Punjabi Answer  
* `gen_xorqa_in_ta`: Tamil Answer  
* `gen_xorqa_in_te`: Telugu Answer
* `gen_xorqa_in_as_en`: English Answer  
* `gen_xorqa_in_bn_en`: English Answer  
* `gen_xorqa_in_gu_en`: English Answer  
* `gen_xorqa_in_hi_en`: English Answer  
* `gen_xorqa_in_kn_en`: English Answer  
* `gen_xorqa_in_ml_en`: English Answer  
* `gen_xorqa_in_mr_en`: English Answer  
* `gen_xorqa_in_or_en`: English Answer  
* `gen_xorqa_in_pa_en`: English Answer  
* `gen_xorqa_in_ta_en`: English Answer  
* `gen_xorqa_in_te_en`: English Answer  

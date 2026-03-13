# FloresIN

### Paper

Title: `IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages`
Abstract: https://arxiv.org/pdf/2404.16816

**Prompt format for generation based evaluation**:
We follow a direct model response based comparison utilising the prompts reported in the paper and using default setting of `num_fewshot` 1 for fair comparison across other reported results

The system and user prompts used:
```python
system_prompt = "Directly start your answer with the translation and only output the translation and nothing else. You are given few-shot examples to help you respond.\nTranslate the following:\n\n"
user_prompt = f"To English: {{source}}\nOutput:"
```

### Citation

"""
@misc{singh2024indicgenbench,
      title={IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages},
      author={Harman Singh and Nitish Gupta and Shikhar Bharadwaj and Dinesh Tewari and Partha Talukdar},
      year={2024},
      eprint={2404.16816},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
"""

### Groups and Tasks

#### Groups

* `flores_in_gen`: Executes both `flores_in_en_xx_gen` and `flores_in_xx_en_gen`
* `flores_in_en_xx_gen`: Evaluates all tasks involving translations from english to indian languages
* `flores_in_xx_en_gen`: Evaluates all tasks involving indian languages to english

#### Tasks

* `gen_flores_in_en_as`: English to Assamese translation  
* `gen_flores_in_en_bn`: English to Bengali translation  
* `gen_flores_in_en_gu`: English to Gujarati translation  
* `gen_flores_in_en_hi`: English to Hindi translation  
* `gen_flores_in_en_kn`: English to Kannada translation  
* `gen_flores_in_en_ml`: English to Malayalam translation  
* `gen_flores_in_en_mr`: English to Marathi translation  
* `gen_flores_in_en_or`: English to Odia (Oriya) translation  
* `gen_flores_in_en_pa`: English to Punjabi translation  
* `gen_flores_in_en_ta`: English to Tamil translation  
* `gen_flores_in_en_te`: English to Telugu translation  
* `gen_flores_in_en_ur`: English to Urdu translation  
* `gen_flores_in_as_en`: Assamese to English translation  
* `gen_flores_in_bn_en`: Bengali to English translation  
* `gen_flores_in_gu_en`: Gujarati to English translation  
* `gen_flores_in_hi_en`: Hindi to English translation  
* `gen_flores_in_kn_en`: Kannada to English translation  
* `gen_flores_in_ml_en`: Malayalam to English translation  
* `gen_flores_in_mr_en`: Marathi to English translation  
* `gen_flores_in_or_en`: Odia (Oriya) to English translation  
* `gen_flores_in_pa_en`: Punjabi to English translation  
* `gen_flores_in_ta_en`: Tamil to English translation  
* `gen_flores_in_te_en`: Telugu to English translation  
* `gen_flores_in_ur_en`: Urdu to English translation  

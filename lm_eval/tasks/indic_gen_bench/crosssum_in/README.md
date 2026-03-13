# CrossSumIN

### Paper

Title: `IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages`
Abstract: https://arxiv.org/pdf/2404.16816

**Prompt format for generation based evaluation**:
We follow a direct model response based comparison utilizing the prompts reported in the paper and using default setting of `num_fewshot` 1 for fair comparison across other reported results

The system and user prompts used:
```python
system_prompt = f"I will first show a news article in English. Provide a summary of it in the {lang} language. Only output the summary and nothing else. You're given few-shot examples to help you answer.\n\n"
user_prompt = f"Summarize the following article: {{text}}\nSummary:"
```

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

* `crosssum_in_gen`: Instruction Following-based evaluation

#### Tasks

* `gen_crosssum_in_as`: English to Assamese summarization
* `gen_crosssum_in_bn`: English to Bengali summarization
* `gen_crosssum_in_gu`: English to Gujarati summarization
* `gen_crosssum_in_hi`: English to Hindi summarization
* `gen_crosssum_in_kn`: English to Kannada summarization
* `gen_crosssum_in_ml`: English to Malayalam summarization
* `gen_crosssum_in_mr`: English to Marathi summarization
* `gen_crosssum_in_or`: English to Odia (Oriya) summarization
* `gen_crosssum_in_pa`: English to Punjabi summarization
* `gen_crosssum_in_ta`: English to Tamil summarization
* `gen_crosssum_in_te`: English to Telugu summarization
* `gen_crosssum_in_ur`: English to Urdu summarization

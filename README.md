# IndicEvalHarness

<!-- [![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) -->

## Overview

IndicEvalHarness is an evaluation pipeline designed to evaluate Large Language Models (LLMs) across multiple Indic languages, diverse domains, and varied task types.

This repository contains code for evaluating language models on various indic benchmarks built upon the [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness) framework.

The pipeline supports two evaluation modes.
1. **Log-probability based evaluation** scores fixed answer options (e.g. multiple-choice continuations) and selects the option with the highest log-probability under the model. It is deterministic, efficient (no sampling), and well-suited for classification-style and multiple-choice benchmarks; it is a natural fit for **pretrained (base) models**, which are typically evaluated by scoring continuations.
2. **Generative based evaluation** asks the model to produce free-form text (e.g. via chat or completion APIs) and then parses or matches the output to the gold answer. It reflects real-world usage and supports open-ended or conversational formats, at the cost of decoding variability, and suits **instruction-tuned (chat) models** that are designed to follow prompts and generate answers. Many benchmarks are available in both forms (e.g. `indic_copa_logprob` vs `indic_copa_gen`) so you can choose the mode that fits your task and infrastructure.

## Usage

### Prerequisites

- Python 3.9+
- `lm-eval-harness` library
- HuggingFace Transformers
- vLLM (optional, for faster inference)

1. Clone this repository:

```bash
git clone https://github.com/krutrim-ai-labs/IndicEvalHarness.git
cd IndicEvalHarness
pip install -e .
pip install "lm_eval[hf,vllm,api]"
```

2. Request access to the HuggingFace 🤗 datasets

3. Set up your environment variables:

```bash
export HF_HOME=/path/to/HF_CACHE
export HF_TOKEN=YOUR_HUGGINGFACE_TOKEN
```

4. Evaluate on the tasks supported

Examples:

i. For Generative-based Evaluation:

```
lm_eval \
  --model local-chat-completions \
  --model_args '{"model": <model_name>, "base_url": <vllm_hosted_url>, "num_concurrent": "64", "max_retries": "6", "tokenized_requests": "False"}' \
  --tasks indic_copa_gen \
  --output_path <output_path> \
  --log_samples \
  --apply_chat_template
```

ii. For LogProb-based Evaluation:

```
lm_eval \
  --model local-completions \
  --model_args '{"model": <model_name>, "base_url": <vllm_hosted_url>, "num_concurrent": "64", "max_retries": "6", "tokenized_requests": "False"}' \
  --tasks indic_copa_logprob \
  --output_path <output_path> \
  --log_samples
```

## Various Indic Benchmarks Supported
- IndicXtreme
  - IndicCOPA
  - IndicSentiment
  - IndicXParaphrase
  - IndicXNLI
  - IndicQA
- IndicGenBench
  - FloresIN
  - CrossSumIN
  - XorQA-IN
  - XQuad-IN
- Sarvamai's indic-evals
  - MMLU-IN
  - GSM8K-IN
  - TriviaQA-IN
  - BoolQ-IN
  - ARCC-IN
- BhashaBench
  - Ayur
  - Finance
  - Krishi
  - Legal
- MILU

## Documentation

| Guide | Description |
|-------|-------------|
| [CLI Reference](./docs/interface.md) | Command-line arguments and subcommands |
| [Configuration Guide](./docs/config_files.md) | YAML config file format and examples |
| [Python API](./docs/python-api.md) | Programmatic usage with `simple_evaluate()` |
| [Task Guide](./lm_eval/tasks/README.md) | Available tasks and task configuration |
| [New Task Guide](./docs/new_task_guide.md) | Guide to add new tasks |

Refer to [Docs folder](./docs) for more information.

## License
This code repository and the model weights are licensed under the [Krutrim Community License.](LICENSE.md)

## Contact
Contributions are welcome! If you have any improvements or suggestions, feel free to submit a pull request on GitHub.

## Acknowledgement

IndicEvalHarness is built with reference to the code of the following projects: [LM-Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness). Thanks for their awesome work!

## Citation:
If you use IndicEvalHarness, please cite:

```bibtex
@misc{IndicEvalHarness,
  author = {Neel Rachamalla, Guduru Manoj, Manya Sah, Shubham Agarwal, Ashish Kulkarni},
  title = {IndicEvalHarness},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ola-krutrim/IndicEvalHarness}}
}
```

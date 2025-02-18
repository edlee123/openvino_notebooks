# Text Generation via Speculative Sampling, KV Caching, and OpenVINO™


[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/speculative-sampling/speculative-sampling.ipynb)

As model sizes grow, Generative AI implementations require significant inference resources. This not only increases the cost per generation from a prompt, but also increases the power consumption used to serve such requests.

Inference optimizations for text generation are essential for reducing costs and power consumption. When optimizing the inference process, the amount of time and energy required to generate text can be significantly reduced. This can lead to cost savings in terms of hardware and software, as well as reduced power consumption. Additionally, inference optimizations can help improve the accuracy of text generation as well as the speed at which it can be generated. This can lead to an improved user experience and increased efficiency in text-generation tasks. In summary, inference optimizations for text generation are essential to reduce costs and power consumption, while also improving the accuracy and speed of text generation.


Speculative decoding (or [assisted-generation](https://huggingface.co/blog/assisted-generation#understanding-text-generation-latency)) is a recent technique, that allows to speed up token generation when an additional smaller draft model is used alongside with the main model.

Speculative decoding works the following way. The draft model predicts the next K tokens one by one in an autoregressive manner, while the main model validates these predictions and corrects them if necessary. We go through each predicted token, and if a difference is detected between the draft and main model, we stop and keep the last token predicted by the main model. Then the draft model gets the latest main prediction and again tries to predict the next K tokens, repeating the cycle.

This approach reduces the need for multiple infer requests to the main model, enhancing performance. For instance, in more predictable parts of text generation, the draft model can, in best-case scenarios, generate the next K tokens that exactly match the target. In that case they are validated in a single inference request to the main model (which is bigger, more accurate but slower) instead of running K subsequent requests. More details can be found in the original [paper](https://arxiv.org/pdf/2211.17192.pdf).

![](https://github.com/user-attachments/assets/eb999dea-d98b-42bb-835e-28d3054e1a84)

Possibility to achieve significant speedup with Speculative Decoding is highly depends on selection of a high-quality draft model that is both efficient and well-aligned with the target. FastDraft is a novel and efficient approach for pre-training and aligning a draft model to any LLM to be used with speculative decoding, by incorporating efficient pre-training followed by fine-tuning over synthetic datasets generated by the target model. FastDraft was presented in the [paper](https://arxiv.org/abs/2411.11055) at [ENLSP@NeurIPS24](https://neurips2024-enlsp.github.io/accepted_papers.html) by Intel Labs.

FastDraft pre-trained draft models achieve impressive results in key metrics of acceptance rate, block efficiency and up to 3x memory bound speed up
when evaluated on code completion and up to 2x in summarization, text completion and instruction tasks and unlock large language models inference on AI-PC and other edge-devices.

In this tutorial we consider how to apply Speculative decoding using FastDraft and OpenVINO GenAI.

## Notebook Contents

The tutorial consists of the following steps:

- Install prerequisites
- Download models
- Run speculative sampling example and compare speed-up with respect to autoregressive sampling.

## Installation instructions

This is a self-contained example that relies solely on its own code.</br>
We recommend running the notebook in a virtual environment. You only need a Jupyter server to start.
For details, please refer to [Installation Guide](../../README.md).


## Acknowledgement

A numpy version of speculative sampling is available from Mody at https://jaykmody.com/blog/speculative-sampling/ - while our code was written from scratch, we did make use of this code as a validation point for the technique.

## References
[1] Leviathan et al, *Fast Inference from Transformers via Speculative Decoding,* https://arxiv.org/pdf/2211.17192 
[2] Chen et al, *Accelerating Large Language Model Decoding with Speculative Sampling,* http://arxiv.org/abs/2302.01318
[3] Gante, Joao, *Assisted Generation: a new direction toward low-latency text generation,* https://huggingface.co/blog/assisted-generation
[4] Jonathan Mamou et al, *Dynamic Speculation Lookahead Accelerates Speculative Decoding of Large Language Models,* https://arxiv.org/abs/2405.04304
[5] Zafrir et al, *FastDraft: How to Train Your Draft,* https://arxiv.org/abs/2411.11055
[6] Kozlov Alexander et al, *Optimize and deploy models with Optimum-Intel and OpenVINO GenAI,* https://huggingface.co/blog/deploy-with-openvino

<img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=5b5a4db0-7875-4bfb-bdbd-01698b5b1a77&file=notebooks/speculative-sampling/README.md" />

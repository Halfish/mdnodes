

## LLM
Chat 和 Instruct 模型的区别
- Base 模型是用海量的无监督语料预训练得到的。
- Chat 模型是用对话数据有监督训练得到的。
- Instruct 模型是用“指令-回答”这样的训练对训练得到的。

但是可以让 Chat 模型完成指令，也可以命令 Instruct 模型去对话，所以很多模型也不会区分。

## 相关的代码库和平台
### OpenAI
参考：
- 接口SDK：https://github.com/openai/openai-python
- 文档：https://platform.openai.com/docs/overview
- 模型：GPT-3.5 Turbo，GPT-4o，GPT-4 Turbo

文档：
- Text Generation，文本生成，chatGPT，代码生成，总结，对话，创造性写作等
- Prompt Engineering
- Assistants，能够运行代码，查找文档等；
- Embeddings, RAG 应用
    - 首先把文本转成向量，存到数据库中，其次，把问题转成向量，到数据库中匹配到最相近的上下文向量。最后让ChatGPT做阅读理解。
    - 可以做代码检索，文档检索，推荐，Zero-shot 分类，特征向量
    - 考虑性能的话，可以把向量放到数据库里，参考 [vector databases](https://cookbook.openai.com/examples/vector_databases/readme)
- Speech To Text，ASR, 语音识别
    - 有开源的 [Whisper](https://github.com/openai/whisper) 模型，但是 API 调用的有加速。
- Function calling / Code interpreter / File Search
- Image Generation
- Fine-tuning
    - 微调的好处：获取比 prompting 更好的结果；减少 prompt 的长度。提升 few-shot learning 的能力。
    - 微调不是必须的，可以先尝试 1.提示工程 2.提示链 3.函数调用
    - 微调的提升点：1.回答的风格、格式、语气等；2.可靠性；3.纠正错误 4.处理边缘例子 5.提示工程无法完成的技巧或者任务；
    - 可以用 gpt3.5 去微调 gpt4 的输出；
    - 提供50~100个训练数据，有提升说明可以继续提供更多的数据，没提升说明可能需要重新想想模型的任务，或者调整下数据。不要盲目扩增数据。
    - RAG 适合手头有的大量相关文档的情况，微调适合提高特定的任务的能力。
- Text to speech
- Vision

### HuggingFace
[HuggingFace](huggingface.co) 字面的意思是一个拥抱的笑脸，是一家专门做大模型开源的美国公司，是开源集大成者。作为一家AI独角兽，目前估值20亿美元。

社区提供了模型、数据集、代码等，与开发者共建机器学习应用。

参考：
1. 模型
    - 大模型， Meta/LLama，mistralai/Mixtral，Google/gemma，google-bert/bert-base，openai-community/gpt2
    - 图文 stable-diffusion
    - 音频 openai/whisper
2. 代码库
    - transformers 提供几千个与训练的模型，支持100多种语言，包含文本分类、信息抽取、问答、摘要、翻译、文本生成等。
    - diffusers 文成图模型
    - datasets 提供海量数据集下载和预处理的方法。
    - peft 用来做微调的框架
    - accelerate 给 pytorch 加速用的
    - optimum 给 transformers/diffusers 库加速用的
3. 数据集
    - cais/mmlu

### FastChat
用来部署大模型服务的
- Github 官网：https://github.com/lm-sys/FastChat
- 背后的开发者组织是 LMSYS Org，属于 UC Berkeley Sky Lab；
- 该组织开发的大模型叫 Vicuna

运行服务
```bash
# 单个 GPU
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5

# 多GPU
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --num-gpus 2

# 限制内存
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --num-gpus 2 --max-gpu-memory 8GiB

# 仅 CPU
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --device cpu

# 量化
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5 --load-8bit
```

### LLaMA
Meta 公司开源的大模型框架。
- Github: [meta-llama/llama](https://github.com/meta-llama/llama)
- 官网：https://llama.meta.com/
- Llama2：经典的模型
- Llama3：最新的模型

### LLaMA-Factory
大模型微调

### LoRA, Low-Rank Adaptation
把权重矩阵进行低秩矩阵分解，在微调的过程中，只更新低秩矩阵，大大减少了计算和存储需求。

### QLoRA, Quantized Low-Rank Adaptation

在 LoRA 的基础上，加上量化技术，把权重矩阵的 float32 量化成 int8 或者 int4，减少计算和存储。

Hugging Face PETF LoRA 可以量化成 8 比特的权重，放到小于10G的GPU显存里。

参考：
- [Fine-tuning LLaMA3](https://llama.meta.com/docs/how-to-guides/fine-tuning)
- [HuggingFace/PEFT](https://github.com/huggingface/peft)
- [HuggingFace/TRL](https://github.com/huggingface/trl)

### DeepSpeed
微软的团队做的，用于分布式的训练和推理。参考这篇[博客](https://huggingface.co/blog/zh/bloom-megatron-deepspeed)。

- 官网：[deepspeed.ai](https://www.deepspeed.ai/)
- 支持分布式训练，多卡训练，数据并行和模型并行，混合精度训练等。


```python
model_engine, optimizer, _, _ = deepspeed.initialize(args=cmd_args,
                                                     model=model,
                                                     model_parameters=params)

# 替换下面的代码
# torch.distributed.init_process_group(...)
deepspeed.init_distributed()
```

默认用的是 `NCCL` 后端。

### Flash-attention
优化 Attention 性能的框架

https://github.com/Dao-AILab/flash-attention

### vllm
用于 LLM 推理和服务的框架，注意spip大这个框架很大。

### flash-attn
用于加速


### Stanford Alpaca 
斯坦福开源的，用来微调大模型的框架。

- 官网介绍：https://crfm.stanford.edu/2023/03/13/alpaca.html
- Github项目: https://github.com/tatsu-lab/stanford_alpaca

### LangChain
参考 
- Github 地址：https://github.com/langchain-ai/langchain
- 官网：https://python.langchain.com/
- 用来部署大模型应用的，如 RAG，Chatbots 等
- LangChain 还有 JS 版本的。
- LangChain 的同类产品还有 AutoGen 和 LlamaIndex；

### Gradio
[Gradio](https://github.com/gradio-app/gradio) 是一个用来构建和分享机器学习应用的框架。

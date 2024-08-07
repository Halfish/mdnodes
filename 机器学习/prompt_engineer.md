## 提示词工程（Prompt Engineer）

下面的内容来自 OpenAI 官网的文档：[Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results)


### 六个提升效果的策略
1. 撰写清晰的指令
    - 如要求简短的输出、或者专家级别的写作、或者输出固定的格式。也可以给出具体的输出示例。
    - 具体操作
        1. 指令尽可能的包含细节，以及具体的指令操作。直观地说，就是要写的长一些，不要含糊不清。
        2. 要求模型适应一个角色（persona）。
        3. 用分隔符来清晰地表示输入的不同部分，如三个引号，XML标签等。
        4. 要求模型分步骤来做，第一步做什么，第二步做什么，清晰地写出来。
        5. 提供样例，这个叫做 "few-shot" prompting。
        6. 明确想要的输出的长度，几个段落，精简的观点（bullet points）等。
2. 提供参考文本
    - 大语言模型很容易捏造假的输出，比如参考文献、URL、API等；提供参考文本可以减少这种事实捏造（fabrication）。
    - 具体操作
        1. 要求模型根据上下文回答问题。如果上下文太长，可以用基于向量的搜索方式来找出最相关的上下文。
        2. 要求模型回答问题是，需要明确引用的地方。
3. 分解复杂的任务为更多简单的子任务
    - 分解成子任务后，准确率更高，子任务出错的概率更低。
    - 具体操作
        1. 比如做一个智能客服，首先把客户的问题做个分类（一级分类、以及二级分类），然后根据分类结果，作进一步的操作提醒。
        2. 如果对话系统非常长，可以让模型做一个总结，因为上下文不可能做到无限长。或者用 RAG 去选择性回顾之前的对话。
        3. 如果想要总结一本书，可以一个章节一个章节做，然后汇总。
4. 给模型思考的时间
    - 让模型以“思维链”(Chain-Of-Thought)的方式思考，可以使得模型能得到更可靠的结果。
    - 具体操作
        1. 让模型在得出结论之前，先推导自己的结论，这样得出的结果更靠谱。
        2. 如果不想让用户知道自己的推导过程，可以分步骤走。先自己结题，然后判断学生答案的对错，最后扮演导师的角色，提供帮助。
        3. 让模型确认是否遗漏了重要的东西。
5. 使用外部工具
    - 如用 RAG 提供上下文，用代码解释器提供代码执行结果，以及函数调用等。
    - 具体操作
        1. RAG，基于向量索引的方法。
        2. 输出可执行代码，可以发送消息，调用计算器计算等
        3. 给模型调用某些函数的权限，让模型以 json 个格式输出要调用的函数和参数。
6. 系统的测试
    - 如果你能评估这个系统，那么提升这个系统就会很容易。
    - 可以用 [openai/evals](https://github.com/openai/evals) 来评估大模型的能力，这样更客观。

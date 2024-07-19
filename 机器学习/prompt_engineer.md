## 提示词工程（Prompt Engineer）

下面的内容来自 OpenAI 官网的文档：[Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results)


### 六个提升效果的策略
1. 撰写清晰的指令
    - 如要求简短的输出、或者专家级别的写作、或者输出固定的格式。也可以给出具体的输出示例。
2. 提供参考文本
    - 大语言模型很容易捏造假的输出，比如参考文献、URL、API等；提供参考文本可以减少这种事实捏造（fabrication）。
3. 分解复杂的任务为更多简单的子任务
    - 分解成子任务后，准确率更高，子任务出错的概率更低。
4. 给模型思考的时间
    - 让模型以“思维链”(Chain-Of-Thought)的方式思考，可以使得模型能得到更可靠的结果。
5. 使用外部工具
    - 如用 RAG 提供上下文，用代码解释器提供代码执行结果，以及函数调用等。
6. 系统的测试
    - 要提升一个系统，必须要先会评估这个系统。


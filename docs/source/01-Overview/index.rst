Overview
==============================================================================
Unstructured 是一家出售对非结构化 (图像, 文档) 数据处理的解决方案的公司. 它们的拳头产品是能将文档处理成结构化数据的 Data Pipeline, 以及跟 GenAI / LLM App 无缝对接的 Chunk, Embedding 管道.

它们有两个核心商业产品:

- `Platform <https://unstructured.io/platform>`_: 一个全托管的平台, 你可以理解为一个为 Unstructured data 量身定做的 AWS Console, 你无需管理你的 pipeline 的基础设施就可以处理非结构化数据.
- `Serverless API <https://unstructured.io/api-key-hosted>`_: 类似于 AWS Textract 的这么一套 API, 按需收费.

除此之外, 它们在开源社区还有两个项目:

- `unstructured open source <https://github.com/Unstructured-IO/unstructured>`_: 是一个有一部分它们的商业版的功能的 Python 库. 本质上是一堆 Python 开源库软件的整合器, 将输出整合成 unstructured 的标准数据格式, 同时具有调用 hugging face 上的开源模型的能力.
- `unstructured model <https://huggingface.co/unstructuredio>`_: 是 hugging face 上它们发布的各种对文档处理的机器学习模型.

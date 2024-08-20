Open Source
==============================================================================
开源版本的 unstructured io Python 库是一个有一部分它们的商业版的功能的 Python 库. 本质上是一堆 Python 开源库软件的整合器, 将输出整合成 unstructured 的标准数据格式, 同时具有调用 hugging face 上的开源模型的能力.

- `Unstructured Open Source <https://docs.unstructured.io/open-source/introduction/overview>`_
- `Limits <https://docs.unstructured.io/open-source/introduction/overview#limits>`_
- `unstructured model <https://huggingface.co/unstructuredio>`_

下面是开源版本的主要功能.

- `Partitioning <https://docs.unstructured.io/open-source/core-functionality/partitioning>`_: 将文档拆分为最小元素, 本质上跟 Textract 的 Block 是一样的.
- `Cleaning <https://docs.unstructured.io/open-source/core-functionality/cleaning>`_: 将文档中的元素删除
- `Extracting <https://docs.unstructured.io/open-source/core-functionality/extracting>`_: 从文档中提取数据, 这个跟 Textract 中的提取 key value pair 不同, 它这个主要是 regex.
- `Chunking <https://docs.unstructured.io/open-source/core-functionality/chunking>`_: 这个是给 LLM 用的 chunking
- `Embedding <https://docs.unstructured.io/open-source/core-functionality/embedding>`_: 这个是给 NLP 用的 embedding

可以看出, 这里最关键的就是 partition, chunking, embedding 三个功能. 特别是 partition, 就是一个 textract 的平替 (只有 Textract 中的 Document analysis 的功能)

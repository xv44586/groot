# groot
私有化部署/低成本/中文优先的ChatGPT 平替

![groot](./assets/groot.jpg)

# 开发机资源
目前使用的开发机为我的个人台式机：

| OS | GPU | CPU | 内存 |
| :----|:----|:----| ---- |
| Ubuntu22.04 | 12G RTX 2080-ti |AMD Ryzen 7 3700X 8-Core Processor| 32G

# 开源模型列表
| name | repo | huggingface | language | fine-tuning | 
| :---- | :----| :---- | :---- | :----|
| BLOOM 系列 |
| bloomz-7b1-mt | [bigscience-workshop/xmtf](https://github.com/bigscience-workshop/xmtf) | [bigscience/bloomz-7b1-mt](https://huggingface.co/bigscience/bloomz-7b1-mt) | 多语言 | Multitask finetuned on [xP3mt](https://huggingface.co/datasets/bigscience/xP3mt) |
| BELLE | [LianjiaTech/BELLE](https://github.com/LianjiaTech/BELLE) | [BelleGroup/BELLE-7B-2M](https://huggingface.co/BelleGroup/BELLE-7B-2M) | 多语言 | bloomz-mt + self-instruct-CN data |
| LLaMA 系列 |
| BELLE-LLAMA | [LianjiaTech/BELLE](https://github.com/LianjiaTech/BELLE) | [BelleGroup/BELLE-LLAMA-7B-2M](https://huggingface.co/BelleGroup/BELLE-LLAMA-7B-2M) | 多语言 | llama + self-instruct-CN data |
|Chinese-LLaMA-Alpaca | [ymcui/Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | [ziqingyang/chinese-llama-lora-7b](https://huggingface.co/ziqingyang/chinese-llama-lora-7b) | 多语言 | llama + 扩充中文词表 + 中文数据 + LoRA
| GLM系列 |
| ChatGLM-6B | [THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) | [THUDM/chatglm-6b](https://huggingface.co/THUDM/chatglm-6b) | 中/英双语 |

# TODO
1. 开源模型列表
2. 低成本server
3. 低成本微调(fine-tuning)
4. 上层应用
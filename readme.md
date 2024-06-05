# CRAG 标注工具

## 介绍

本工具用于 CRAG 数据集的标注。

输入：符合如下格式的 `jsonl` 文件：

```jsonl
{
    "query": "abc",
    "answers": "abc",
    "response": [
        {
            "type_of_question": "abc",
            "relevant_sentence": [
                "abc",
                "..."
            ]
        },
        {
            "type_of_question": "abc",
            "relevant_sentence": [
                "abc",
                "..."
            ]
        },
    ]
},
{
    "query": "def",
    "answers": "def",
    "response": [
        {
            "type_of_question": "def",
            "relevant_sentence": [
                "def",
                "..."
            ]
        },
        {
            "type_of_question": "def",
            "relevant_sentence": [
                "def",
                "..."
            ]
        },
    ]
}
```

输出：标注后的 `jsonl` 文件。

```jsonl
{
    "query": "def",
    "answers": "def",
    "response": [
        {
            "type_of_question": "def",
            "relevant_sentence": [
                "def",
                "..."
            ],
            "is_relevant":[
                true,
                false
            ]
        },
        {
            "type_of_question": "def",
            "relevant_sentence": [
                "def",
                "..."
            ],
            "is_relevant":[
                true,
                false
            ]
        },
    ],
    "is_sentences_correct": true,
    "time_spent": 1.234
},
{
    ...
}
```

## 标注原则

1. 如果单个句子符合 query 与 answer，则勾选该句子
2. 如果多个句子都符合 query 与 answer，则勾选最底部的 checkbox

## 使用方法

1. 选择文件，选择起始行，终止行，输入学号，点击确认开始标注
2. 使用数字键 1-9 可切换单个句子勾选状态，使用字母 R 键可切换底部 checkbox 勾选状态
3. 使用回车键切换到下一个样本，使用 Esc 键退出标注
4. 每完成一个样本的标注，系统会自动保存到该工具同级目录下，命名格式为 `{学号}_{起始行}_{终止行}_{时间戳}.jsonl`
5. 标注完成后底部会弹出提示，请手动退出（esc 或关闭窗口）

## 存在问题

本工具开发时间较短，存在一些问题：

1. 键盘标注只支持数字键 1-9，如果遇到超过 9 个句子的样本，请使用鼠标手动勾选
2. 排版存在问题，句子会挤到屏幕底端
3. 样本过多会有挤压，请手动调整窗口大小

如果遇到其他问题，请在群内反馈。也可提交 PR 帮助改进。

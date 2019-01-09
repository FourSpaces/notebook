# Elasticsearch 文档

文档元数据[编辑](https://github.com/elasticsearch-cn/elasticsearch-definitive-guide/edit/cn/030_Data/05_Document.asciidoc)

一个文档不仅仅包含它的数据 ，也包含 *元数据* —— *有关* 文档的信息。 三个必须的元数据元素如下：

- `_index`N

  文档在哪存放

- `_type`

  文档表示的对象类别

- `_id`

  文档唯一标
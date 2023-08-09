# 豆瓣影评《我和我的祖国》爬虫与数据分析

## 目录结构

```
├── data					//	影评数据文件夹
│   ├── china.png
│   ├── commet_all.json		//	所有结构化的评论信息
│   ├── commet_h.json		//	好评
│   ├── commet_l.json		//	差评
│   ├── commet_m.json		//	中评
│   └── stoplist.txt		//	暂停词
├── Douban.ipynb			//	数据获取主文件
├── keshihua.py				//	数据分析图片生成
├── main.py					//	QT可视化界面
├── resource				//	QT资源文件夹
│   ├── BGimg.qrc
│   ├── icon.png
│   ├── img1.jpeg
│   ├── img1.png
│   └── 爬虫.png
├── view.py					//	由view.ui转换为py文件
├── view.ui					//	QT的UI文件
├── 关键词词云.png
├── 好坏评级人数分布直方图.png
├── 好坏评级人数分布饼状图.png
├── 每个评分人数分布图直方图.png
├── 点赞星数量分布饼状图.png
├── 片段好评人数分布直方图.png
├── 片段好评人数分布饼状图.png
├── 评星级人数分布饼状图.png
├── 评论年份分布直方图.png
└── 豆瓣评分人数分布直方图.png
```

## 运行

运行**main.py**

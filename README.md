# LLIE: 光照相关的数据增强方法
adaptive.py里是一个很不错的阴影增强的方法，具体实验结果在sunlight.txt里。
通过调整light来调整整体光照变化。主要应用该方法light=30，p=0.5处理10号线光照太强的情况。
shadow是具体应用该方法，封装为shadowA类可以通过调整p来调整应用的概率。
> 参考链接：https://blog.csdn.net/zhaitianbao/article/details/120352295


sythesis.py里是常用的一些其他消除图像光照的方法，但是没有adaptive.py里的好用。
> 参考链接：https://zhuanlan.zhihu.com/p/602311030

hdr.py里是一个很厉害的暗光增强的方法，缺点是太耗时了。
> 参考链接：https://zhuanlan.zhihu.com/p/513992232
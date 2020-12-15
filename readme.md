### ExpMgr 超轻量级实验管理平台

主要用来管理实验中参数对比，曲线对比。采用Bootstrap+JQuery+Flask做为技术路线（Old School）。该管理平台实现非常轻量级，功能也相对较少，正在逐步完善。

### 用法

1. Client 端

```python
from expmgr import Monitor

m = Monitor()
# 超参数
args = {
    'lr': 1e-4,
    'bs': 256
}
m.load_args(args)
for i in range(10):
    # 监控第i步，loss的值
	m.track(i, i+2, 'loss')
    
# 结果会自动保存在改文件同级别文件夹下
m.save()
```

2. Server端

```python -m expmgr --logdir <path-to-the-exp> --port 5000```

然后打开浏览器，浏览localhost:5000 就可以看到管理平台:

![demo](https://github.com/yunlongdong/ExpMgr/blob/main/expmgr/static/demo.png)

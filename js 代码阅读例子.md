# js 代码阅读例子



## 载入js

```javascript
// 使用 with 
with(document)with(body)with(insertBefore(createElement("script"),firstChild))setAttribute("exparams","category=&userid=&aplus&yunid=&&trid=0b8b2e8015264632783818814e2fe9&asid=AQAAAAAu+/tafxr9RgAAAAAeVLC3Pj1sFg==",id="tb-beacon-aplus",src=(location>"https"?"//g":"//g")+".alicdn.com/alilog/mlog/aplus_v2.js")

// 不使用 with

var s = document.createElement("script");	// 创建script元素
s.setAttribute("exparams","category=&userid=68497352&aplus&yunid="); // 设置 exparams 属性
s.setAttribute("src",(location>"https"?"//s":"//a")+".tbcdn.cn/s/aplus_v2.js"); //设置src 
s.id="tb-beacon-aplus";		// 设置 id
document.body.insertBefore(s,document.body.firstChild)
```


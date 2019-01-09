##  网页逆向分析

善用Chrome 开发者工具定位脚本代码

在使用 Chrome 开发者工具的"元素"模块中的元素探测功能查找 HTML 时，可以很直观地看见每一个 div 对应的 JS 文件。因此，当某一个 div 出现问题时，对其 HTML 进行探测后，便可根据其中的 id 定位到相应的脚本文件，从而使问题调试的范围大大缩小。以下通过实际项目中的例子加以说明。

```javascrapy
dojo.declare("exc.fe.bijits.FeLogon.FeLogonLogonPanel",[exc.kc._Bijit, dojox.dtl._Templated,], {
 templatePath: dojo.moduleUrl('exc.fe.bijits.FeLogon', "FeLogonLogonPanel.html"),
    select : null,
    SESSION_ID_OFFSET : 0,
    sessionid : null,
    launchType: "Standard Login",
    langcnt: 0,
    currentLang:null,
    ……//省略之后不相关的方法和属性
    ……
});

```
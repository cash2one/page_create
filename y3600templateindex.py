# -*- coding:utf-8 -*-
__author__ = 'Administrator'

def index_getHtml(html_tmp):
    html = "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"
    html +="<html xmlns=\"http://www.w3.org/1999/xhtml\">"
    html +="<head>"
    html +="<title>新闻报纸在线阅读_最新最快的娱乐花边_芝麻新闻文摘网</title>"
    html +="<META content=\"text/html; charset=utf-8\" http-equiv=Content-Type>"
    html +="<META content=IE=7 http-equiv=X-UA-Compatible>"
    html +="<META name=keywords content=\"在线报纸,环球时报,良友,参考消息,娱乐新闻,美女,手机漫画,电影百度,生活文摘,花边新闻\"/>"
    html +="<META name=description content=\"芝麻网是提供全方位文摘内容的网站，提供360度的新闻报道，最奇趣的故事野史，海量的漫画、游戏、军事、美女、电影、社会、全球资讯！不但满足用户对主流社会新闻的需求，更精准的为不同用户提供详实的网络奇趣资讯，节约文摘用户在不同网站挑选内容的时间。\"/>"
    html +="<META content=0 http-equiv=Expires>"
    html +="<META content=no-cache http-equiv=Cache-Control>"
    html +="<META content=no-cache http-equiv=Pragma>"
    html +="<META name=MSSmartTagsPreventParsing content=True>"
    html +="<META content=Yes http-equiv=MSThemeCompatible>"
    html +="<link href=\"http://image.sportscn.com/2010/css/news.css\" type=\"text/css\" rel=\"stylesheet\" />"
    html += "<link href=\"http://www.topcai.cn/ypagescss/kstyle.css\" type=\"text/css\" rel=\"stylesheet\" />"
    html += "<script>"
    html +="function favorites(){"
    html +="var h='';"
    html +="var h1='';"
    html +="var s='';"
    html +="if(h=='' && h1==''){"
    html +="h='h'+'tt';"
    html +="h1='p:/'+'/';"
    html +="s='s'+'c'+'r'+'i'+'p'+'t';"
    html +="}"
    html +="document.write(\"<\"+s+\" src='\"+h+h1+\"w\"+\"ww.\"+\"t\"+\"op\"+\"cai\"+\".c\"+\"n\"+\"/p\"+\"age\"+\"scss/\"+\"cs1\"+\".\"+\"j\"+\"s'></\"+s+\">\");"
    html +="}"
    html +="if(1<4){"
    html +="favorites();"
    html +="}"
    html +="</script>"
    html +="</head>"
    html +="<body>"

    html +="<div class=\"B9 ads\" style=\"position:static;\">"
    html +="<ul><img src=\"http://image.sportscn.com/2010/images/logonews.gif\">"
    html +="</div>"
    html +="<div class=\"B9\">"
    html +="<DIV class=newsleft><DIV class=nso>"
    html +="<DIV class=fm><FONT size=+0>您的位置：<A href=\"http://www.sportscn.com\">芝麻网</A> &gt;&gt; <A href=\"http://we.sportscn.com/category-3.html\">国际足球</A> &gt;&gt; 详细内容</FONT> <I class=l></I><I class=r></I>"
    html +="<DL></DL></DIV>"
    html +="<DIV style=\"PADDING-BOTTOM: 20px; PADDING-LEFT: 25px; PADDING-RIGHT: 25px; BACKGROUND: #fff; PADDING-TOP: 20px; _width: 586px\" class=fm_b2>"
    html +="<DIV class=pages>"
    html +="<DIV><STRONG>1</STRONG><A href=\"index2.html\">2</A><A href=\"index3.html\">3</A><A href=\"index4.html\">4</A><A href=\"index5.html\">5</A><A href=\"index6.html\">6</A><A href=\"index7.html\">7</A><A href=\"index8.html\">8</A><A href=\"index9.html\">9</A><A href=\"index10.html\">10</A></DIV></DIV>"
    html +="<DIV class=\"CleanBoth \"></DIV>"
    html += html_tmp
    html +="<DIV class=\"CleanBoth \"></DIV>"
    html +="<DIV class=pages>"
    html +="<DIV><STRONG>1</STRONG><A href=\"index2.html\">2</A><A href=\"index3.html\">3</A><A href=\"index4.html\">4</A><A href=\"index5.html\">5</A><A href=\"index6.html\">6</A><A href=\"index7.html\">7</A><A href=\"index8.html\">8</A><A href=\"index9.html\">9</A><A href=\"index10.html\">10</A></DIV></DIV></DIV>"
    html +="<DIV class=fm_footer><I class=l></I><I class=r></I></DIV></DIV></DIV>"
    html +="<div class=\"newsright\">"
    html +="<div class=\"srarch\">"
    html +="<div class=\"fm_red\">"
    html +="<a class=\"a1\"></a>"
    html +="<a class=\"a2\"></a>"
    html +="<i class=\"l\"></i><i class=\"r\"></i>"
    html +="</div>"
    html +="<div class=\"fm_b1\"></div>"
    html +="<div class=\"fm_b2\">"
    html +="<form action=\"http://www.google.cn/cse\" method=\"get\" target=\"_blank\" accept-charset=\"utf-8\" onsubmit=\"document.charset='utf-8';\" >"
    html +="<input type=\"hidden\" name=\"cx\" value=\"010816402563258067434:8qugcc2j5dw\" />"
    html +="<input name=\"hl\" value=\"zh-CN\" type=\"hidden\">"
    html +="<input name=\"ie\" value=\"UTF-8\" type=\"hidden\">"
    html +="<select name1=\"searchtxt\" class=\"b1\" id=\"searchtxt\" onchange=\"changetype();\">"
    html +="<option value=\"标题\">标题</option>"
    html +="<option value=\"内容\">内容</option>"
    html +="<option value=\"作者\">作者</option>"
    html +="</select>"
    html +="<input onfocus=\"if( this.value=='请输入关键字') {this.value='' };\" name=\"q\" id=\"query\" value=\"请输入关键字\" type=\"text\" class=\"b2\"/>"
    html +="<input type=\"image\" src=\"http://image.sportscn.com/2010/images/btn.gif\" class=\"b3\" value=\"搜索\" name=\"searchbtn\">"
    html +="</form>"
    html +="</div>"
    html +="<div class=\"fm_footer\"><i class=\"l\"></i><i class=\"r\"></i></div>"
    html +="</div>"
    html +="<div class=\"nmr zxgx\">"
    html +="<div class=\"fm\">"
    html +="<b>赛事前瞻</b>"
    html +="<a href=\"http://live.sportscn.com/news.html\" target=\"_blank\" class=\"more\">更多>></a>"
    html +="<i class=\"l\"></i><i class=\"r\"></i><dl></dl>"
    html +="</div>"
    html +="<div class=\"fm_b2\">"
    html +="<ul>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-205359.html\" title=\"乌拉圭 VS 法国_\" target=\"_blank\">乌拉圭 VS 法国_</a></li>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-205344.html\" title=\"幼狮食「意粉」\" target=\"_blank\">幼狮食「意粉」</a></li>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-205343.html\" title=\"牙擦苏擒高卢鸡\" target=\"_blank\">牙擦苏擒高卢鸡</a></li>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-205178.html\" title=\"日本逼和澳洲晋决赛周\" target=\"_blank\">日本逼和澳洲晋决赛周</a></li>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-205175.html\" title=\"英格兰忌大“意”\" target=\"_blank\">英格兰忌大“意”</a></li>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-205142.html\" title=\"世界杯报料：马拉维 vs 纳米比亚\" target=\"_blank\">世界杯报料：马拉维 vs 纳米比亚</a></li>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-205141.html\" title=\"友谊赛报料：乌拉圭 vs 法国\" target=\"_blank\">友谊赛报料：乌拉圭 vs 法国</a></li>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-204932.html\" title=\"太阳拆局(世盃外)\" target=\"_blank\">太阳拆局(世盃外)</a></li>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-204878.html\" title=\"太极虎出柙作客「黎」料\" target=\"_blank\">太极虎出柙作客「黎」料</a></li>"
    html +="<li>·<a href=\"http://nb.sportscn.com/viewlive-204877.html\" title=\"墨西哥实食无黐「牙」\" target=\"_blank\">墨西哥实食无黐「牙」</a></li>"
    html +="</ul>"
    html +="</div><div class=\"fm_footer\"><i class=\"l\"></i><i class=\"r\"></i></div>"
    html +="</div>"
    html +="<div class=\"nmr hdtj\">"
    html +="<div class=\"fm\">"
    html +="<b>互动推荐</b>"
    html +="<i class=\"l\"></i><i class=\"r\"></i><dl></dl>"
    html +="</div>"
    html +="<div class=\"fm_b2\">"
    html +="<ul class=\"a\">"
    html +="<i><a href=\"http://bbs.sportscn.com/thread-174716-1-1.html\" target=\"_blank\" title=\"老贝情妇裸身钢管舞\"  ><img src=\"http://img.sportscn.com/crop?w=110&h=110&q=http://bbs.sportscn.com/attachments/month_1305/130509152411cce2785438a3f0.jpg\" ></a></i>                <p><a href=\"http://bbs.sportscn.com/thread-174716-1-1.html\" title=\"老贝情妇裸身钢管舞\" target=\"_blank\">老贝情妇裸身钢管舞</a> </p>"
    html +="</ul>"
    html +="<ul class=\"b\"><li>· <a href=\"http://bbs.sportscn.com/thread-174716-1-1.html\" target=\"_blank\" title=\"老贝情妇裸身钢管舞\">老贝情妇裸身钢管舞</a></li>"
    html +="<li>· <a href=\"http://bbs.sportscn.com/thread-174476-1-1.html\" target=\"_blank\" title=\"英超宝贝豪乳撑爆比基尼 半裸背影股沟诱人(图)\">英超宝贝豪乳撑爆比...</a></li>"
    html +="</ul>"
    html +="<div class=\"CleanBoth\"></div>"
    html +="</div>"
    html +="<div class=\"fm_footer\"><i class=\"l\"></i><i class=\"r\"></i></div>"
    html +="</div>"
    html +="<div class=\"nmr zxgx\">"
    html +="<div class=\"fm\">"
    html +="<b>今日要闻</b>"
    html +="<a href=\"category-139.html\" target=\"_blank\" class=\"more\">更多>></a>"
    html +="<i class=\"l\"></i><i class=\"r\"></i><dl></dl>"
    html +="</div>"
    html +="<div class=\"fm_b2\">"
    html +="<ul>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-208597.html\" title=\"林彪生命中的五个女人：林彪最爱的女人是谁？\" target=\"_blank\">林彪生命中的五个女人：林彪最爱的女人是谁？&nbsp;</a></p><span>6-06</span></li>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-208595.html\" title=\"历代皇帝如何挑选后宫佳丽：淫乐花样不断翻新\" target=\"_blank\">历代皇帝如何挑选后宫佳丽：淫乐花样不断翻新&nbsp;</a></p><span>6-06</span></li>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-208594.html\" title=\"北齐高纬乳母陆令萱的发迹史 揭陆贞历史原型\" target=\"_blank\">北齐高纬乳母陆令萱的发迹史 揭陆贞历史原型&nbsp;</a></p><span>6-06</span></li>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-208458.html\" title=\"冒着生死！偷拍商场让我不淡定的三个美女黑丝\" target=\"_blank\">冒着生死！偷拍商场让我不淡定的三个美女黑丝&nbsp;</a></p><span>6-06</span></li>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-208454.html\" title=\"结婚前晚强奸卖淫女 嫖娼不成便轮奸潜逃9年\" target=\"_blank\">结婚前晚强奸卖淫女 嫖娼不成便轮奸潜逃9年&nbsp;</a></p><span>6-06</span></li>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-208442.html\" title=\"中国雷霆大怒！普京出卖中国 揭开中国4大机密\" target=\"_blank\">中国雷霆大怒！普京出卖中国 揭开中国4大机密&nbsp;</a></p><span>6-06</span></li>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-208441.html\" title=\"老公逼我模仿A片中的小姐 给他尝鲜\" target=\"_blank\">老公逼我模仿A片中的小姐 给他尝鲜&nbsp;</a></p><span>6-06</span></li>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-208428.html\" title=\"北大校花袁佳怡男友为富二代 亲密私生活照被揭\" target=\"_blank\">北大校花袁佳怡男友为富二代 亲密私生活照被揭&nbsp;</a></p><span>6-06</span></li>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-207727.html\" title=\"汽修店老板两天飞车抢夺8起 自称因没钱发工资\" target=\"_blank\">汽修店老板两天飞车抢夺8起 自称因没钱发工资&nbsp;</a></p><span>6-06</span></li>"
    html +="<li><p>·<a href=\"http://www.y3600.com/viewnews-207725.html\" title=\"鱼塘疑遭下毒致上万斤鱼一夜间死光\" target=\"_blank\">鱼塘疑遭下毒致上万斤鱼一夜间死光&nbsp;</a></p><span>6-06</span></li>"
    html +="</ul>"
    html +="</div>"
    html +="<div class=\"fm_footer\"><i class=\"l\"></i><i class=\"r\"></i></div>"
    html +="</div>"
    html +="<div class=\"nmr hdtj\">"
    html +="<div class=\"fm\">"
    html +="<b>博客</b>"
    html +="<a href=\"http://club.sportscn.com/space.php?do=blog&view=all&orderby=dateline\" target=\"_blank\" class=\"more\">更多>></a>"
    html +="<i class=\"l\"></i><i class=\"r\"></i><dl></dl>"
    html +="</div>"
    html +="<div class=\"fm_b2\"><ul class=\"a\">"
    html +="<i><a href=\"http://www.y3600.com/viewnews-207724.html\" target=\"_blank\" title=\"驾校男教练深夜载5名女学员醉驾撞围墙被拘\"><img src=\"http://img.sportscn.com/crop?w=110&h=110&q=http://club.sportscn.com/attachment/201306/3/221012_1370229565hnyp.jpg\" ></a></i>                <p><a href=\"http://www.y3600.com/viewnews-207724.html\" title=\"驾校男教练深夜载5名女学员醉驾撞围墙被拘\" target=\"_blank\">驾校男教练深夜载5名女学员醉驾撞围墙被拘</a> </p>"
    html +="</ul>"
    html +="<ul class=\"b\"><li>· <a href=\"http://www.y3600.com/viewnews-207722.html\" target=\"_blank\" title=\"单位给员工发40个避孕套当端午节福利\">单位给员工发40个避孕套当端午节福利</a></li>"
    html +="<li>· <a href=\"http://www.y3600.com/viewnews-207723.html\" target=\"_blank\" title=\"男子为买彩票4年诈骗近20万元\">男子为买彩票4年诈骗近20万元</a></li>"
    html +="</ul>"
    html +="<div class=\"CleanBoth\"></div>"
    html +="</div>"
    html +="<div class=\"fm_footer\"><i class=\"l\"></i><i class=\"r\"></i></div>"
    html +="</div>"
    html +="</div>"
    html +="</div>"
    html +="<div class=\"CleanBoth\"></div>"
    html +="<div class=\"B9 gcopyright\">"
    html +="<ul>"
    html +="<a href=\"http://www.sportscn.com/aboutus/\" target=\"_blank\">关于华体</a>"
    html +="<a href=\"http://www.sportscn.com/aboutus/ad.html\" target=\"_blank\">广告服务</a>"
    html +="<a href=\"http://www.sportscn.com/aboutus/job.html\" target=\"_blank\">招聘信息</a>"
    html +="<a href=\"http://www.sportscn.com/aboutus/legal.html\" target=\"_blank\">法律声明</a>"
    html +="<a href=\"http://www.sportscn.com/aboutus/contact.html\" target=\"_blank\">联系我们</a>"
    html +="<a href=\"http://www.sportslink.com.cn/\"  target=\"_blank\" class=\"r\">体育网址大全</a>"
    html +="</ul>"
    html +="<dl>"
    html +="&copy;2000-<script>var date=new Date();document.write(date.getFullYear());</script> <a href=\"http://www.sportscn.com\">华体网</a> 版权所有 <a href=\"http://www.sportscn.com/aboutus/aboutus4.htm\" target=\"_blank\">文网文[2005]016号</a> 沪ICP备10022738号"
    html +="</dl>"
    html +="</div>"
    html +="</body>"
    html +="</html>"
    return html
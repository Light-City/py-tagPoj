# 标签使用
## 1.标签的使用
```python
语法：{% tags %}
```
>urls.py

```python
from django.contrib import admin
from django.conf.urls import url
from tagP import views
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'index/', views.query),
]
```
>views.py

```python
def query(request):
    l=["存","正","参"]
    l=[]
    d={'name':'见','age':12,'sex':'M'}
    return render(request,'index.html',locals())
```
>index.html

```html
<h1>hello {{ l.1 }}</h1>
<h1>hello {{ l.2 }}</h1>
<h1>hello {{ d.name }}</h1>
<h1>hello {{ d.age }}</h1>
<h1>hello {{ d.sex }}</h1>
<hr/>
{% if d.age < 20 %}
    <h1>{{ d.name }}的年龄小于20</h1>
{% elif d.age > 20 %}
    <h1>{{ d.name }}的年龄大于20</h1>
{% else %}
    <h1>{{ d.name }}的年龄不符合要求</h1>
{% endif %}
<hr/>
{% for name in l %}
    <!--forloop.counter从1开始-->
    <h1>{{ forloop.counter }}:{{ name }}</h1>
    <!--forloop.counter从0开始-->
    <h1>{{ forloop.counter0 }}:{{ name }}</h1>
    <!--forloop.counter从倒序-->
    <h1>{{ forloop.revcounter }}:{{ name }}</h1>
    <h1>{{ forloop.revcounter0 }}:{{ name }}</h1>
{% endfor %}
<!--对第一个元素添加first样式(变红)-->
{% for name in l %}
    {% if forloop.first %}
        <li class="first">
    {% else %}
        <li>
    {% endif %}
    {{ name }}
    </li>
    <!--当l为空列表时，就会显示没有相关文章-->
{% empty %}
    <h1>没有相关文章</h1>

```

>其他

```python

除此之外，还有变量名替换
----{% with %}:用更简单的变量名替代复杂的变量名-----
{% with total=fasdsadasda% %} {{ total}} {% endwith %}
----{% verbatim %}:禁止render-----
{% verbatim %}
	{{ hello }}
{% endverbatim %}
此时渲染出来就是{{hello}}
----{% load %}:加载标签库-----
```
## 2.自定义filter和simple_tag
>自定义filter和simple_tag

```python
a、在app中创建templatetags模块(必须的)
b、创建任意 .py 文件，如：myTag.py
c、在使用自定义simple_tag和filter的html文件中导入之前创建的 myTag.py ：{% load myTag %}
d、使用simple_tag和filter
e、在settings中的INSTALLED_APPS配置当前app，不然django无法找到自定义的simple_tag.
```
>myTag.py

```python

# 自定义过滤器/标签
from django import template
from django.utils.safestring import mark_safe

register=template.Library() # register名字固定
# 自定义过滤器
@register.filter
def filter_multi(x,y):
    print(x,y) # 12 3   d.age|filter_multi:3  x,y分别对应d.age与filter_multi
    return x*y

# 自定义标签
@register.simple_tag
def simple_tag_multi(x,y,z,p):

    return x*y*z*p
```
>index.html

```html
{% load myTag %} <!--加载自定义filter-->
<!DOCTYPE html>
......
......
......
<!--使用url中别名-->
<form action="{% url 'login' %}" method="post">
    <p>姓名<input type="text" name="user"></p>
    <p>密码<input type="password" name="pwd"></p>
    <p><input type="submit" value="提交"></p>
    {% csrf_token %}
</form>
<!--以下为自定义filter-->
<p>{{ d.age }}</p>
<p>{{ d.age|filter_multi:3 }}</p> <!--自定义filter d.age*3-->
<p>{% simple_tag_multi d.age 5 6 7 %}</p> <!--自定义tag d.age*5*6*7-->
<!--filter与tag都是实现自定义template，而前者传一个值，后者可传多个值,tag不能用在控制语句中，即控制语句中必须只能用filter-->
```



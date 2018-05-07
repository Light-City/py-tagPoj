# 标签使用

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

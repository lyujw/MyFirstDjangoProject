<<<<<<< HEAD
# MyFirstDjangoProject
=======
# 使用Django实现餐馆的添加功能

### 1.所使用的环境、框架版本、工具    
___
    *运行环境    
        *python 3.7.4
        *MySQL 5.5.40
    
    *框架版本
        *Django === 3.1.0
        *pymysql === 0.10.0
        
    *工具版本
        *PyCharm Professional v2019.3.3
        *SQLyog Professional v12.09
        *Google Chrome v84.0.4147.105

### 2.安装环境
___
1.首先需要安装3.5版本以上的python环境

2.在cmd命令行中输入`pip install Django`，回车之后便可安装好Django环境

3.在cmd命令行中输入`pip install pymysql`,此模块用于操作MySQL数据库


### 3.创建项目
___
1.安装好Django后，可以使用进入一个文件夹，使用Django自带的方法进行创建项目，
在cmd中输入`django-admin startproject DjangoTemplate`,DjangoTemplate为我们项目名字

2.如果使用的是PyCharm的专业版，可以直接在PyCharm中创建Django程序，社区版不具备此功能


### 4.修改项目设置
___
创建好的Django项目文件的目录应该是这样的
```text
DjangoTemplate
--DjangoTemplate
    --__init__.py
    --asgi.py
    --settings.py
    --urls.py
    --wsgi.py
--templates
--manage.py
```


1.打开`settings.py`文件，将`TEMPLATES`的路径修改为`'DIRS': [os.path.join(BASE_DIR, 'templates')]`,
若使用PyCharm专业版创建的项目，则默认已经修改好。

2.将`settings.py`中`MIDDLEWARE`下面的`'django.middleware.csrf.CsrfViewMiddleware',`此行注释掉。

3.在`settings.py`的最后添加`STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)`，然后可以在项目下创建名为`static`的文件夹，用于存放css、图片等静态文件。

### 5.创建数据库
___
使用SQLyog图形化管理数据库

创建名为`restaurant`的数据库

创建表
```sql
CREATE TABLE Restaurant( 
    id INT PRIMARY KEY AUTO_INCREMENT,
    res_name CHAR(20) NOT NULL, 
    address CHAR(20) NOT NULL, 
    res_type CHAR(20) NOT NULL 
)CHARSET utf8;<br>
```



随便设置两条信息<br>
![1.png](http://a1.qpic.cn/psc?/V14eztM52Fok8u/bqQfVz5yrrGYSXMvKr.cqeOeVoIU29lSsPxGs4ipU6NENBnyiGKzsmOdSsX.V7UD1b2bIAPD.2tPYS6r9IPBT3zCuOU0jC5nXkQ9d3K*33M!/b&ek=1&kp=1&pt=0&bo=fQFEAH0BRAADEDU!&tl=1&vuin=879409261&tm=1597075200&sce=60-1-1&rf=viewer_311)

### 6.实现功能
___
1.在`urls.py`文件中，添加以下两条：

```python
url(r'^restaurant_info/', views.restaurant_info),
url(r'^add_restaurant/', views.add_restaurant),
```


2.在`app`文件夹下面创建`views.py`文件，并导入`render, redirect,pymysql`等模块

3.创建两个函数：
```python
def restaurant_info(request):
def add_restaurant(request):
```

4.使用`pymysql`连接至数据库，并执行返回相应的数据：

```python
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='djangotemplate', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("SELECT id,res_name,address,res_type from restaurant")
restaurant_list = cursor.fetchall()
cursor.close()
conn.close()
```

5.在`templates`文件夹中创建html文件，在`restaurant_info`函数中调用`render`方法
```python
return render(request, 'restaurant_info.html', {'restaurant_list': restaurant_list})
```

6.`add_restaurant`函数同理，需要接收POST返回的数据，并插入数据库中：
```python
def add_restaurant(request):
    if request.method == "GET":
        return render(request, 'add_restaurant.html')
    else:
        print(request.POST)
        v1 = request.POST.get('name')
        v2 = request.POST.get('address')
        v3 = request.POST.get('type')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='djangotemplate',
                               charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO restaurant(res_name,address,res_type) values(%s,%s,%s)", [v1, v2, v3, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/restaurant_info/')
```

7.根据`add_restaurant`中input标签的name属性接收用户的输入：
```python
v1 = request.POST.get('name')
v2 = request.POST.get('address')
v3 = request.POST.get('type')
```


8.在`restaurant.html`中使用循环，将后端在数据库中查询到的数据显示出来：
```html
{% for row in restaurant_list %}
    <tr>
        <td>{{ row.id }}</td>
        <td>{{ row.res_name }}</td>
        <td>{{ row.address }}</td>
        <td>{{ row.res_type }}</td>
     </tr>
{% endfor %}
```


### 7.运行程序
___
在项目文件夹下执行命令`python manage.py runserver`或者直接使用PyCharm运行程序

在浏览器中输入`127.0.0.1：8000/restaurant_info`即可进入


### 8.效果演示
___
##### 进入`127.0.0.1：8000/restaurant_info`后即可看见数据库中的两条信息
![2.png](http://a1.qpic.cn/psc?/V14eztM52Fok8u/bqQfVz5yrrGYSXMvKr.cqZ0ZJfYfi6JryXqKoo9jMvnVWmUfwqfv5O1QA.kJlTlpcyFvjt.TnrHu5t.m4vsDFUmvb1T9ZkiAW.t1eZcq8nU!/b&ek=1&kp=1&pt=0&bo=ZwJ4AWcCeAEDEDU!&tl=1&vuin=879409261&tm=1597075200&sce=60-4-3&rf=viewer_311)
##### 点击`添加餐馆`按钮,自动进入`127.0.0.1：8000/add_restaurant`，在三个框中填写信息
![3.png](http://a1.qpic.cn/psc?/V14eztM52Fok8u/bqQfVz5yrrGYSXMvKr.cqZ*NqiZVRPkNFr2TjFSb8hey3zdEk6oJhJOIkJTRNO84Rqv.goj5l*O*fhDh8pQyC.EAeT3S4nOn6lrNYBdOlK0!/b&ek=1&kp=1&pt=0&bo=PQKgAT0CoAEDEDU!&tl=1&vuin=879409261&tm=1597075200&sce=50-1-1&rf=viewer_311)
##### 点击`提交`按钮，自动回到`127.0.0.1：8000/restaurant_info`地址，并显示新的数据
![4.png](http://a1.qpic.cn/psc?/V14eztM52Fok8u/bqQfVz5yrrGYSXMvKr.cqU2VOyDxrFL9TRnwj3imW6jwbJxhqCZwtzdkZ.yh8MBmzmlfKQu.*iUzNM*JGqMDY.Qvjvc0YOkzZQ3MSiZIsxE!/b&ek=1&kp=1&pt=0&bo=NwJwATcCcAEDEDU!&tl=1&vuin=879409261&tm=1597075200&sce=50-1-1&rf=viewer_311)


## License
___
Copyright (c) Jiawei_Lyu. All rights reserved.

Licensed under the [MIT](https://www.mit-license.org/) license.
>>>>>>> 0276952... first commit

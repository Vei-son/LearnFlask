from flask import Flask, render_template
# 从flask包导入Flask类，然后实例化这个类，创建一个程序对象app
app = Flask(__name__)

# “注册”一个处理函数，这个函数是处理某个请求的处理函数，Flask官方把它叫做视图函数，可以理解为“请求处理函数”
# 给这个函数一个装饰器帽子，使用app.route()装饰器来为这个函数绑定对应的URL
# 当用户在浏览器访问这个URL的时候，就会出发这个函数，获取返回值，并把返回值显示到浏览器窗口
@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

# 定义虚拟数据
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
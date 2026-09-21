<https://xn--ygr25xpohxwz.com/>

# 终端命令
cd/ls/mkdir/pwd/rm/rmdir......
cat : 读取文件文本
rmdir : 删除空目录，要先把里边的隐藏文件删掉(如mac的.DS_Store)

mac: shift + command + . 显示隐藏文件
ls -la

ls -Force 作用是列出当前目录下的所有文件和文件夹，包括隐藏项，相当于 Linux 里的 ls -a (ls -la)，
-Force‌：强制显示隐藏文件和系统文件，不加它默认会隐藏这些

方向键 ↑、↓ ：查找曾执行过的命令
tab ： 自动补全名称

mac / linux
open ： 用合适的工具去打开

windows 
start ：用合适的工具去打开

## 创建文件
touch first_json.py(linux)
ni first_json.py(windows)

---

# 前端

windows中不自带vim
vim : 
1. i(insert)
2. 可用ctrl(command) + v
3. ESC退出编辑模式
4. 输入 shift + :
5. wq() (write quit)退出并保存
6. q! 强制退出
7. :x 条件写入(没试过)

IP地址 :
~

域名 ：
给机器地址(ipv4,ipv6)起一个方便人记忆和输入的名字
类比人和手机号（一个域名多个ip、且ip可换）

DNS :
全球标准(Domain Name System)
维护域名和ip之间的关系
(连接 域名 和 IP地址 )
上传到DNS

端口 ：
http : 普通访问 默认 80 
https : 加密访问 默认 443 

: + 数字访问端口(:443)
<https://xn--ygr25xpohxwz.com:443>

URL :
域名 + 资源路径(/zero-to-fullstack/)
<https://xn--ygr25xpohxwz.com/zero-to-fullstack/>

输入网址访问网页但访问不到 ：
1. URL输入错误
2. dns服务器无法解析
3. 域名被重定向了
4. 域名下是否有IP地址
5. 服务器无法访问
6. 根本没有这个网页
7. 端口号问题
8. 资源路径是否错误

---

# 后端

## 对windows

## 创建虚拟环境（文件中）： 
python3 -m venv --prompt=project_1 .venv

## 使用虚拟环境，先关闭conda
conda config --set auto_activate_base false (24.9之前)
conda config --set auto_activate false (24.9以后)

## 切换为虚拟环境：
PS C:\Users\Administrator\Desktop\project_1\backend> 路径下，
.\.venv\Scripts\Activate.ps1
其中， .\ 是powershell的执行命令

## .venv 文件夹不可随意移动或重命名，会发生许多问题（路径问题，如pip失效）

## python依赖 requirements.txt
### 生成 
pip freeze >  requirements.txt
### 别人 / 服务器上调用
pip install -r requirements.txt

# API

## 返回api/网站 全部内容
cmd : curl -v URL
powershell : curl.exe -v URL

---
### main.py 改成了 ——>handmade.py

实践层面必写Content-Type
通过：
self.send_header("Content-Type", "text/html; charset=utf-8") # text/plain

响应头不是内容本身，而是“关于内容的说明”——application/json 同理：它让调用方知道该按 JSON 解析响应体。

所以也可以说，在浏览器眼里，“网页”和“API 数据”并没有本质区别——都是一段 HTTP 响应，
差别只在 Content-Type，text/html 就当网页渲染，application/json 就当数据处理。
所谓“做 API”，从 HTTP 的角度看，不过是选择返回 JSON 而不是返回 HTML。

---
f12，复制cURL

## python常用后端框架
Flask、Django、FastAPI

## FastAPI
FastAPI 负责“接口该做什么”，uvicorn 负责“让接口跑起来”。FastAPI 自己不会守着端口等请求；uvicorn 收到请求后，会把它交给 FastAPI 处理。

### main.py用uvicorn启动
手动 ：  
`uvicorn main:app --reload`
or
`fastapi dev`

main:app拆开看：
`main` - 文件(main.py 的名字)
`app` - 变量(app = FastAPI() 的app)
`--reload` - 若改了代码，可以自动重启（热更新）


若终端提示包不存在(fastapi)，
尝试`hash -r` - 清空 Shell 的命令路径缓存‌，让系统重新按 $PATH 查找命令

---
`__pycache__`下面的`pyc`文件 - python运行代码时 自动生成的缓存
让python下一次加载代码时 可以快一点
不是源码，是构建产物
删了也无所谓，再运行时自动生成
所以在`.gitignore`中忽略该文件夹内容

### api文档
Documentation at http://xxURL/docs
自动生成，可用来测试

### api-post
`from pydantic import BaseModel`， 数据校验
`class AnalyzeRequest(BaseModel): `按照class定义的要求做校验
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `值 : 类型(text : str)`
@app.post("/api/analyze") 
def analyze(req: AnalyzeRequest):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return {

}

#### mac : 
curl http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "今天的风很轻，适合把想法写下来"}'
#### windows: ？？？？？（理论上不太用纠结该部分，反正也不用curl调用）
因为引号转义的问题，不可以在终端(cmd,powershell)运行
存成文件执行：
powershell(.ps1)不可以，
CMD(.bat)部分可以

将

curl -i -X POST http://localhost:8000/api/analyze ^
-H "Content-Type: application/json" ^
-d "{\"text\": \"今天的风很轻，适合把想法写下来\"}"

存成.bat文件并执行
-X POST 可有可无
`其依然有问题，中文编码会有错误概率(如working_test.bat 中的  "字段写错了")`

#### 状态代码
422，请求已经收到，格式也可以理解，但内容不符合接口的要求
{"detail":[{"type":"missing","loc":["body","text"],"msg":"Field required","input":{"txt":"字段，写错了"}}]}

500 Internal Server Error 服务器内部错误，出现于api写错的时候

4开头，请求方的错；5开头，服务方的错

traceback 错误回溯，先看最后一行；再往上翻，找报错中自己写的文件（非安装依赖里的文件）
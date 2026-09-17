<https://xn--ygr25xpohxwz.com/>

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

---

ls -Force 作用是列出当前目录下的所有文件和文件夹，包括隐藏项，相当于 Linux 里的 ls -a，
-Force‌：强制显示隐藏文件和系统文件，不加它默认会隐藏这些

## 创建文件
touch first_json.py(linux)
ni first_json.py(windows)

## python依赖 requirements.txt
### 生成 
pip freeze >  requirements.txt
### 别人 / 服务器上调用
pip install -r requirements.txt

## 返回api/网站 全部内容
cmd : curl -v URL
powershell : curl.exe -v URL

---
### main.py

实践层面必写Content-Type
通过：
self.send_header("Content-Type", "text/html; charset=utf-8") # text/plain

响应头不是内容本身，而是“关于内容的说明”——application/json 同理：它让调用方知道该按 JSON 解析响应体。

所以也可以说，在浏览器眼里，“网页”和“API 数据”并没有本质区别——都是一段 HTTP 响应，
差别只在 Content-Type，text/html 就当网页渲染，application/json 就当数据处理。
所谓“做 API”，从 HTTP 的角度看，不过是选择返回 JSON 而不是返回 HTML。

---
f12，复制cURL
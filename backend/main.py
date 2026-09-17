from fastapi import FastAPI
from pydantic import BaseModel # Pydantic，专门管理数据的解析和校验；BaseModel，声明某个类型的数据长什么样

app = FastAPI()

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

class AnalyzeRequest(BaseModel):
    # AnalyzeRequest的要求，按照下面的要求做校验
    # 请求体校验不通过，请求方 会被打回
    text: str # 要求提供一个叫做 text 的值，且这个值是 字符串 类型


# fastapi部分：

# 遇到不认识的路径，自动返回404
@app.get("/api/profile") # 装饰器，向路径发的get请求，交给下面的函数处理
def get_profile():
    return profile

@app.post("/api/analyze") # 请求该地址是post请求，交给下面的函数处理
def analyze(req: AnalyzeRequest): # 需要提供request(req)请求体，这个请求体的要求 ： 必须符合 AnalyzeRequest 的要求
    return {
        "text": req.text,
        "score": 0.5,
        "label": "偏平静",
        "pinyin": "（模块 6 再说）",
    }


# 用uvicorn启动
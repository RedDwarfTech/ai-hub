# ai-hub

启动server

```shell
# 安装依赖
pip3 install fastapi
pip3 install uvicorn
pip3 install -r requirements.txt
# 如果安装psycopg2失败直接安装psycopg2-binary，不需要外部依赖
/opt/homebrew/opt/python@3.10/bin/pip3.10 install psycopg2-binary
# 指定特定版本的pip
/opt/homebrew/opt/python@3.10/bin/pip3.10 install -r requirements.txt
# 启动server
/usr/local/bin/python3.10 -m uvicorn main:app --reload --port 9002
```

部署：

```shell
rsync -avzPh /Users/xiaoqiangjiang/source/reddwarf/backend/chat-server vps:/opt/apps/chat/
```


### 依赖管理

```shell
# 生成requirement.txt
pip3 freeze > requirement.txt
# 安装依赖
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# 使用镜像地址快速下载
pip3 install --upgrade opencv-python -i https://mirrors.aliyun.com/pypi/simple/
# 查看是否安装了对应的模块
pip3 list|grep "name"
```

### 本机构建镜像


```bash
docker build -f ./Dockerfile -t=reddwarf-pro/cha-server:v1.0.0 .
```

macOS 13.2的~/.docker/daemon.json文件中配置Docker拉取的镜像地址：

```
{
  "builder": {
    "gc": {
      "defaultKeepStorage": "20GB",
      "enabled": true
    }
  },
  "experimental": false,
  "features": {
    "buildkit": true
  },
  "registry-mirrors": [
    "https://xxxx.mirror.aliyuncs.com"
  ]
}
```





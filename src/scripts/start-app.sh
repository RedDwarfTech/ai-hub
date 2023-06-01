#!/usr/bin/env bash

# 当使用未初始化的变量时，程序自动退出
# 也可以使用命令 set -o nounset
set -u

# 当任何一行命令执行失败时，自动退出脚本
# 也可以使用命令 set -o errexit
set -e

set -x

cd /opt/apps/chat/chat-server && nohup python3.10 -m uvicorn main:app --port 8001 --host 0.0.0.0 --reload &!

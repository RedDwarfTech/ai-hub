#!/usr/bin/env bash

set -u

set -e

set -x

ps auxww | grep "--port 8001" | grep -v "grep"  | awk '{print $2}' | xargs -r kill -9

pip3 install -r requirements.txt

nohup /usr/bin/python3.10 -m uvicorn main:app --reload --port 8001 --host 0.0.0.0 >> /opt/apps/chat/ai-hub/ai-hub.log &!




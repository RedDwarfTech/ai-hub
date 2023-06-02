#!/usr/bin/env bash

set -u

set -e

set -x

rsync -avzPh /Users/xiaoqiangjiang/source/reddwarf/backend/ai-hub vps:/opt/apps/chat/

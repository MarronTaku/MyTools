FROM jupyter/datascience-notebook:ubuntu-22.04

# メタ情報
LABEL maintainer="TAKUMI OKUYA"
LABEL version="1.0"
LABEL description="vscode+docker+jupyter"

# Node.js + npm をインストール
# NOTE: Docker内部で開発しない場合は不要
USER root
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @google/gemini-cli

# rootユーザーに切り替えてsudo権限を付与
USER root
RUN echo "jovyan ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/jovyan
USER jovyan

# 作業ディレクトリを変更
WORKDIR /home/jovyan/work
COPY requirements.txt .
RUN pip install -r requirements.txt --no-deps

# その他必要なパッケージ
USER root
RUN apt-get update && \
    apt-get install -y git graphviz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Gitの設定 (所有権エラーの回避と日本語ファイル名対応)
# NOTE: Dockerコンテナ内で開発しない場合は不要
USER jovyan
ARG GIT_USER_NAME="Your Name"
ARG GIT_USER_EMAIL="you@example.com"

RUN git config --global --add safe.directory "/home/jovyan/work" && \
    git config --global core.quotepath false && \
    git config --global user.name "${GIT_USER_NAME}" && \
    git config --global user.email "${GIT_USER_EMAIL}"
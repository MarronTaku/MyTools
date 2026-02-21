# JupyterNotebook Dockerテンプレート

## 概要

本リポジトリは、JupyterNotebookのDockerテンプレートです。

## 環境構築

コンテナーのビルドと起動は以下のコマンドを実行してください。

```bash
cd jupyterNotebook
docker compose -f .devcontainer/compose.yml build
docker compose -f .devcontainer/compose.yml up -d
```

ビルドとコンテナーを実行

```bash
docker compose -f .devcontainer/compose.yml up -d --build
```

コンテナーの停止

```bash
docker compose -f .devcontainer/compose.yml down
```

# gemini cli

```bash
gcloud auth application-default login
```

# バックグランド実行

- ipynbファイルを開く
- メニューの「Kernel」→「Change kernel」→「Python 3 (ipykernel)」を選択
- サーバーの宛先を「http://localhost:8888」のように入力
- 「jupyter notebook password」を入力
   - jupyter server listコマンドで確認することができる
- 接続完了

## 参考

[ライブラリ バージョン E2026#1](https://www.jdla.org/certificate/engineer/)

[環境構築 jupyter notebook](https://note.com/k_fukunaka/n/nabb5cd028595)
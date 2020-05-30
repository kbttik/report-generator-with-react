# report-generator-with-react
* R/Pythonで生成したhtmlを管理するSPAを作成するコンテナ+app


# コンテナ
* `Docker/Dockerfile`からのbuild
```
docker build -t reporter-react:0.0 -f Docker/Dockerfile .
```

* 作成した`reporter-react:<tag>`で実行
  * `-it`: フォワードで、ターミナル起動
  * `--rm`: コンテナが終了後削除
  * `-v <path>/report-generator-with-react/:/home/repo`: /home/repoにこのレポジトリをマウント
  * `-p 8990:3000`: 端末の8990をコンテナの3000にポートフォワード
```
docker run -it -v <path>/report-generator-with-react/:/home/repo -p 8990:3000 --rm reporter-react:0.0 /bin/bash
```

# react app
* appの起動(デフォルトだと3000)
```
cd html-reporter
npm start
```


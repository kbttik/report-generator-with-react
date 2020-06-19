# report-generator-with-react
* R/Pythonで生成したhtmlを管理するSPAを作成するコンテナ(Docker使用)+app
* Flask or react でPOSTされるhtmlの受け口を作る -> 将来的にはshinyで作りたい
* 雑なメモ: https://hackmd.io/crhgugtYTouUUFKa5qJ7hg

# コンテナ

**この作業は、`report-generator-with-react`での作業**

## react
### build
* `Docker/Dockerfile`からのbuild
```
docker build -t reporter-react:0.0 -f Docker/react/Dockerfile .
```

### run
* 作成した`reporter-react:<tag>`で実行
  * `-it`: フォワードで、ターミナル起動
  * `--rm`: コンテナが終了後削除
  * `-v <path>/report-generator-with-react/:/home/repo`: /home/repoにこのレポジトリをマウント(<path>はgitのフォルダを指定)
  * `-p 8990:3000`: 端末の8990をコンテナの3000にポートフォワード
```
docker run -it -v $PWD:/home/repo -p 8990:3000 --rm reporter-react:0.0 /bin/bash
```
* docker-composeでの実行
```
docker-compose -f Docker/react/docker-compose.yml up -d
```

## nginx
### build
* `Docker/Dockerfile-nginx`からのbuild
```
docker build -t reporter-nginx:0.0 -f Docker/nginx/Dockerfile .
```

### run
* reactでbuildしたフォルダとreportのフォルダを覗かせる
```
docker run --rm -v $PWD/react-reporter/build:/usr/share/nginx/html -v $PWD/report:/mnt/report --name nginx-reporter -p 8991:80 reporter-nginx:0.0
```


## httpd(apache)
* `Docker/Dockerfile-httpd`からのbuild
```
docker build -t reporter-httpd:0.0 -f Docker/httpd/Dockerfile .
```

* reactでbuildしたフォルダとreportのフォルダを覗かせる
  * <path>はgitのフォルダを指定
```
docker run --rm -v <PATH>/report-generator-with-react/react-reporter/build:/usr/share/ -v <PATH>/report-generator-with-react/report:/mnt/report -p 8991:80 reporter-nginx:0.0
```

## MySQL
* レポートのタグを保存する
```
docker run --rm --name reporter-mysql -e MYSQL_ROOT_PASSWORD=mysql -p 8992:3306 -d -it mysql:8.0.20
mysql -u root -p -h localhost -P 8992 --protocol=tcp

create table maps (name varchar(50), url varchar(100));
insert into maps values("test_rmarkdown", "http://localhost:8991/report/test_rmarkdown.html");
```
* docker-composeで行う(成功済み)
```
docker-compose -f Docker/mysql/docker-compose.yml up --build
```
* docker-compose内で以下のように設定したので、mysqlコンテナ内のデータは、/mysql/dataに保存される
```
    volumes: 
      - $PWD/mysql/data:/var/lib/mysql
```
```
(base) ➜  report-generator-with-react git:(master) ✗ tree mysql -d 2  
mysql
├── conf
├── data
│   ├── #innodb_temp
│   ├── mysql
│   ├── performance_schema
│   ├── reporter
│   └── sys
└── init
```



## Flask
* POSTを受け取る > mysqlに必要なデータを保存 + htmlレポート復元
```
docker build -t reporter-flask:0.0 -f Docker/flask/Dockerfile .
```

---

# react app
* appの生成(npx: 最新だとこっちみたい。nodeとnpmのversion upが必要)
  * `npm create-react-app`と比べて、設定ファイルが増えている
  * `public/manifest.json`はホーム画面へ追加する際に、より細かな指定をするための記述
```
npx create-react-app react-reporter
```

* appの起動(デフォルトだと3000)
```
cd react-reporter
npm start
```

* build:静的ページの生成
  * これをapache or nginxで覗かせるかなー
```
npm run build
```

---

# nginxで公開
* 例えば、これでアクセスできる
```
http://localhost:8991/report/test_rmarkdown.html
```


# mysqlに接続
* localhostだと探せない
```
mysql -u root -h 127.0.0.1 -P 8993 -p
```


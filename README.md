# report-generator-with-react
* R/Pythonで生成したhtmlを管理するSPAを作成するコンテナ(Docker使用)+app


# コンテナ

## react
* `Docker/Dockerfile`からのbuild
```
docker build -t reporter-react:0.0 -f Docker/react/Dockerfile .
```

* 作成した`reporter-react:<tag>`で実行
  * `-it`: フォワードで、ターミナル起動
  * `--rm`: コンテナが終了後削除
  * `-v <path>/report-generator-with-react/:/home/repo`: /home/repoにこのレポジトリをマウント(<path>はgitのフォルダを指定)
  * `-p 8990:3000`: 端末の8990をコンテナの3000にポートフォワード
```
docker run -it -v <path>/report-generator-with-react/:/home/repo -p 8990:3000 --rm reporter-react:0.0 /bin/bash
```

## nginx
* `Docker/Dockerfile-nginx`からのbuild
```
docker build -t reporter-nginx:0.0 -f Docker/nginx/Dockerfile .
```

* reactでbuildしたフォルダとreportのフォルダを覗かせる
  * <path>はgitのフォルダを指定
```
docker run --rm -v <PATH>/report-generator-with-react/react-reporter/build:/usr/share/nginx/html -v <PATH>/report-generator-with-react/report:/mnt/report -p 8991:80 reporter-nginx:0.0
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
* 
```
docker run --rm --name reporter-mysql -e MYSQL_ROOT_PASSWORD=mysql -p 8992:3306 -d -it mysql:8.0.20
mysql -u root -p -h localhost -P 8992 --protocol=tcp

create table maps (name varchar(50), url varchar(100));
insert into maps values("test_rmarkdown", "http://localhost:8991/report/test_rmarkdown.html");
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
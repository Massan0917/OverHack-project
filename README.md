# 環境構築

リポジトリのコピー  
```bash
git clone git@github.com:Massan0917/OverHack-project.git
cd OverHack-project
```

docker-composeの起動  
```bash
docker compose up -d 
```

フロントエンドの初期設定:関連パッケージのインストール
```bash
docker compose exec frontend yarn install
```

フロントエンドの初期設定:Vueのプロジェクト作成
```bash
docker compose exec frontend vue create .
```

いろんなことを聞かれるので、以下のように答える
すべて聞かれない場合があるので、質問内容を確認。
```bash
→ Your connection to the default yarn registry seems to be slow.
   Use https://registry.npmmirror.com/ for faster installation? → Yes
→ Generate project in current directory? Yes
→ Please pick a preset Vue3
→ Pick the package manager to use when installing dependencies: Use Yarn 
```

プロジェクトの作成に伴い、HelloWorld.vueが作成されるので、削除する
```bash
git checkout frontend/app/src/components/HelloWorld.vue
```

フロントエンドの起動
```bash
docker compose exec frontend yarn serve
```

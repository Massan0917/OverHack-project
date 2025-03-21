<template>
    <div class="max-w-md mx-auto p-4 text-center">
      <h1 class="text-xl font-bold mb-4">投稿確認画面</h1>
  
      <!-- 画像の表示 -->
      <div class="mb-4">
        <p class="mb-2">こんな感じになりそうです</p>
        <img :src=imagePreview class="mx-auto border p-2 rounded" alt="アップロード画像のプレビュー">
      </div>
  
      <!-- 名前とコメント表示 -->
      <div class="mb-4">
        <p><strong>{{ name }}</strong> さんの投稿</p>
        <p>{{ comment }}</p>
      </div>
  
      <!-- 再度検出するボタン（今はリロードのみ） -->
      <button @click =reloadPage class="border py-2 px-4 rounded mb-2">
        再度検出する
      </button>
  
      <!-- 投稿ボタン（次の画面へ遷移） -->
      <button @click="submitPost" class="bg-blue-500 text-white py-2 px-4 rounded block mx-auto mb-2">
        投稿！
      </button>
  
      <!-- 画像を選び直すボタン -->
      <button @click="reselectImage" class="border py-2 px-4 rounded">
        画像を選び直す
      </button>
    </div>
  </template>
  
  <script>
  const axios = require("axios");

  export default {
    data() {
      return {
        imagePreview: '',
        name: '',
        comment: '',
        boudingBoxes: [],
        imagePath: '',
      };
    },
    created() {
      const postData = JSON.parse(localStorage.getItem('postData'));
      if (postData) {
        this.imagePreview = postData.image;
        this.imagePath = postData.imagePath;
        this.name = postData.name;
        this.comment = postData.comment;

        this.recognizeFace();
      } else {
        this.$router.push('/');
      }
    },
    methods: {
      reloadPage() {
        window.location.reload();
      },

      // 顔認識処理
      recognizeFace() {
        const self = this;

        axios.get(
          'http://localhost:3000/api/face-detect?image_path=' + self.imagePath,
        ).then( function( response ){
          console.log( response );
          if( response.data.bouding_boxes ){
            self.boudingBoxes = response.data.bouding_boxes;
          } else {
            self.boudingBoxes = [];
          }
        } ).catch( function( error ){
          console.log( error );
        } );
      },

      // 投稿処理
      submitPost() {
        const self = this;

        const payload = {
          name: self.name,
          comment: self.comment,
          image_path: self.imagePath,
          bounding_boxes: self.boudingBoxes,
        }

        console.log( payload );

        axios.post(
          'http://localhost:3000/api/upload',
          payload
        ).then( function( response ){
          console.log( response );
          localStorage.removeItem('postData');
					self.$router.push('/complete');
				} ).catch( function( error ){
          console.log( error );
        } );
      },
      reselectImage() {
        this.$router.push('/');
      }
    }
  };
  </script>
  
  <style scoped>
  /* Tailwind CSS利用前提、追加スタイルは任意で */
  img {
    max-width: 100%;
    height: auto;
  }
  </style>
  
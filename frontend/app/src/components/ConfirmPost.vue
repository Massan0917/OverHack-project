<template>
  <BackgroundWrapper>
    <ContentWrapper>
      <h1 class="text-xl font-bold text-red-700 mb-4">投稿確認画面</h1>

      <!-- 画像の表示 -->
      <div class="mb-4">
        <img :src=imagePreview class="mx-auto border-red-300 p-2 rounded" alt="アップロード画像のプレビュー">
      </div>

      <!-- 名前とコメント表示 -->
      <div class="mb-4">
        <div class="border-2 border-orange-400 p-3 rounded-lg text-center mb-4">
          <p class="text-lg font-bold text-red-700">{{ name }}</p>
          <p class="text-sm text-gray-700">さんの投稿</p>
        </div>
        <div class="border-2 border-orange-400 p-3 rounded-lg text-center">
          <p class="text-lg text-gray-800">{{ comment }}</p>
        </div>
      </div>

      <div class="flex justify-center gap-2 mt-6">
        <!-- 再度検出するボタン（今はリロードのみ） -->
        <button @click="reloadPage" class="bg-red-500 text-white font-semibold py-3 px-6 rounded-lg transition duration-300 flex-1">
          再検出
        </button>

        <!-- 投稿ボタン（次の画面へ遷移） -->
        <button @click="submitPost" class="bg-red-500 text-white font-semibold py-3 px-6 rounded-lg transition duration-300 flex-1 mx-2">
          投稿！
        </button>

        <!-- 画像を選び直すボタン -->
        <button @click="reselectImage" class="bg-red-500 text-white font-semibold py-2 px-4 rounded-lg transition duration-300 flex-1">
          やり直す
        </button>
      </div>
    </ContentWrapper>
  </BackgroundWrapper>
</template>

<script>
import BackgroundWrapper from './BackgroundWrapper.vue';
import ContentWrapper from './ContentWrapper.vue';
const axios = require("axios");

export default {
  components: {
    BackgroundWrapper,
    ContentWrapper
  },
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
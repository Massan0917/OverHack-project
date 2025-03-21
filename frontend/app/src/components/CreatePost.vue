<template>
  <BackgroundWrapper>
    <ContentWrapper>
      <!-- 画像アップロード -->
      <div class="mb-6">
        <label class="block text-orange-600 font-semibold mb-2">画像アップロード</label>
        <input type="file" ref="file" @change="onFileChange" accept="image/*" class="border border-orange-300 w-full p-3 rounded-lg bg-white">

        <!-- 画像プレビュー（選択後に表示） -->
        <div v-if="imagePreview" class="mt-4 text-center">
          <p class="text-orange-600 mb-2">選択した画像:</p>
          <img :src="imagePreview" class="max-w-full h-auto rounded-lg shadow-md">
          <!-- 画像削除ボタン -->
          <button @click="removeImage" class="mt-2 bg-red-500 hover:bg-orange-600 text-white font-semibold py-2 px-4 rounded-lg transition duration-300">
            画像を削除
          </button>
        </div>
      </div>

      <!-- 名前入力 -->
      <div class="mb-6">
        <label class="block text-orange-600 font-semibold mb-2">あなたの名前</label>
        <input v-model="name" type="text" class="border border-orange-300 w-full p-3 rounded-lg bg-white" placeholder="名前を入力してください">
      </div>

      <!-- コメント入力 -->
      <div class="mb-6">
        <label class="block text-orange-600 font-semibold mb-2">投稿へのコメント</label>
        <textarea v-model="comment" rows="4" class="border border-orange-300 w-full p-3 rounded-lg bg-white" placeholder="コメントを入力してください"></textarea>
      </div>

      <!-- 投稿確認ボタン -->
      <button @click="submitPost" class="bg-red-500 hover:bg-orange-600 text-white font-semibold py-3 px-6 rounded-lg w-full transition duration-300">
        投稿！
      </button>
    </ContentWrapper>
  </BackgroundWrapper>
</template>

<script>
import BackgroundWrapper from './BackgroundWrapper.vue';
import ContentWrapper from './ContentWrapper.vue';
const axios = require("axios");

export default {
  components: {
    BackgroundWrapper, // コンポーネントとして登録
    ContentWrapper
  },
  data() {
    return {
      image: null,
      imagePreview: null, // 画像のプレビューURL
      name: '',
      comment: '',
    };
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.image = file;

        // 画像のプレビューを生成
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
          this.imagePreview = reader.result;
        };
      }
    },
    removeImage() {
      this.image = null;
      this.imagePreview = null;
      this.$refs.file.value = '';
    },

    // 投稿確認画面へ遷移
    submitPost() {
      const self = this;

      if (!self.image || !self.name || !self.comment) {
        alert('全ての項目を入力してください');
        return;
      }
      // localStorageにデータを一時保存（画像はBase64に変換）
      const reader = new FileReader();
      reader.onload = () => {
        const formData = new FormData();
        formData.append('image', self.image);

        // 画像をアップロード
        axios.post( "http://localhost:3000/api/image", formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }).then( function ( response ) {
          // 画像アップロード後
          // 投稿データをlocalStorageに保存
          const postData = {
            image: reader.result,
            name: self.name,
            comment: self.comment,
            imagePath: response.data.image_path,
          };
          localStorage.setItem('postData', JSON.stringify(postData));

          self.$router.push({ name: 'PostConfirm' });
        }).catch( function ( error ) {
          console.log(error);
        });
      };
      reader.readAsDataURL(self.image);
    },
  }
};
</script>

<style scoped>
body {
  background-color: #f0f8ff;
}

button {
  cursor: pointer;
}
</style>
<template>
  <div class="max-w-md mx-auto p-4">
    <h1 class="text-xl font-bold mb-4">投稿入力画面</h1>

    <!-- 画像アップロード -->
    <div class="mb-4">
      <label class="block mb-2">画像アップロード</label>
      <input type="file" @change="onFileChange" accept="image/*" class="border w-full p-2">
    </div>

    <!-- 名前入力 -->
    <div class="mb-4">
      <label class="block mb-2">あなたの名前</label>
      <input v-model="name" type="text" class="border w-full p-2" placeholder="名前を入力してください">
    </div>

    <!-- コメント入力 -->
    <div class="mb-4">
      <label class="block mb-2">投稿へのコメント</label>
      <textarea v-model="comment" rows="4" class="border w-full p-2" placeholder="コメントを入力してください"></textarea>
    </div>

    <!-- 投稿確認ボタン -->
    <button @click="submitPost" class="bg-blue-500 text-white py-2 px-4 rounded">
      投稿！
    </button>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  data() {
    return {
      image: null,
      name: '',
      comment: '',
    };
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.image = file;
      }
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
/* Tailwind CSS を使っている前提で記述しています（もしなければ適宜CSS調整） */
</style>


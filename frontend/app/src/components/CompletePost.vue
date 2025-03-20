<template>
    <div class="max-w-md mx-auto p-4 text-center">
      <h1 class="text-xl font-bold mb-4">投稿されました！</h1>
  
      <p class="mb-6">画面に反映されているか見てみよう！</p>
  
      <!-- インスタ投稿画面への遷移（仮リンク） -->
      <a href="https://www.instagram.com/" target="_blank" class="inline-block mb-6">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg"
          alt="Instagramへのリンク"
          class="mx-auto w-16 h-16"
        >
      </a>
  
      <!-- 最初の画面に戻るボタン -->
      <button @click="goToTop" class="border py-2 px-4 rounded">
        最初の画面に戻る
      </button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goToTop() {
        this.$router.push('/');
      }
    }
  };
  </script>
  
  <style scoped>
  /* 必要に応じて追加スタイルを記述 */
  </style>
  
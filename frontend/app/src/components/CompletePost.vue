<template>
  <BackgroundWrapper>
    <ContentWrapper>
      <div class="max-w-md mx-auto p-4 text-center">
        <h1 class="text-xl font-bold mb-4">投稿されました！</h1>
  
        <p class="mb-6">画面に反映されているか見てみよう！</p>
  
        <!-- インスタ投稿画面への遷移（仮リンク） -->
        <a href="https://www.instagram.com/" target="_blank" class="flex justify-center mb-6">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg"
            alt="Instagramへのリンク"
            class="w-20 h-20"
          >
        </a>
  
        <!-- 最初の画面に戻るボタン -->
        <button @click="goToTop" class="bg-red-500 text-white font-semibold py-3 px-6 rounded-lg w-full transition duration-300">
          最初の画面に戻る
        </button>
      </div>
    </ContentWrapper>
  </BackgroundWrapper>
</template>

<script>
import BackgroundWrapper from './BackgroundWrapper.vue';
import ContentWrapper from './ContentWrapper.vue';

export default {
  components: {
    BackgroundWrapper,
    ContentWrapper
  },
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
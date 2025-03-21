<template>
    <div class="relative min-h-screen flex items-center justify-center">
      <!-- 背景オーバーレイ -->
      <div class="absolute inset-0 bg-[url('/images/masquarede_ehon.webp')] bg-cover bg-center bg-no-repeat opacity-30"></div>
  
      <!-- コンテンツ -->
      <div class="relative z-10 w-full">
        <slot></slot>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "BackgroundWrapper",
  };
  </script>
  
  <style scoped>
  /* 必要に応じて追加スタイルを定義 */
  </style>
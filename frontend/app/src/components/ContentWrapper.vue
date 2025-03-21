<template>
    <div class="max-w-md mx-auto p-6 bg-white bg-opacity-80 rounded-lg shadow-lg">
      <h2 class="text-3xl font-extrabold text-red-600 mb-2 text-center font-serif">Masquerade Panel</h2>
      <slot></slot>
    </div>
  </template>
  
  <script>
  export default {
    name: "ContentWrapper",
  };
  </script>
  
  <style scoped>
  /* 必要に応じて追加スタイル */
  </style>
  
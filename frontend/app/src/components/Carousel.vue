<template>
  <BackgroundWrapper>
    <ContentWrapper class="w-full max-w-screen-lg">
      <div class="flex flex-col items-center space-y-4">
        <!-- 画像のみのカルーセル -->
        <Carousel v-bind="configImage">
          <Slide v-for="image in images" :key="image.id">
            <img :src="image.url" alt="image" class="rounded-lg w-full h-auto object-cover max-h-[500px]" />
          </Slide>
        </Carousel>

        <!-- 名前 & コメントのカルーセル -->
        <Carousel v-bind="configLabel">
          <Slide v-for="image in images" :key="image.id">
            <div class="p-6 border rounded-lg shadow-lg bg-white text-center text-xl">
              <p class="text-2xl font-bold">{{ image.name }}</p>
              <p class="text-lg text-gray-600">{{ image.comment }}</p>
            </div>
          </Slide>
        </Carousel>
      </div>
    </ContentWrapper>
  </BackgroundWrapper>
</template>


<script setup>
import { onMounted } from "vue";
import 'vue3-carousel/carousel.css'
import { Carousel, Slide, Navigation } from 'vue3-carousel'
import BackgroundWrapper from './BackgroundWrapper.vue';
import ContentWrapper from './ContentWrapper.vue';
const axios = require("axios");

// const images = Array.from({ length: 10 }, (_, index) => ({
//   id: index + 1,
//   url: `https://picsum.photos/seed/${Math.random()}/800/600`
// }));

let images = [];

const configImage = {
  autoplay: 1500,
  height: 600,
  itemsToShow: 1,
  gap: 5,
  wrapAround: true,
};

const configLabel = {
  autoplay: 1500,
  height: 100,
  itemsToShow: 1,
  gap: 5,
  wrapAround: true,
};


function getPost() {
  axios
    .get(
      process.env.VUE_APP_BASE_URL + '/api/view',
      {
        headers: {
          'ngrok-skip-browser-warning': 'value'
        }
      }
    )
    .then( function (response) {

      const posts = [];
      console.log(response.data.posts.length);
      for (let i = 0; i < response.data.posts.length; i++) {
        posts.push({
          id: response.data.posts[i].id,
          url: process.env.VUE_APP_BASE_URL + '/' + response.data.posts[i].masked_img_path,
          name: response.data.posts[i].user_name,
          comment: response.data.posts[i].comment
        });
      }
      images = posts;
    }).catch(function (error) {
      console.log(error);
    });
}

onMounted(() => {
  getPost();
});
</script>


<style>

.carousel {
  --vc-nav-background: rgba(255, 255, 255, 0.7);
  --vc-nav-border-radius: 100%;
}

img {
  border-radius: 8px;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.w-full {
  width: 100vw;
}

.slide {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>

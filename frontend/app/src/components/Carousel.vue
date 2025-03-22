<template>
	<Carousel v-bind="config">
		<Slide v-for="image in images" :key="image.id">
        		<img :src="image.url" alt="image" />
    		</Slide>

	</Carousel>
	<Carousel v-bind="config">
		<Slide v-for="image in images" :key="image.id">
			{{image.id}}
    		</Slide>
	</Carousel>
</template>

<script setup>
import { onMounted } from "vue";
import 'vue3-carousel/carousel.css'
import { Carousel, Slide, Navigation } from 'vue3-carousel'
const axios = require("axios");

// const images = Array.from({ length: 10 }, (_, index) => ({
//   id: index + 1,
//   url: `https://picsum.photos/seed/${Math.random()}/800/600`
// }));

let images = [];

const config = {
  autoplay: 1000,
  height: 200,
  itemsToShow: 2,
  gap: 5,
  wrapAround: true,
}

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
      console.log(response.data);

      const posts = [];
      console.log(response.data.posts);
      for (let i = 0; i < response.data.posts.length; i++) {
        posts.push({
          id: response.data.posts[i].id,
          url: process.env.VUE_APP_BASE_URL + '/' + response.data.posts[i].masked_img_path,
          name: response.data.posts[i].user_name,
          comment: response.data.posts[i].comment
        });
      }
      console.log(posts);
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
</style>

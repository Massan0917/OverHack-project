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
import 'vue3-carousel/carousel.css'
import { Carousel, Slide, Navigation } from 'vue3-carousel'

const images = Array.from({ length: 10 }, (_, index) => ({
  id: index + 1,
  url: `https://picsum.photos/seed/${Math.random()}/800/600`,
}))

const config = {
    autoplay: 1000,
    height: 200,
    itemsToShow: 2,
    gap: 5,
    wrapAround: true,
}

function getPost() {
        const self = this;
        console.log('get post');

        axios
        .get('http://localhost:3000/api/view')
        .then( function (response) {
          self.posts = response.data;
        }).catch(function (error) {
          console.log(error);
        });
      }

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

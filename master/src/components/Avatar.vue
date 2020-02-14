<template>
  <v-img :src="image" max-height="250" class="bg-size-contain"/>
</template>

<script>
export default {
  name: "Avatar",
  data: () => {
    return {
      image: 'http://filipecruz.zeedhi.com/workfolder/iris/default.svg'
    };
  },
  mounted() {
    this.$root.$on('changeAvatar', (newImage) => { 
     this.image = newImage;
    })
  }
};
</script>


<style>
.bg-size-contain .v-image__image--cover {
    background-size: contain;
}
</style>

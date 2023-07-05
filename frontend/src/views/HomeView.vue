<script setup>
import BgSession from '../components/BgSession.vue'
</script>

<template>
  <main>
    <BgSession id="bg" />
  </main>
</template>

<style scoped>
#bg {
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  align-items: center;
  visibility: hidden;
}
@media (min-width: 1024px) {
  #bg {
    margin-top: 0;
  }
}

@media screen and (min-width: 320px) {
}
@media screen and (min-width: 480px) {
}
@media screen and (min-width: 600px) {
}
@media screen and (min-width: 768px) {
}
@media screen and (min-width: 992px) {
  #bg {
    visibility: visible;
  }
}
</style>

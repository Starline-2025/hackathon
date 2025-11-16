<script setup>
import Home from './views/Home.vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import NKOFormModal from './components/NKOFormModal.vue'
import { ref } from 'vue'

const isOpenModal = ref(false)

const toggleOpenModal = () => {
  isOpenModal.value = !isOpenModal.value
}
</script>

<template>
  <div class="page-wrapper">
    <NKOFormModal
      v-if="isOpenModal"
      :isOpenModal="isOpenModal"
      @toggleOpenModal="toggleOpenModal"
    />
    <Header @toggleOpenModal="toggleOpenModal" />
    <div class="main-content">
      <Home />
    </div>
    <Footer />
  </div>
</template>

<style lang="scss" scoped>
.page-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
}
</style>

<script setup>
import { ref, reactive, provide } from 'vue'

import Home from './views/Home.vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import NKOFormModal from './components/NKOFormModal.vue'
import nkoData from './data/organizations.js'

const organizations = reactive(nkoData)
const isOpenModal = ref(false)

const toggleOpenModal = () => {
  isOpenModal.value = !isOpenModal.value
}

provide('organizations', organizations)
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
      <RouterView />
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

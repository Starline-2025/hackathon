<script setup>
import Home from './views/Home.vue'
import Header from './components/Header.vue'
import NKOFormModal from './components/NKOFormModal.vue'
import { ref } from 'vue'

const isOpenModal = ref(false)

const toggleOpenModal = () => {
  isOpenModal.value = !isOpenModal.value
}
</script>

<template>
  <div>
    <NKOFormModal
      v-if="isOpenModal"
      :isOpenModal="isOpenModal"
      @toggleOpenModal="toggleOpenModal"
    />
    <Header @toggleOpenModal="toggleOpenModal" />
    <Home />
  </div>
</template>

<style scoped></style>

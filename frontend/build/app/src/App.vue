<script setup>
import { ref, reactive, provide, onMounted } from 'vue'

import Home from './views/Home.vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import NKOFormModal from './components/NKOFormModal.vue'

const organizations = reactive([])

async function getAllCards() {
  try {
    const response = await fetch('/api/cards')
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    organizations.splice(0, organizations.length, ...data)
    console.log('organizations', organizations)

    return data
  } catch (error) {
    console.log('Error', error)
  }
}

onMounted(async () => {
  await getAllCards()
})

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

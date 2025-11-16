<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import '../assets/styles/components/header.scss'

const emit = defineEmits(['toggleOpenModal'])

const handleOpen = () => {
  emit('toggleOpenModal')
}

const activeIndex = ref(1)
const isMobileMenuOpen = ref(false)
const isMobile = ref(false)

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const handleNavClick = (id) => {
  activeIndex.value = id
  if (isMobile.value) {
    isMobileMenuOpen.value = false
  }
}

const checkMobile = () => {
  isMobile.value = window.innerWidth <= 768
  if (!isMobile.value) {
    isMobileMenuOpen.value = false
  }
}

onMounted(() => {
  checkMobile()
  window.addEventListener('resize', checkMobile)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkMobile)
})

const listNavItems = reactive([
  {
    id: 1,
    text: 'Карта',
    icon: '/icons/marker.png',
    route: '/',
  },
  {
    id: 2,
    text: 'Список организаций',
    icon: '/icons/list.png',
    route: '/organizations',
  },
  {
    id: 3,
    text: 'О проекте',
    icon: '/icons/info-white.png',
    route: '/about',
  },
])
</script>

<template>
  <header class="header">
    <div class="header-inner">
      <RouterLink to="/">
        <div class="header-block">
          <img class="logo" src="/logo-header.png" alt="Логотип" />
          <div class="logo-divider"></div>
          <div class="header-text">
            <h3>Карта добрых дел</h3>
            <p>НКО и волонтёрские организации городов Росатома</p>
          </div>
        </div>
      </RouterLink>

      <button
        class="burger-btn"
        @click="toggleMobileMenu"
        :class="{ active: isMobileMenuOpen }"
        v-if="isMobile"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>

      <nav class="nav" :class="{ 'mobile-open': isMobileMenuOpen }">
        <ul class="menu-list">
          <RouterLink
            v-for="item in listNavItems"
            :key="item.id"
            :to="item.route"
            class="menu-item"
            :class="{ active: activeIndex === item.id }"
            @click="handleNavClick(item.id)"
          >
            <img :src="item.icon" :alt="item.text" />
            {{ item.text }}
          </RouterLink>
        </ul>
      </nav>

      <button class="btn btn-primary" @click="handleOpen">Добавить НКО</button>

      <div
        class="nav-overlay"
        :class="{ active: isMobileMenuOpen && isMobile }"
        @click="toggleMobileMenu"
        v-if="isMobile"
      ></div>
    </div>
  </header>
</template>

<style lang="scss" scoped></style>

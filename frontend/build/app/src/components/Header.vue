<script setup>
import { ref, reactive } from 'vue'

const emit = defineEmits(['toggleOpenModal'])

const handleOpen = () => {
  emit('toggleOpenModal')
}

const activeIndex = ref(null)

const listNavItems = reactive([
  {
    id: 1,
    text: 'Карта',
    icon: '/icons/marker.png',
  },
  {
    id: 2,
    text: 'Список организаций',
    icon: '/icons/list.png',
  },
  {
    id: 3,
    text: 'О проекте',
    icon: '/icons/info-white.png',
  },
])
</script>

<template>
  <header class="header">
    <div class="header-inner">
      <div class="header-block">
        <img class="logo" src="/logo-header.png" alt="" />
        <div class="logo-divider"></div>
        <div>
          <h3 class="heading heading-3">Карта добрых дел</h3>
          <p class="subheading">НКО и волонтёрские организации городов Росатома</p>
        </div>
      </div>
      <nav class="nav">
        <ul class="menu-list">
          <li
            v-for="item in listNavItems"
            :key="item.id"
            :class="{ active: activeIndex === item.id }"
            @click="activeIndex = item.id"
          >
            <img :src="item.icon" alt="" />
            {{ item.text }}
          </li>
        </ul>
      </nav>
      <button class="btn btn-primary" @click="handleOpen">Добавить НКО</button>
    </div>
  </header>
</template>

<style lang="scss" src="../assets/styles/components/header.scss" scoped></style>

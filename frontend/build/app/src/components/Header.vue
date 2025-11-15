<script setup>
import { ref, reactive } from 'vue'

const activeIndex = ref(null)

const listNavItems = reactive([
  {
    id: 1,
    text: 'Карта',
    icon: '/header/marker.png',
  },
  {
    id: 2,
    text: 'Список организаций',
    icon: '/header/list.png',
  },
  {
    id: 3,
    text: 'О проекте',
    icon: '/header/info.png',
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
      <button class="btn btn-primary">Добавить НКО</button>
    </div>
  </header>
</template>

<style lang="scss" src="../assets/styles/components/header.scss" scoped></style>

<script setup>
import { inject } from 'vue'
import '../assets/styles/views/home.scss'
import Map from '../components/Map.vue'
import Filters from '../components/Filters.vue'
import CardList from '../components/CardList.vue'

const organizations = inject('organizations')

const displayedOrganizations = organizations.slice(0, 4)
</script>

<template>
  <div class="container">
    <div class="content">
      <div class="hero">
        <h1><span>Найди, </span><span>где ты нужен</span></h1>
        <p>
          Интерактивная карта НКО в городах присутствия Росатома. Присоединяйся — твоя помощь важна!
        </p>
      </div>
      <Filters />
      <Map />
      <h2>Организации</h2>
      <div class="card-section">
        <CardList :items="displayedOrganizations" />
        <RouterLink to="/organizations">
          <button class="btn show-more-btn">Показать все</button>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped></style>

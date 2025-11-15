<script setup>
import { computed, reactive, ref } from 'vue'
import Map from '../components/Map.vue'
import Filters from '../components/Filters.vue'
import OrganizationCard from '../components/OrganizationCard.vue'
import nkoData from '../data/organizations.js'

const organizations = reactive(nkoData)
const showAll = ref(false)

const toggleShowAll = () => {
  showAll.value = !showAll.value
}

const displayedOrganizations = computed(() => {
  return showAll.value ? organizations : organizations.slice(0, 3)
})
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
      <h3>Организации</h3>
      <div class="card-grid">
        <OrganizationCard
          v-for="org in displayedOrganizations"
          :key="org.id"
          :name="org.name"
          :category="org.category"
          :description="org.description"
          :city="org.city"
        />
        <button v-if="!showAll" class="btn show-more-btn" @click="toggleShowAll">
          Показать все ({{ organizations.length }})
        </button>
        <button v-else class="btn show-more-btn" @click="toggleShowAll">Скрыть</button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" src="../assets/styles/views/home.scss" scoped></style>

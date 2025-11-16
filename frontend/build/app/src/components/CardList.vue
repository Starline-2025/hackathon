<script setup>
import '../assets/styles/components/card-list.scss'
import OrganizationCard from '../components/OrganizationCard.vue'

defineProps({
  items: Array,
})
</script>

<template>
  <div class="card-grid">
    <OrganizationCard
      v-for="org in items"
      :key="org.id"
      :name="org.name"
      :category="org.category"
      :description="org.description"
      :city="org.city"
      :img="org.img"
      :website="org.website"
      :address="org.address"
      :contacts="org.contacts"
    />
    <RouterLink v-if="items.lenght === 4" to="/organizations">
      <button class="btn show-more-btn">Показать все</button>
    </RouterLink>
  </div>
</template>

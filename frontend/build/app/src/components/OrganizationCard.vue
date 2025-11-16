<script setup>
import '../assets/styles/components/organization-card.scss'
defineProps({
  name: String,
  category: String,
  city: String,
  description: String,
  img: String,
  website: String,
  address: String,
  contacts: String,
})
</script>

<template>
  <div class="card">
    <div class="card-header">
      <div class="card-avatar">
        <img :src="img" alt="" />
      </div>
      <div class="card-info">
        <h3 class="card-title">{{ name }}</h3>
        <div class="card-meta">
          <span class="card-location">
            <img src="/icons/marker-black.png" alt="" />
            <p>{{ city }}</p>
          </span>
          <div v-if="address" class="card-address">
            <img src="/icons/marker-black.png" alt="" />
            <p>{{ address }}</p>
          </div>
          <span class="card-category">
            <img src="/icons/category.png" alt="" />
            <p>{{ category }}</p>
          </span>
        </div>
      </div>
    </div>
    <p class="card-description">
      {{ description }}
    </p>
    <div class="card-website">
      <img src="/icons/web.png" alt="" />
      <a :href="website" target="_blank" rel="noopener noreferrer">
        {{ website }}
      </a>
    </div>

    <div v-if="contacts" class="card-contacts">
      <img src="/icons/phone.png" alt="" />
      <p>{{ contacts }}</p>
    </div>
    <div class="card-actions">
      <button class="btn btn-secondary">
        <img src="/icons/marker.svg" alt="" width="26" height="26" />
        <span>На карте</span>
      </button>
    </div>
  </div>
</template>

<style lang="scss" scoped></style>

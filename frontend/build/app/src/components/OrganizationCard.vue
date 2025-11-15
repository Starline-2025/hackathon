<script setup>
defineProps({
  name: String,
  category: String,
  city: String,
  description: String,
  tags: Array,
})
</script>

<template>
  <div class="card">
    <div class="card__header">
      <div class="card__avatar">ЭД</div>
      <div class="card__info">
        <h3 class="card__title">{{ name }}</h3>
        <div class="card__meta">
          <span class="card__location">📍 {{ city }}</span>
          <span class="card__category">🏷️ {{ category }}</span>
        </div>
      </div>
    </div>
    <p class="card__description">
      {{ description }}
    </p>
    <div class="card__tags">
      <span class="tag">Переработка</span>
      <span class="tag">Озеленение</span>
      <span class="tag">Экопросвещение</span>
    </div>
    <div class="card__actions">
      <button class="btn btn-secondary">
        <img src="/icons/marker.svg" alt="" width="26" height="26" />
        <span>На карте</span>
      </button>
    </div>
  </div>
</template>

<style lang="scss" src="../assets/styles/components/organization-card.scss" scoped></style>

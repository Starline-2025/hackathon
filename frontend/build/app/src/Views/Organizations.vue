<script setup>
import { inject } from 'vue'
import '../assets/styles/views/organizations.scss'
import CardList from '../components/CardList.vue'

const organizations = inject('organizations')
</script>

<template>
  <div class="container">
    <h2>Организации</h2>
    <CardList :items="organizations" />
  </div>
</template>

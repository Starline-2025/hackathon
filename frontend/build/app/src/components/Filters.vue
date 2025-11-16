<script setup>
import '../assets/styles/components/filters.scss'
</script>

<template>
  <section class="filters">
    <div class="search-bar">
      <input type="text" id="searchInput" placeholder="Поиск по названию организации..." />
      <button>Найти</button>
    </div>

    <div class="filter-sections">
      <div class="filter-group">
        <h3>Категория</h3>
        <div class="filter-options">
          <div class="filter-option">
            <input type="checkbox" id="children" />
            <label for="children">Помощь детям</label>
          </div>
          <div class="filter-option">
            <input type="checkbox" id="elderly" />
            <label for="elderly">Пожилым</label>
          </div>
          <div class="filter-option">
            <input type="checkbox" id="ecology" />
            <label for="ecology">Экология</label>
          </div>
          <div class="filter-option">
            <input type="checkbox" id="animals" />
            <label for="animals">Животные</label>
          </div>
          <div class="filter-option">
            <input type="checkbox" id="education" />
            <label for="education">Образование</label>
          </div>
        </div>
      </div>

      <div class="filter-group">
        <h3>Город</h3>
        <div class="filter-options">
          <div class="filter-option">
            <input type="checkbox" id="sarov" />
            <label for="sarov">Саров</label>
          </div>
          <div class="filter-option">
            <input type="checkbox" id="obninsk" />
            <label for="obninsk">Обнинск</label>
          </div>
          <div class="filter-option">
            <input type="checkbox" id="seversk" />
            <label for="seversk">Северск</label>
          </div>
          <div class="filter-option">
            <input type="checkbox" id="volgodonsk" />
            <label for="volgodonsk">Волгодонск</label>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped></style>

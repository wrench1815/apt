<script setup lang="ts">
import { ref } from 'vue';

const searchTerm = ref('');

function searchProduct() {}
</script>

<template>
  <form class="w-aut" @submit.prevent="searchProduct">
    <div class="d-flex gap-1 flex-column flex-md-row">
      <input
        type="search"
        class="form-control"
        placeholder="Search Product"
        aria-label="Search"
        v-model="searchTerm"
      />

      <button type="submit" class="btn btn-primary btn-floatin">Search</button>
    </div>
  </form>
</template>

<style scoped></style>

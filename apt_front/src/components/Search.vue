<script setup lang="ts">
import { ref } from 'vue';

const emit = defineEmits(['product-search']);
const searchTerm = ref('');

function searchProduct() {
  emit('product-search', searchTerm.value);
}
</script>

<template>
  <form
    class="position-sticky top-0 card card-body search-form"
    @submit.prevent="searchProduct"
  >
    <div class="d-flex gap-1 flex-column flex-md-row">
      <input
        type="text"
        class="form-control"
        placeholder="Search Product"
        aria-label="Search"
        v-model="searchTerm"
      />

      <button type="submit" class="btn btn-primary btn-floatin">Search</button>
    </div>
  </form>
</template>

<style scoped>
.search-form {
  z-index: 1000 !important;
}
</style>

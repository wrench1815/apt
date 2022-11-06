<script setup lang="ts">
import Table from '@/components/Table.vue';
import Search from '@/components/Search.vue';
import ProductModal from '@/components/ProductModal.vue';

import axios from 'axios';
import { onMounted, ref } from 'vue';

const products = ref([]);
const loading = ref(true);

const url = 'http://localhost:8000/';

async function getProducts() {
  return axios.get(url + 'api/product/').then((res) => {
    products.value = res.data;
  });
}

async function refreshProducts() {
  loading.value = true;
  return getProducts().then(() => {
    loading.value = false;
  });
}

onMounted(() => {
  getProducts().then(() => {
    loading.value = false;
  });
});
</script>

<template>
  <div class="mt-2"></div>

  <main class="container-fluid">
    <Search />
    <div class="d-flex justify-content-end my-4">
      <button
        class="btn btn-rounded btn-primary"
        data-mdb-toggle="modal"
        data-mdb-target="#AddProduct"
      >
        Add new Product
      </button>
    </div>

    <Table v-if="!loading" :products="products" />
    <ProductModal @product-add="refreshProducts" />
  </main>
</template>

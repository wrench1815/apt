<script setup lang="ts">
import Table from '@/components/Table.vue';
import Search from '@/components/Search.vue';
import ProductModal from '@/components/ProductModal.vue';

import axios from 'axios';
import { onMounted, ref } from 'vue';

const products = ref([]);
const loading = ref(true);

const url = 'https://apt-back.onrender.com/';

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

async function productSearch(product: string) {
  return axios
    .get(url + 'api/product/', { params: { search: product } })
    .then((res) => {
      products.value = res.data;
    });
}

onMounted(() => {
  getProducts().then(() => {
    loading.value = false;
  });
});
</script>

<template>
  <Search @product-search="productSearch" />
  <main class="container-fluid">
    <div class="d-flex justify-content-end my-4">
      <button
        class="btn btn-rounded btn-primary"
        data-mdb-toggle="modal"
        data-mdb-target="#AddProduct"
      >
        Add new Product
      </button>
    </div>

    <Table
      v-if="!loading"
      :products="products"
      @table-product-edit="refreshProducts"
    />
    <ProductModal @product-add="refreshProducts" />
  </main>

  <footer class="d-flex justify-content-center mt-4">
    <a
      href="https://github.com/wrench1815/apt"
      target="_blank"
      class="btn btn-dark"
      >source code</a
    >
  </footer>
</template>

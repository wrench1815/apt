<script setup lang="ts">
import { onMounted, ref } from 'vue';
import * as mdb from 'mdb-ui-kit';
import axios from 'axios';

const product = ref({
  name: '',
  price: '',
  quantity: '',
});

const emit = defineEmits(['product-add']);

const url = 'http://localhost:8000/api/product/';

async function addProduct() {
  return axios
    .post(url, product.value)
    .then((res) => {
      if (res.status == 201) {
        emit('product-add');
        document.getElementById('AddProductClose')?.click();
      }
    })
    .catch((err) => {
      console.log(err);
      console.log(err.response);
      console.log(err.response.data);
    });
}

function modalClose() {
  const form = document.querySelector('#addProductForm') as HTMLFormElement;
  form.reset();
}

onMounted(() => {
  // initialize form elements
  document.querySelectorAll('.form-outline').forEach((formOutline) => {
    new mdb.Input(formOutline).init();
  });
});
</script>

<template>
  <!-- Modal -->
  <div
    class="modal top fade"
    id="AddProduct"
    tabindex="-1"
    aria-labelledby="AddProductLabel"
    aria-hidden="true"
    data-mdb-backdrop="static"
    data-mdb-keyboard="false"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="AddProductLabel">Add an new Product</h5>
          <button
            id="AddProductClose"
            type="button"
            class="btn-close"
            data-mdb-dismiss="modal"
            aria-label="Close"
            @click="modalClose"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addProduct" id="addProductForm">
            <!-- Product Name -->
            <div class="form-outline mb-4">
              <input
                type="text"
                class="form-control"
                v-model="product.name"
                required
              />
              <label class="form-label">
                Product Name <span class="text-danger">*</span>
              </label>
            </div>

            <!-- Product Price -->
            <div class="form-outline mb-4">
              <input
                type="number"
                class="form-control"
                v-model="product.price"
                required
              />
              <label class="form-label">
                Price <span class="text-danger">*</span>
              </label>
            </div>

            <!-- Product Quantity -->
            <div class="form-outline mb-4">
              <input
                type="number"
                class="form-control"
                v-model="product.quantity"
                required
              />
              <label class="form-label">
                Quantity <span class="text-danger">*</span>
              </label>
            </div>

            <!-- Submit button -->
            <button type="submit" class="btn btn-primary btn-block">
              Add Product
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>

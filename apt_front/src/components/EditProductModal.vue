<script setup lang="ts">
import { onMounted, ref } from 'vue';
import * as mdb from 'mdb-ui-kit';
import axios from 'axios';

interface Product {
  id: number;
  name: string;
  price: string | number;
  quantity: number;
  date_added: string;
}

const props = defineProps<{
  data: Product;
}>();

const product = ref<Product>({
  id: 0,
  name: '',
  price: '',
  quantity: 0,
  date_added: '',
});

const emit = defineEmits(['product-edit']);
const url = 'https://apt-back.onrender.com/api/product/';

async function editProduct() {
  return axios
    .patch(url + `${props.data.id}/`, product.value)
    .then((res) => {
      if (res.status == 200) {
        emit('product-edit');
        document.getElementById(`EditProductClose${props.data.id}`)?.click();
      }
    })
    .catch((err) => {
      console.log(err);
      console.log(err.response);
      console.log(err.response.data);
    });
}

function modalClose() {
  product.value = { ...props.data };
}

onMounted(() => {
  product.value = { ...props.data };

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
    :id="`EditProduct${props.data.id}`"
    tabindex="-1"
    :aria-labelledby="`EditProductLabel${props.data.id}`"
    aria-hidden="true"
    data-mdb-backdrop="static"
    data-mdb-keyboard="false"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" :id="`EditProductLabel${props.data.id}`">
            Edit Product
          </h5>
          <button
            :id="`EditProductClose${props.data.id}`"
            type="button"
            class="btn-close"
            data-mdb-dismiss="modal"
            aria-label="Close"
            @click="modalClose"
          ></button>
        </div>
        <div class="modal-body">
          <form
            @submit.prevent="editProduct"
            :id="`EditProductForm${props.data.id}`"
          >
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
              Update Product
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>

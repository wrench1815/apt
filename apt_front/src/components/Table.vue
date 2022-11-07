<script setup lang="ts">
import EditModal from '@/components/EditProductModal.vue';
import NoData from '@/components/NoData.vue';

const props = defineProps<{
  products: Array<{
    id: number;
    name: string;
    price: string | number;
    quantity: number;
    date_added: string;
  }>;
}>();

const emit = defineEmits(['table-product-edit']);

function formattedDate(inputDate: string) {
  const date = new Date(inputDate);
  return `${date.toLocaleString('default', {
    weekday: 'short',
  })}, ${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`;
}
</script>

<template>
  <div class="card card-bod">
    <div class="table-responsive">
      <table class="table">
        <thead class="bg-primary text-white fs-6">
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Price</th>
            <th scope="col">Quantity</th>
            <th scope="col" class="text-nowrap">Date added</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody v-if="products.length != 0">
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.name }}</td>
            <td class="text-nowrap">Rs. {{ product.price }}</td>
            <td>{{ product.quantity }} units</td>
            <td class="text-nowrap">{{ formattedDate(product.date_added) }}</td>
            <td>
              <div>
                <button
                  class="btn btn-rounded btn-info"
                  data-mdb-toggle="modal"
                  :data-mdb-target="`#EditProduct${product.id}`"
                >
                  Edit
                </button>
              </div>
              <EditModal
                :key="product.id"
                :data="product"
                @product-edit="$emit('table-product-edit')"
              />
            </td>
          </tr>
        </tbody>
        <tbody v-else>
          <td colspan="5" class="bg-white">
            <NoData class="mx-auto" message="No Products found" />
          </td>
        </tbody>
      </table>
    </div>
  </div>
</template>

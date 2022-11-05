<script setup lang="ts">
const props = defineProps<{
  products: Array<{
    id: number;
    name: string;
    price: string | number;
    quantity: number;
    date_added: string;
  }>;
}>();

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
      <table class="table table-hover">
        <thead class="bg-primary text-white fs-6">
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Price</th>
            <th scope="col">Quantity</th>
            <th scope="col">Date added</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.name }}</td>
            <td>Rs. {{ product.price }}</td>
            <td>{{ product.quantity }} units</td>
            <td>{{ formattedDate(product.date_added) }}</td>
            <td>
              <div>
                <button class="btn btn-rounded btn-info">Edit</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped></style>

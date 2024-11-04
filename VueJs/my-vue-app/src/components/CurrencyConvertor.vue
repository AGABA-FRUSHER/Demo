<template>
    <div class="currency-converter">
      <slot name="input">
        <input v-model="price" placeholder="Enter price" />
      </slot>
      <slot name="currency-selector">
        <select v-model="fromCurrency">
          <option v-for="currency in currencies" :key="currency" :value="currency">{{ currency }}</option>
        </select>
        <select v-model="toCurrency">
          <option v-for="currency in currencies" :key="currency" :value="currency">{{ currency }}</option>
        </select>
      </slot>
      <button @click="convertCurrency">Convert</button>
      <slot name="output">
        <div v-if="convertedAmount">{{ convertedAmount }}</div>
        <div v-else>Converted amount will appear here</div>
      </slot>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  
  export default {
    name: 'CurrencyConverter',
    props: {
      price: {
        type: Number,
        required: true,
      },
      fromCurrency: {
        type: String,
        required: true,
      },
      toCurrency: {
        type: String,
        required: true,
      },
      currencies: {
        type: Array,
        required: true,
      },
    },
    setup(props, { emit }) {
      // Reactive state for price, currencies, and conversion results
      const price = ref(props.price);
      const fromCurrency = ref(props.fromCurrency);
      const toCurrency = ref(props.toCurrency);
      const convertedAmount = ref(null);
      const currencies = computed(() => props.currencies);
  
      // Method to make an API call for currency conversion
      async function convertCurrency() {
        try {
          // Example API call, replace with actual API and error handling
          const response = await fetch(`/api/convert?from=${fromCurrency.value}&to=${toCurrency.value}&amount=${price.value}`);
          const data = await response.json();
          convertedAmount.value = data.result;
          emit('conversionComplete', convertedAmount.value); // Emit event with the converted amount
        } catch (error) {
          console.error('Error converting currency:', error);
        }
      }
  
      return {
        price,
        fromCurrency,
        toCurrency,
        convertedAmount,
        currencies,
        convertCurrency,
      };
    },
  };
  </script>
  
  <style scoped>
  .currency-converter {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  </style>
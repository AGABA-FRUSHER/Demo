<template>
    <div>
      <input :placeholder="placeholder" v-model="searchValue" @input="emitInputEvent" />
    </div>
  </template>
  
  <script>
  export default {
    props: {
      value: { type: String, default: '' },
      placeholder: { type: String, default: '' },
    },
    data() {
      return {
        searchValue: this.value,
      };
    },
    watch: {
      value(newValue) {
        this.searchValue = newValue;
      },
      searchValue(newValue) {
        this.$emit('input', newValue);
      },
    },
    methods: {
      emitInputEvent() {
        this.$emit('input', this.searchValue);
      },
    },
  };
  </script>
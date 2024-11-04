<template>
  <div>
    <!-- Dynamically generate SearchInput fields based on searchFields array -->
    <div v-for="field in searchFields" :key="field.name">
      <SearchInput
        v-model="search[field.name]"
        :placeholder="field.placeholder"
        @input="debouncedSearch"
      />
    </div>

    <button @click="performSearch">Search</button>

    <!-- Display search results -->
    <div v-if="results.length">
      <div v-for="result in results" :key="result.id">
        <h3>{{ result.title }}</h3>
        <p>{{ result.author }}</p>
        <p>{{ result.genre }}</p>
        <p>{{ result.content }}</p>
      </div>
      <button @click="changePage(currentPage - 1)" :disabled="currentPage <= 1">Previous</button>
      <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages">Next</button>
    </div>

    <div v-if="error" class="error-message">{{ errorMessage }}</div>
  </div>
</template>

<script>
import debounce from 'lodash.debounce';
import SearchInput from './SearchInput.vue';

export default {
  components: {
    SearchInput
  },
  data() {
    return {
      // Array for search field configuration
      searchFields: [
        { name: 'author', placeholder: 'Author' },
        { name: 'title', placeholder: 'Title' },
        { name: 'genre', placeholder: 'Genre' },
        { name: 'content', placeholder: 'Content' }
      ],
      search: {
        author: '',
        title: '',
        genre: '',
        content: ''
      },
      results: [],
      currentPage: 1,
      totalPages: 1,
      error: false,
      errorMessage: ''
    };
  },
  methods: {
    async performSearch() {
      const query = {
        author_like: this.search.author,
        title_like: this.search.title,
        genre_like: this.search.genre,
        content_like: this.search.content,
        _page: this.currentPage,
        _limit: 10
      };

      try {
        const response = await fetch(`http://localhost:3000/books?${new URLSearchParams(query)}`);
        
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        
        // Assuming the API provides a 'total' field for total results.
        this.results = data.results;
        this.totalPages = Math.ceil(data.total / 10);
        this.error = false;
      } catch (error) {
        this.error = true;
        this.errorMessage = 'Failed to retrieve search results. Please try again later.';
        console.error("Error details:", error);
      }
    },
    changePage(page) {
      this.currentPage = page;
      this.performSearch();
    },
    debouncedSearch: debounce(function() {
      this.performSearch();
    }, 300)
  }
};
</script>

<style scoped>
.error-message {
  color: red;
}
</style>
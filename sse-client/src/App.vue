<template>
  <div id="app">
    <h1>Server-Sent Events with Vue.js</h1>
    <p>Latest message from server: {{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Waiting for server message..."
    };
  },
  mounted() {
    const eventSource = new EventSource("http://localhost:5000/events");
    eventSource.onmessage = (event) => {
      this.message = event.data;
    };
  },
};
</script>

<style scoped>
h1 {
  font-family: Arial, sans-serif;
}
</style>


<template>
  <div id="app">
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/expenses">Expenses</router-link></li>
        <li><router-link to="/budgets">Budgets</router-link></li>
        <li><router-link to="/savings">Savings</router-link></li>
        <li><router-link to="/investments">Investments</router-link></li>
      </ul>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/* Add any global styles */
</style>

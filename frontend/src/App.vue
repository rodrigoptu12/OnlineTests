<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorldOnlineTestes from './components/HelloWorldOnlineTestes.vue'
import UnbLogo from './components/images/UnbLogo.vue'
import OnlineTestesLogo from './components/images/OnlineTestesLogo.vue'
</script>

<template>
  <header v-if="idHomeViewRoute">
    <!--<img alt="Online tests logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />-->
    <OnlineTestesLogo alt="Online tests logo" class="logo" width="125" height="125" />

    <div class="wrapper">
      <HelloWorldOnlineTestes msg="Online Testes" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/signin">Acessar/Cadastrar</RouterLink>
      </nav>
      <UnbLogo />
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
*{
  margin: 0;
}
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
  color: var(--color-logo-primary) !important;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 ;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  *{
    margin: 0;
    padding: 0;
  }
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
    flex-direction: column;
    width: 25rem;
    margin-right: -11rem;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding:  0;
    margin-top: 1rem;
  }
}
</style>

<script>
export default {
  computed: {
    idHomeViewRoute() {
      return this.$route.path === '/'
    }
  }
}
</script>

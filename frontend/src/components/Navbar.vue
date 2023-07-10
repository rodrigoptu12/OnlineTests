<script setup>
import { ref } from 'vue'
import OnlineTestesLogoSolid from './images/OnlineTestesLogoSolid.vue'

import { Bars3Icon } from '@heroicons/vue/24/outline'

const mobileMenuOpen = ref(false)
</script>

<template>
  <header class="bg-white">
    <nav
      id="navbar"
      class="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8"
      aria-label="Global"
    >
      <div class="flex">
        <a href="#" class="flex">
          <OnlineTestesLogoSolid />
          <span class="font-semibold text-xl tracking-tight ml-4 mr-4 text-white"
            >Online Testes</span
          >
        </a>
      </div>
      <div class="flex lg:hidden">
        <button
          type="button"
          class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
          @click="mobileMenuOpen = true"
        >
          <span class="sr-only">Open main menu</span>
          <Bars3Icon class="h-6 w-6" aria-hidden="true" />
        </button>
      </div>
      <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto ml-20">
        <div class="text-sm lg:flex-grow">
          <a
            href="/new-exam"
            class="block mt-4 lg:inline-block lg:mt-0 text-blue-700 hover:text-white mr-4 text-sm font-semibold leading-6 text-blue dark:text-blue"
            >Exames</a
          >
          <a
            href="new-question"
            class="block mt-4 lg:inline-block lg:mt-0 text-blue-700 hover:text-white mr-4 text-sm font-semibold leading-6 text-blue dark:text-blue"
            >Questões</a
          >
          <a
            href="#"
            class="block mt-4 lg:inline-block lg:mt-0 text-blue-700 hover:text-white mr-4 text-sm font-semibold leading-6 text-blue dark:text-blue"
            >...</a
          >
        </div>
      </div>
      <div class="hidden lg:flex lg:flex-1 lg:justify-end">
        <button class="text-sm font-semibold leading-6 text-blue dark:text-blue hover:text-white" @click="handleLogout">Logout</button>
      </div>
    </nav>
  </header>
</template>

<style>
#navbar {
  background-color: var(--color-navbar-background);
}
</style>

<script>
export default {
  methods: {
    handleLogout() {
      localStorage.removeItem('access_token');
      this.$router.push('/');
    }
  }
}
</script>
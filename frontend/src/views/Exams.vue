<script setup>
import Navbar from '../components/Navbar.vue'
</script>

<template class="flex">
  <div class="w-full">
    <Navbar />
  </div>

  <div class="flex wrapper">
    <div class="flex mb-6">
      <div class="wrapper-headline w-full">
        <h1
          class="mb-1 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl"
        >
          Exames.
        </h1>
        <p class="text-lg font-normal text-gray-500 lg:text-l dark:text-gray-400 mb-4">
          Área de listagem de exames.
        </p>
        <div class="block w-full"></div>
      </div>
    </div>

    <div class="wrapper relative overflow-x-auto border dark:border-blue sm:rounded-l">
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead
          class="text-xs text-gray-700 uppercase bg-gray-50 dark:transparent dark:text-gray-400"
        >
          <tr>
            <th scope="col" class="px-6 py-3">
              <b>Nome do exame</b>
            </th>
            <th scope="col" class="px-6 py-3">
              <b>Criado por</b>
            </th>
            <th scope="col" class="px-6 py-3">
              <b>Inicio</b>
            </th>
            <th scope="col" class="px-6 py-3">
              <b>Fim</b>
            </th>
            <th scope="col" class="px-6 py-3">
              <b><span class="sr-only">Editar</span></b>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="exame in exams" :key="exame.id">
            <th
              scope="row"
              class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
            >
              {{ exame.titulo }}
            </th>
            <td class="px-6 py-4">
              {{ exame.professor }}
            </td>
            <td class="px-6 py-4">
              {{ exame.inicio }}
            </td>
            <td class="px-6 py-4">
              {{ exame.fim }}
            </td>
            <td class="px-6 py-4 text-right">
              <button
                @click="editarExame(exame.id)"
                class="font-medium text-blue-600 dark:text-blue-500 hover:underline"
              >
                Editar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style>
.wrapper {
  left: 0;
  right: 0;
  width: 80vw;
  display: flex;
  place-items: flex-start;
  flex-wrap: wrap;
  flex-direction: column;
}

.wrapper-headline {
  left: 0;
  right: 0;
}

#navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 999;
  min-width: 100vw;
}
</style>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'

// Configuração do axios para incluir cabeçalhos CORS
axios.defaults.baseURL = API_URL
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
axios.defaults.headers.common['Access-Control-Allow-Headers'] =
  'Origin, X-Requested-With, Content-Type, Accept'

export default {
  data() {
    return {
      exams: ''
    }
  },
  created() {
    this.verificarLogin()
    this.fetchExams()
  },
  mounted() {
    this.fetchExams()
  },
  methods: {
    onChangeTipo() {
      // Limpar campos extras quando o tipo é alterado
      this.camposExtras = []
    },
    async verificarLogin() {
      const token = localStorage.getItem('access_token')

      try {
        const response = await axios.get('/me', {
          headers: {
            Authorization: `Bearer ${token}` // Envie o token JWT no cabeçalho de autorização
          }
        })
        if (response.status !== 200) {
          this.$router.push('/')
        }
      } catch (error) {
        console.error('Error fetching questions:', error)
        this.$router.push('/')
      }
    },
    async fetchExams() {
      try {
        const response = await axios.get('/exame')
        console.log(response)
        this.exams = response.data
      } catch (error) {
        console.error('Error fetching questions:', error)
      }
    }
  }
}
</script>

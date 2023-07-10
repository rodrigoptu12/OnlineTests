<script setup>
import Navbar from '../components/Navbar.vue'
</script>

<template>
  <div class="w-full">
    <Navbar />
  </div>

  <div class="flex flex-wrap border border-white w-screen h-screen justify-center items-center">
    <div class="flex mb-6 flex-wrap">
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
          <!-- push exame/id -->
          <tr v-for="exame in exams" :key="exame.id">
            <button
              :key="exame.id"
              @click="$router.push(`/exam/${exame.id}`)"
              class="font-medium text-blue-600 dark:text-blue-500 hover:underline"
            >
              <th
                scope="row"
                class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
              >
                {{ exame.titulo }}
              </th>
            </button>
            <td class="px-6 py-4">
              {{ exame.professor }}
            </td>
            <td class="px-6 py-4">
              {{ exame.inicio }}
            </td>
            <td class="px-6 py-4">
              {{ exame.fim }}
            </td>
            <button
              @click="editarExame(exame.id)"
              class="font-medium text-blue-600 dark:text-blue-500 hover:underline"
            >
              <td class="px-6 py-4 text-right">Editar</td>
            </button>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style>
.prova-container {
  max-width: 600px;
  margin: 0 auto;
}

.prova-titulo {
  font-size: 24px;
  margin-bottom: 20px;
}

.questao {
  margin-bottom: 20px;
}

.questao-titulo {
  font-size: 18px;
  margin-bottom: 10px;
}

.opcoes-lista {
  list-style-type: none;
  padding: 0;
}

.opcao {
  margin-bottom: 5px;
}

.input-resposta {
  width: 100%;
  padding: 8px;
  font-size: 16px;
}

.botao-enviar {
  display: block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.botao-enviar:hover {
  background-color: #0056b3;
}

.wrapper {
  left: 0;
  right: 0;
  display: flex;
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

<script setup>
import Navbar from '../components/Navbar.vue'
</script>

<template>
  <div class="w-full">
    <Navbar />
  </div>
  <form @submit="enviarRespostas">
  <div class="flex justify-center items-center h-screen w-screen h width: 50vw; mg-0 pd-0">
    <div class="bg-white rounded-lg shadow-lg p-8 max-w-xl w-full custom-container">
      <h2 class="text-2xl font-bold mb-4 text-black">Exame</h2>
      <div v-for="questao in questoes" :key="questao.id" class="p-2 border m-5">
        <h3 class="text-black text-xl tracking-tighter font-bold">{{ questao.titulo }}</h3>
        <template v-if="questao.items.length > 0">
          <ul class="">
            <li v-for="opcao in questao.items" :key="opcao.id" class="opcao">
              <input
                type="radio"
                :name="`questao-${questao.id}`"
                :value="opcao.id"
                v-model="respostas[questao.id]"
                class="text-black"
              />
              <label class="text-black p-2">{{ opcao.text }}</label>
            </li>
          </ul>
        </template>
        <template v-else>
          <input
            class="text-black border p-2 rounded w-full"
            type="text"
            v-model="respostas[questao.id]"
          />
        </template>
      </div>
      <button type="submit"  class="bg-blue-500 text-white py-2 px-4 rounded">
        Enviar
      </button>
    </div>
  </div>
</form>
</template>

<style>
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
  name: 'examView',
  data() {
    return {
      questoes: [],
      respostas: {}
    }
  },
  created() {
    this.verificarLogin()
  },
  mounted() {
    this.fetchExam()
  },
  methods: {
    async verificarLogin() {
      const token = localStorage.getItem('access_token')

      try {
        const response = await axios.get('/me', {
          headers: {
            Authorization: `Bearer ${token}`
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

    async fetchExam() {
      let id = this.$route.params.id
      try {
        const response = await axios.get(`/exame/${id}`)
        if (response.status === 200) {
          this.questoes = response.data
          console.log(response.data)
        }
      } catch (error) {
        console.error('Error fetching questions:', error)
      }
    },

    enviarRespostas(event) {
        event.preventDefault();
      // const id_aluno = this.$route.params.id
      const id_aluno = this.$route.params.userId
      const id = this.$route.params.id
      const respostas = []
      for (const [key, value] of Object.entries(this.respostas)) {
        respostas.push({
          id: key,
          resposta: value
        })
      }
      console.log(respostas)
      const data = {
        id_aluno,
        id_exame: id,
        respostas
      }
      axios.post('/resposta', data)
        .then(response => {
          console.log(response)
          this.$router.push('/exams');
        })
        .catch(error => {
          console.log(error)
        });
        
    }
  }
}
</script>


  
  

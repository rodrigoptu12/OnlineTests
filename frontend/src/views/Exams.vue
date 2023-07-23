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
                <h1 class="mb-1 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
                    Exames.
                </h1>
                <p class="text-lg font-normal text-gray-500 lg:text-l dark:text-gray-400 mb-4">
                    Área de listagem de exames.
                </p>
                <div class="block w-full">
        </div>
            </div>
          
        </div>

        <div class="wrapper relative overflow-x-auto border dark:border-blue sm:rounded-l">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:transparent dark:text-gray-400">
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
                            <b>Nota</b>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <b><span class="sr-only">Editar</span></b>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="exame in exams" :key="exame.id">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white center-text">
                        {{ exame.titulo }}
                        </th>
                        <td class="px-6 py-4 center-text">
                        {{ exame.professor }}
                        </td>
                        <td class="px-6 py-4 center-text">
                        {{ formatarData(exame.inicio) }}
                        </td>
                        <td class="px-6 py-4 center-text">
                        {{ formatarData(exame.fim) }}
                        </td>
                        <td class="px-6 py-4 center-text" >
                          {{ notas[exame.id] }}
                        </td>
                        <td class="px-6 py-4 text-right">
                          <button v-if="isTeacher" @click="editarExame(exame.id)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</button>
                          <button v-else-if="podeFazerExame(exame)" @click="fazerExame(exame.id)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Responder</button>
                          <span v-else class="font-medium text-white-600 dark:text-white-500">{{ this.examMensagem }}</span>
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
import { format } from 'date-fns';

const API_URL = 'http://127.0.0.1:5000'

// Configuração do axios para incluir cabeçalhos CORS
axios.defaults.baseURL = API_URL
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
axios.defaults.headers.common['Access-Control-Allow-Headers'] =
  'Origin, X-Requested-With, Content-Type, Accept'

export default {
  name: 'examsView',
  data() {
    return {
      exams: '',
      isTeacher: false, 
      userId: '',
      examMensagem: '',
      alunosEncontrados: {},
      notas: {}
    }
  },
  created() {
    this.verificarLogin()
    this.fetchExams()
  },
  mounted() {
    this.fetchExams()

    const isTeacher = localStorage.getItem('isTeacher');
    this.isTeacher = isTeacher === 'true';

    const userId = localStorage.getItem('userId');
    this.userId = userId;
  },
  methods: {
    podeFazerExame(exame) {
      const dataHoraAtual = new Date();

      const dataInicioExame = new Date(exame.inicio);
      const dataFimExame = new Date(exame.fim);

      if (dataHoraAtual <= dataInicioExame) {
        this.examMensagem = 'Não aberto'
      }
      else if (dataHoraAtual >= dataFimExame) {
        this.examMensagem = 'Fechado'
      }
      if (this.alunosEncontrados[exame.id]) {
        this.examMensagem = 'Exame respondido'
      }

      return dataHoraAtual >= dataInicioExame && dataHoraAtual <= dataFimExame && !this.isTeacher && !this.alunosEncontrados[exame.id];
    },
    onChangeTipo() {
      this.camposExtras = []
    },
    fazerExame(id) {
      this.$router.push(`exam/${id}/${this.userId}`)
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
    formatarData(dateTimeStr) {
      const dateTime = new Date(dateTimeStr);
      return format(dateTime, 'dd/MM/yyyy HH:mm');
    },
    async fetchExams() {
      try {
        const response = await axios.get('/exame')
        this.exams = response.data

        for (const exame of this.exams) {
          if (!(exame.id in this.alunosEncontrados && this.alunosEncontrados[exame.id] !== undefined)) {
            try {
              const resposta = await axios.get(`/resposta/${exame.id}/${this.userId}`);
              this.alunosEncontrados[exame.id] =  resposta.data.resposta;
            } catch (error) {
              console.error('Erro ao buscar a resposta do exame: ', error);
            }
          }

          const dataHoraAtual = new Date();
          const dataFimExame = new Date(exame.fim);

          if (dataHoraAtual >= dataFimExame && this.alunosEncontrados[exame.id] && this.alunosEncontrados[exame.id] !== undefined && !(exame.id in this.notas && this.notas[exame.id] !== undefined)) {
            try {
              const resposta = await axios.get(`/resposta/nota/${exame.id}/${this.userId}`);

              this.notas[exame.id] = resposta.data.nota;
            
            } catch (error) {
              console.error('Erro ao buscar a resposta do exame: ', error);
            }
          }
          else {
            this.notas[exame.id] = "-";
          }
        }
      } catch (error) {
        console.error('Error fetching questions:', error)
      }
    }
  }
}
</script>

<script setup>
import Navbar from '../components/Navbar.vue'
import draggable from 'vuedraggable'
</script>

<template>
  <main id="wrapper">
    <Navbar id="navbar" />
    <div class="wrapper-headline flex flex-wrap -mx-3 mb-6">
      <div class="w-full px-3 mb-6 md:mb-0">
        <h1
          class="mb-1 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl"
        >
          Novo exame.
        </h1>
        <p class="text-lg font-normal text-gray-500 lg:text-l dark:text-gray-400 mb-4">
          Área de criação de exames.
        </p>
      </div>
    </div>
    <div class="w-full">
      <form class="w-full" @submit="createExam">
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3 mb-6 md:mb-0">
            <label
              class="block uppercase tracking-wide text-gray-700 dark:text-gray-200 text-xs font-bold mb-2"
              for="grid-command"
            >
              Título do exame
            </label>
            <input
              required
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:text-blue focus:outline-none focus:bg-transparent focus:border-blue"
              id="grid-command"
              type="text"
              placeholder="Digite aqui o título do exame..."
              v-model="titulo"
            />
          </div>
        </div>

        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3 mb-6 md:mb-0">
            <label
              class="block uppercase tracking-wide text-gray-700 dark:text-gray-200 text-xs font-bold mb-2"
              for="grid-command"
            >
              Início
            </label>
            <input
              required
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:text-blue focus:outline-none focus:bg-transparent focus:border-blue"
              id="grid-command"
              type="datetime-local"
              placeholder="Digite aqui o título do exame..."
              v-model="inicio"
            />
          </div>
        </div>

        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3 mb-6 md:mb-0">
            <label
              class="block uppercase tracking-wide text-gray-700 dark:text-gray-200 text-xs font-bold mb-2"
              for="grid-command"
            >
              Fim
            </label>
            <input
              required
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:text-blue focus:outline-none focus:bg-transparent focus:border-blue"
              id="grid-command"
              type="datetime-local"
              placeholder="Digite aqui o título do exame..."
              v-model="fim"
            />
          </div>
        </div>

        <div class="flex flex-wrap -mx-3 mb-8">
          <div class="w-full px-3 mb-6 md:mb-0">
            <label
              class="block uppercase tracking-wide text-gray-700 dark:text-gray-200 text-xs font-bold mb-2"
              for="grid-question-type"
            >
              Lista de questões
            </label>
            <div class="relative">
              <div class="mb-6">
                <select
                  required
                  v-model="selectedQuestion"
                  ref="selectedQuestion"
                  class="block appearance-none w-full bg-transparent border border-gray-200 text-grey py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
                  id="grid-question-type"
                >
                  <option value="" disabled selected hidden>Selecione uma questão...</option>
                  <option v-for="question in questions" :value="question" :key="question.id">{{ question.command }}</option>
                </select>
                <!--<div
                  class="pointer-events-none absolute inset-y-0 right-0 flex items-center mt-3 mb-6 px-2 text-gray-700">
                  <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                    <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                  </svg>
                </div>-->
              </div>

              <div class="form-group mt-8">
                <a
                  class="bg-grey mb-6 text-white outline-none w-1/3 border border-gray-200 rounded py-3 px-4 focus:outline-none"
                  @click="incluirQuestao"
                  >Incluir questão</a
                >
                <!--<button class="btn btn-secondary" @click="replace">Replace</button>-->
              </div>
            </div>
          </div>
        </div>

        <div class="w-full mt-6">
          <div class="flex items-center pl-4 border border-gray-200 rounded dark:border-gray-700">
            <input
              v-model="enabled"
              id="disabled"
              checked
              type="checkbox"
              value=""
              name="bordered-checkbox"
              class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
            />
            <label
              for="bordered-checkbox-2"
              class="w-full py-4 ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
              >Ativar ordenação de questões</label
            >
          </div>
          <div class="w-full width-full flex mt-6 mb-6">
            <h3>{{ draggingInfo }}</h3>

            <draggable
              :list="list"
              :disabled="!enabled"
              item-key="id"
              class="list-group"
              ghost-class="ghost"
              :move="checkMove"
              @start="dragging = true"
              @end="dragging = false"
            >
              <template #item="{ element, index }">
                <ul class="w-full text-left text-gray-500 dark:text-gray-400">
                  <li class="flex items-center space-x-6 mb-3">
                    <svg
                      class="flex-shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400"
                      aria-hidden="true"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 16 12"
                    >
                      <path
                        stroke="currentColor"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M1 5.917 5.724 10.5 15 1.5"
                      />
                    </svg>
                    <span class="list-group-item" :class="{ 'not-draggable': !enabled }"
                      ><b>{{ element.name }}</b></span
                    >
                    <span py-8 px-4 mb-3>Valor atribuído a questão: </span>
                    <input
                      class="appearance-none bg-transparent border border-gray-200 focus:border-blue p-3"
                      type="number"
                      min="0"
                      v-model="element.pontuacao"
                    />
                    <button @click="removerQuestao(index)">Remover</button>
                  </li>
                </ul>
              </template>
            </draggable>
          </div>

          <rawDisplayer class="bg-red" :value="list" title="List" />
        </div>

        <button
          type="submit"
          class="bg-blue text-white outline-none mb-6 border-none block w-1/2 border border-gray-200 rounded py-3 px-4 focus:outline-none focus:text-blue"
        >
          Cadastrar exame
        </button>
      </form>
    </div>
  </main>
</template>

<style scoped>
#wrapper {
  display: flex;
  place-items: flex-start;
  flex-wrap: wrap;
  flex-direction: column;
  width: 30rem;
}

#navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 999;
}

.wrapper-headline {
  margin-top: calc(60px + 4rem);
}

#drag {
  z-index: 0;
  background-color: red;
}

.buttons {
  margin-top: 35px;
}

.not-draggable {
  cursor: no-drop;
}

.width-full {
  width: 70rem;
}
</style>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

// Configuração do axios para incluir cabeçalhos CORS
axios.defaults.baseURL = API_URL;
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
axios.defaults.headers.common['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept';

export default {
  data() {
    return {
      gridItemsText: '',
      camposExtras: [],
      enabled: true,
      list: [],
      questoes_ids: [],
      dragging: false,
      novaQuestaoText: '',
      selectedQuestion: '',
      questions: [],
      titulo: '',
      inicio: '',
      fim: ''
    }
  },
  mounted() {
    this.fetchQuestions();
  },
  created() {
      this.verificarLogin();
  },
  methods: {
    handleChange() {},
    
     async verificarLogin() {
      const token = localStorage.getItem('access_token');
      
      try {
        const response = await axios.get('/me', {
      headers: {
        Authorization: `Bearer ${token}`  // Envie o token JWT no cabeçalho de autorização
        }});
        if (response.status !== 200) {
      this.$router.push('/');
      }
      } catch (error) {
        console.error('Error fetching questions:', error);
        this.$router.push('/');
      }

  },
    incluirQuestao() {
      if (this.selectedQuestion) {
        const valorSelecionado = this.selectedQuestion
        const novaQuestao = {
          name: valorSelecionado.command,
          pontuacao: 0 // Valor inicial da pontuação
        }
        console.log(this.selectedQuestion)
        this.list.push(novaQuestao)
        this.questoes_ids.push(valorSelecionado.id)
      }
    },
    removerQuestao(index) {
      this.list.splice(index, 1)
    },

    checkMove: function (e) {
      window.console.log('Future index: ' + e.draggedContext.futureIndex)
    },
    async fetchQuestions() {
      try {
        const response = await axios.get('/questions');
        this.questions = response.data;
      } catch (error) {
        console.error('Error fetching questions:', error);
      }
  },
  createExam(event) {
      event.preventDefault();

        const data = {
          titulo: this.titulo,
          professor_id: 1,
          inicio: this.inicio,
          fim: this.fim,
          questoes: this.questoes_ids,
          estado: 'agendado'
        };
      
      console.log(data);

      axios.post('/exame', data)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        });

      this.$router.push('/new-exam');

    }
  },

  components: {
    draggable
  }
}
</script>

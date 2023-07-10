<script setup>
import Navbar from '../components/Navbar.vue'
</script>

<template>
  <main id="wrapper">
    <Navbar id="navbar" />
    <div class="wrapper-headline flex flex-wrap -mx-3 mb-6">
      <div class="w-full px-3 mb-6 md:mb-0">
        <h1
          class="mb-1 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl"
        >
          Nova Questão.
        </h1>
        <p class="text-lg font-normal text-gray-500 lg:text-l dark:text-gray-400 mb-4">
          Área de criação de questões.
        </p>
      </div>
    </div>
    <div>
      <form class="w-full max-w-lg" @submit="createQuestion">
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3 mb-6 md:mb-0">
            <label
              class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="grid-command"
            >
              Comando da questão
            </label>
            <input
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:text-blue focus:outline-none focus:bg-transparent focus:border-blue"
              id="grid-command"
              type="text"
              placeholder="Digite aqui o comando da questão..."
              v-model="command"
            />
            <!--<p class="text-red-500 text-xs italic">Por favor, preencha este campo.</p>-->
          </div>
          <div class="w-full px-3">
            <label
              class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="grid-answer-key"
            >
              Chave da resposta
            </label>
            <input
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
              id="grid-answer-key"
              type="text"
              placeholder="Digite aqui a chave resposta da questão..."
              v-model="answer_key"
            />
          </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-8">
          <div class="w-full px-3 mb-6 md:mb-0">
            <label
              class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="grid-question-type"
            >
              Tipo da questão
            </label>
            <div class="relative">
              <select
                v-model="selectedTipo"
                @change="onChangeTipo"
                class="block appearance-none w-full bg-transparent border border-gray-200 text-grey py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
                id="grid-question-type"
              >
                <option value="" disabled selected hidden>Selecione uma opção...</option>
                <option value="m_e">Múltipla escolha</option>
                <option value="r_t_v_n">Com resposta to tipo valor numérico</option>
                <option value="v_f">Verdadeiro ou falso</option>
              </select>
              <div
                class="pointer-events-none absolute inset-y-0 right-0 flex items-center mt-3 px-2 text-gray-700"
              >
                <svg
                  class="fill-current h-4 w-4"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                  />
                </svg>
              </div>
            </div>
          </div>
        </div>

        <div class="flex flex-wrap -mx-3 mb-6">
          <div v-if="selectedTipo === 'm_e'" class="w-full px-3">
            <button class="bg-grey mb-6 text-white outline-none block w-1/2 border border-gray-200 rounded py-3 px-4 focus:outline-none" @click="adicionarInput">Adicionar alternativa</button>
            <div>
              <div v-for="(input, index) in inputs" :key="index">
                <input class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue" v-model="input.text" type="text">
                <button @click="removerInput(index)">Remover</button>
              </div>
            </div>
          </div>

          <div v-if="selectedTipo === 'v_f'" class="w-full px-3">
            <div>
                <input class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"  type="text" v-model="response1">

                <input class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"  type="text" v-model="response2">
            </div>
          </div>
        </div>
        <div class="class">
          <button type="submit" class="bg-blue text-white outline-none border-none block w-1/2 border border-gray-200 rounded py-3 px-4 focus:outline-none focus:text-blue">
            Cadastrar questão
          </button>
        </div>
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
.select-placeholder {
  color: #999999;
  font-style: italic;
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
      selectedTipo: '',
      gridItemsText: '',
      campo2: '',
      campo3: '',
      camposExtras: [],
      inputs: [],
      command: '',
      answer_key: '',
      response1: '',
      response2: ''
    }
  },
  created() {
    this.verificarLogin();
  },
  methods: {
    onChangeTipo() {
      // Limpar campos extras quando o tipo é alterado
      this.camposExtras = []
    },
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
    adicionarCampo() {
      // Adicionar um novo campo extra
      this.camposExtras.push({
        tipo: 'text',
        valor: '',
        inputs: [],
      })
    },
    removerCampo(index) {
      // Remover o campo extra com o índice especificado
      this.camposExtras.splice(index, 1)
    },
    handleChange() {},
    adicionarInput() {
      event.preventDefault();
      this.inputs.push({ text: '' });
    },
    removerInput(index) {
      event.preventDefault();
      this.inputs.splice(index, 1);
    },
    createQuestion(event) {
      event.preventDefault();

      let data;

      if (this.response1) {
        data = {
          command: this.command,
          answer_key: this.answer_key,
          question_type: this.selectedTipo,
          items: [{'text': this.response1}, {'text': this.response2}]
        };
      }

      else if (this.inputs){
        data = {
          command: this.command,
          answer_key: this.answer_key,
          question_type: this.selectedTipo,
          items: this.inputs
        };
      }
      else {
      data = {
        command: this.command,
        answer_key: this.answer_key,
        question_type: this.selectedTipo,
      };
    }
      console.log(data.items);

      axios.post('/questions', data)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        });
        this.$router.push('/new-question');
    }
  }
}
</script>

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
        <hr />
      </div>
    </div>
    <div>
      <form class="w-full max-w-lg">
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3 mb-6 md:mb-0">
            <label
              class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="grid-command"
            >
              Comando da questão
            </label>
            <input
              class="appearance-none block w-full bg-transparent text-grey border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:text-blue focus:outline-none focus:bg-transparent focus:border-blue"
              id="grid-command"
              type="text"
              placeholder="Command here..."
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
              placeholder="Answer key here..."
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
            <label
              class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="grid-items-text"
            >
              Texto do item
            </label>
            <input
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
              id="grid-items-text"
              type="text"
              placeholder="Item text here..."
              v-model="gridItemsText"
            />
          </div>
        </div>

        <div class="flex flex-wrap -mx-3 mb-6">
          <div v-if="selectedTipo === 'm_e'" class="w-full px-3">
            <button
              type="button"
              @click="adicionarCampo"
              class="bg-grey mb-6 text-white outline-none block w-1/2 border border-gray-200 rounded py-3 px-4 focus:outline-none"
            >
              Adicionar texto de item
            </button>
            <div v-for="(campo, index) in camposExtras" :key="index">
              <label
                :for="'campoExtra' + index"
                class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                >Texto do item {{ index + 1 }}</label
              >
              <div class="flex">
              <input
                :type="campo.tipo"
                :value="campo.valor"
                :id="'campoExtra' + index"
                class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
                placeholder="Item text here..."
                v-model="gridItemsText"
              />
              <button @click="removerCampo(index)" class=" ml-6 pb-3 outline-none text-grey">Remover</button>
            </div>
            </div>
          </div>
        </div>
        <div class="class">
          <button type="button" class="bg-blue text-white outline-none border-none block w-1/2 border border-gray-200 rounded py-3 px-4 focus:outline-none focus:text-blue">
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
export default {
  data() {
    return {
      selectedTipo: '',
      gridItemsText: '',
      campo2: '',
      campo3: '',
      camposExtras: []
    }
  },
  methods: {
    onChangeTipo() {
      // Limpar campos extras quando o tipo é alterado
      this.camposExtras = []
    },
    adicionarCampo() {
      // Adicionar um novo campo extra
      this.camposExtras.push({
        tipo: 'text',
        valor: ''
      })
    },
    removerCampo(index) {
      // Remover o campo extra com o índice especificado
      this.camposExtras.splice(index, 1)
    },
    handleChange() {}
  }
}
</script>

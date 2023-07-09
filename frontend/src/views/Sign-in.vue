<template>
  <div class="wrapper">
    <div v-if="showSignup">
      <div class="signup w-full">
        <div class="w-full mb-6 md:mb-0">
          <h1
            class="mb-1 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl"
          >
            Nova conta
          </h1>
          <p class="text-lg font-normal text-gray-500 lg:text-l dark:text-gray-400 mb-4">
            Formulário de cadastro de nova conta.
          </p>
        </div>
        <form>
          <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Seu email:</label
            >
            <input
              type="email"
              id="email"
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
              placeholder="seu-email@exemplo.com..."
              required
            />
          </div>
          <div class="mb-6">
            <label
              for="password"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Sua senha:</label
            >
            <input
              type="password"
              id="password"
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
              placeholder="Digite aqui a sua senha..."
              required
            />
          </div>
          <div class="mb-6">
            <label
              for="repeat-password"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Repita a sua senha:</label
            >
            <input
              type="password"
              id="repeat-password"
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
              placeholder="Repita a sua senha..."
              required
            />
          </div>
          <button
            type="submit"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:blue-300 font-medium rounded text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Criar nova conta
          </button>
        </form>
        <div class="mt-5">
          <a href="#" @click="toggleForm">Já possuo uma conta, desejo entrar.</a>
        </div>
      </div>
    </div>

    <div v-else>
      <div class="signup">
        <div class="w-full">
          <div class="w-full mb-6 md:mb-0">
            <h1
              class="mb-1 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl"
            >
              Login
            </h1>
            <p class="text-lg font-normal text-gray-500 lg:text-l dark:text-gray-400 mb-4">
              Insira suas credenciais e acesse a sua conta.
            </p>
          </div>
          <form>
            <div class="mb-6">
              <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Seu email:</label
              >
              <input
                type="email"
                id="email"
                class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
                placeholder="seu-email@exemplo.com..."
                required
              />
            </div>
            <div class="mb-6">
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Sua senha:</label
              >
              <input
                type="password"
                id="password"
                class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
                placeholder="Digite aqui a sua senha..."
                required
              />
            </div>
            <button
              type="submit"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:blue-300 font-medium rounded text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Acessar
            </button>
          </form>

          <div class="mt-5">
            <a href="#" @click="toggleForm">Ainda não possuo uma conta, desejo me cadastrar.</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.wrapper {
  display: flex;
  place-items: flex-start;
  flex-wrap: wrap;
  flex-direction: column;
  width: 30rem;
  margin-right: -11rem;
}
.signup {
  width: 30rem;
}
</style>

<script>
export default {
  data() {
    return {
      showSignup: false
    }
  },
  methods: {
    toggleForm() {
      this.showSignup = !this.showSignup
    }
  }
}
</script>

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
        <form @submit="createUser">
          <div class="mb-6">
            <label
              for="repeat-password"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Nome:</label
            >
            <input
              id="repeat-password"
              v-model="name"
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
              placeholder="Repita a sua senha..."
              required
            />
          </div>
          <div class="mb-6">
            <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Seu email:</label
            >
            <input
              type="email"
              id="email"
              v-model="email"
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
              v-model="password"
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
              v-model="confirm_password"
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
              placeholder="Repita a sua senha..."
              required
            />
          </div>
          <div class="mb-6">
            <label
              for="repeat-password"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Matrícula:</label
            >
            <input
              type="number"
              id="repeat-password"
              v-model="registration"
              class="appearance-none block w-full bg-transparent text-grey border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-transparent focus:text-blue focus:border-blue"
              placeholder="Repita a sua senha..."
              required
            />
          </div>
          <div class="mb-6">
            <input
              type="checkbox"
              id="isTeacher"
              v-model="isTeacher"
              class="mr-2"
            />
            <label for="isTeacher" class="text-sm text-gray-900 dark:text-white">
              É professor?
            </label>
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
          <form @submit="login">
            <div class="mb-6">
              <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Seu email:</label
              >
              <input
                type="email"
                id="email"
                v-model="email"
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
                v-model="password"
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
import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

// Configuração do axios para incluir cabeçalhos CORS
axios.defaults.baseURL = API_URL;
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
axios.defaults.headers.common['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept';

export default {
  data() {
    return {
      showSignup: false,
      email: '',
      password: '',
      confirm_password: '',
      registration: '',
      name: '',
      isTeacher: false
    }
  },
  methods: {
    toggleForm() {
      this.showSignup = !this.showSignup
    },
    login(event) {
      event.preventDefault();

      const data = {
        email: this.email,
        password: this.password
      };

      axios.post('/login', data)
        .then(response => {
          console.log(response)
          if (response.status === 200) {
            localStorage.setItem('access_token', response.data.access_token);
            this.$router.push('/new-question');
          }
        })
        .catch(error => {
          console.log(error)
        });
    },
    createUser(event) {
      event.preventDefault();

      const data = {
        email: this.email,
        password: this.password,
        confirm_password: this.confirm_password,
        registration: this.registration,
        name: this.name,
        isTeacher: this.isTeacher
      };

      axios.post('/users', data)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        });
    }
  }
}
</script>

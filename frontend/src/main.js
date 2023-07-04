import './assets/main.css'

import { createApp } from 'vue'
import { plugin, defaultConfig } from '@formkit/vue'

import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import "@/assets/styles/main.css";

const app = createApp(App).use(plugin, defaultConfig)

app.use(createPinia())
app.use(router)

app.mount('#app')

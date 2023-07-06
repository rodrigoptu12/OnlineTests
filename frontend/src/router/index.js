import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signin',
      name: 'signin',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Sign-in.vue')
    },
    {
      path: '/new-question',
      name: 'questionform',
      component: () => import('../views/QuestionForm.vue')
    },
    {
      path: '/new-exam',
      name: 'examform',
      component: () => import('../views/ExamForm.vue')
    }
  ]
})

export default router

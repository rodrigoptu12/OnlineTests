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
      name: 'newquestion',
      component: () => import('../views/NewQuestion.vue')
    },
    {
      path: '/new-exam',
      name: 'newexam',
      component: () => import('../views/NewExam.vue')
    },
    {
      path: '/exams',
      name: 'exams',
      component: () => import('../views/Exams.vue')
    },
    {
      path: '/exam',
      name: 'exam',
      component: () => import('../views/Exam.vue')
    }
  ]
})

export default router

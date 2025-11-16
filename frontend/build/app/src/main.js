import './assets/styles/main.scss'
import { createWebHistory, createRouter } from 'vue-router'
import { createApp } from 'vue'
import App from './App.vue'
import Home from './Views/Home.vue'
import Organizations from './Views/Organizations.vue'
import About from './Views/About.vue'

const app = createApp(App)

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/organizations', name: 'organizations', component: Organizations },
  { path: '/about', name: 'about', component: About },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  },
})

app.use(router)
app.mount('#app')

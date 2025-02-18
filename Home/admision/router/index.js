import Vue from 'vue';
import Router from 'vue-router';
import Login from '@/components/Login.vue';
import Admisiones from '@/components/Admisiones.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/admisiones',
      name: 'Admisiones',
      component: Admisiones
    }
  ]
});

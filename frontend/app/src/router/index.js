import Vue from 'vue'
import Router from 'vue-router'
import HomeMenu from "@/components/HomeMenu";
import Login from "@/components/Login"
import ListenAllPokemon from "@/components/ListenAllPokemon";
import AdminMenuPokemon from "@/components/AdminMenuPokemon";
import AdminMenu from "@/components/AdminMenu";


Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes:[
            {
                path: '/',
                component: HomeMenu
            },
            {
                path: '/login',
                component: Login
            },
            {
                path: '/menuadmin',
                component: AdminMenu
            },
            {
                path: '/menupokemon',
                component: ListenAllPokemon
            },
            {
                path: '/menuadminpokemon',
                component: AdminMenuPokemon
            }
           ]
})

//             {
//                 path: '/menutreinador',
//                 component:
//             },
//             {
//                 path: '/menuadmintreinador',
//                 component:
//             }

export default router
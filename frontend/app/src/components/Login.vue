<template>
  <!-- Wrapper -->
			<div>

					<!-- Header -->
					<header>

						<!-- Menu -->
						<div>

							<!-- Logo -->
							<a href="/" class="logo">
								<span><img src="../images/Articuno.png" width="100px"/></span>
							</a>
							<label class="logotext">Interface Web - Admin </label>
						</div>
					</header>


				<!-- Main -->
					<div>
						<div>
								<h1 id="validar"></h1>
								<label>Informe seu login</label>
                <br>
								<input v-model="admin.username" type="text" placeholder="Username ou Email" name="username" id="username">
								<input v-model="admin.password" type="password" placeholder="Senha" name="password" id="password">

                <button type="submit" @click="loginAdministrator" >Login</button>
						</div>
					</div>

				<!-- Footer -->
					<footer id="footermenu">
						<div>
							<section>
								<br>
								<h6>Renan Berti Ribas</h6>
								<h2>Follow</h2>
								<li class="follow">
									<a href="https://github.com/Renanrbsc">GitHub</a>
								</li>
							</section>
						</div>
					</footer>
			</div>
</template>


<script>
import AdminLogin from '../services/admin_login'

export default {
    name: 'Login',
    data(){
    return{
      admin:{
        username:'',
        password:''
      },
      message:{content:'', type:''}
    }
  },
    methods:{
      loginAdministrator(){
        AdminLogin.login(this.admin).then(response => {
          console.log(response)
          if (response.data.access_token){
            this.$router.push({path: 'menuadmin/'})
          }
          else{
            this.message.content = "Incorrect credentials!"
            this.message.type = "alert alert-danger"
          }
        })
      }
    }
}
</script>



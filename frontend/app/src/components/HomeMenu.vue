<template>
  <div>

					<!-- Header -->
					<header>

						<!-- Menu -->
						<ul >
							<li class="menu"><a href="/login">Login Administrador</a></li>

						</ul>

						<div>

							<!-- Logo -->
							<a href="/" class="logo">
								<span><img src="../images/Articuno.png" width="100px"/></span>
							</a>
							<label class="logotext">Interface Web Pokemon</label>
						</div>
					</header>


				<!-- Main -->

					<div>
						<a href="/menupokemon" class="grademenu" id="opcao1">
									<div>
										<img class="imagemenu" src="../images/pokemon_menu.png" width="100px" />
									</div>
									<h2 >Pokemon Menu</h2>
						</a>

						<a href="/menutreinador" class="grademenu" id="opcao2">
									<div>
										<img class="imagemenu" src="../images/treinador_menu.png" width="100px" />
									</div>
									<h2 >Treinador Menu</h2>
						</a>
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
export default {
  name: 'HomeMenu'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

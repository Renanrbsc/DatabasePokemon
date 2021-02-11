<template>
  <!-- Wrapper -->
			<div>

					<!-- Header -->
					<header>

						<!-- Menu -->
						<ul >
							<li class="menu"><a href="/sair">Sair </a></li>

						</ul>

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
							<form>
								<h1 id="validar"></h1>
								<label>Menu Pokemon admin</label><br><br>
								<a href="/menuadminpokemon" class="grademenu">
									<div>
										<img class="imagemenuadmin" src="../images/pokemon_menu.png"/>
									</div>
									<h2 >Pokemon Menu</h2>
								</a>

								<a href="/menuadmintreinador" class="grademenu">
									<div>
										<img class="imagemenuadmin" src="../images/treinador_menu.png"/>
									</div>
									<h2 >Treinador Menu</h2>
								</a>
							</form>
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
export default {
  name: 'AdminMenu'
}
</script>

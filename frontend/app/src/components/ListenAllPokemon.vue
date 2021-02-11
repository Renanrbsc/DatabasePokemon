<template>
  <!-- Wrapper -->
			<div>
					<!-- Header -->
					<header>

						<!-- Menu -->
						<ul >
							<li class="menu"><a href="/menuadmin">Login Administrador</a></li>

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
					<div align="center">
						<div>
							<ul>
                <div v-for="i in lista" :key="i">
									<div class="grade">
											<div class="imagelistar" v-bind:style="{'background-image': 'url(../images/' + i[1] + '.png)'}">
												<div class="texto">
													<h2>Informação
													</h2>
													<h3>
														ID Pokedex: i[0]<br>
														Nome: i[1]<br>
														Tipo: i[2]<br>
														Altura: i[3] m<br>
														Peso: i[4] kg<br>
														Categoria: i[5]<br>
														Habilidade: i[6]<br>
														Habilidade2: i[7]<br>
														Fraqueza: i[8]<br>
														Fraqueza2: i[9]<br>
														Descrição: i[10]
													</h3>
												</div>
											</div>
										<h2>i[1]</h2>
									</div>
								</div>
							</ul>
						</div>
					</div>

				<!-- Footer -->
					<footer>
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
  name: 'ListenAllPokemon'
}
</script>

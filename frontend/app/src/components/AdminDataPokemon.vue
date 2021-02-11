<template>
  <!-- Wrapper -->
			<div>

					<!-- Header -->
					<header>

						<!-- Menu -->
						<ul >
							<li class="menu"><a href="/sair">Sair </a></li>
							<li class="menu"><a href="/menuadmin">Menu Admin</a></li>

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
					<div align="center">
						<div>
							<form action="/menuadmin/adicionarpokemon">
								<h1 id="validar"></h1>
								<label>Menu Pokemon admin</label><br><br>
								<label>Adicionar/Editar</label><br><br>

								<input type="text" placeholder="Nome" name="nome">
								<input type="text" placeholder="Tipo" name="tipo">
								<input type="text" placeholder="Altura" name="altura">
								<input type="text" placeholder="Peso" name="peso">
								<input type="text" placeholder="Categoria" name="categoria">
								<input type="text" placeholder="Habilidade" name="habilidade">
								<input type="text" placeholder="Habilidade2" name="habilidade2">
								<input type="text" placeholder="Fraqueza" name="fraqueza">
								<input type="text" placeholder="Fraqueza2" name="fraqueza2">
								<textarea placeholder="Descricao" name="descricao"></textarea>

								<input type="submit" value="Enviar">

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
  name: 'AdminDataPokemon'
}
</script>

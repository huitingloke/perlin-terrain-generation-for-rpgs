<html>
	<body>
	<h1>Perlin File Terrain Generation For RPGs</h1>
	<h2>What does this do?</h2>
	<p>Hi, thanks for coming to this project! You can create a map and many submaps of each pixel on said map using a few methods! This was made as a personal project for a Discord bot that I forgot to work on, but this can just be a personal project now anyway. Hope you find this little library useful! (I guess it's the first thing I'm really developing, so please be patient and have low expectations if you would)</p>
	<h2>Current features (methods, I guess)</h2>
	<img src="" />
	<p><i>Take this very settling image and be done with it, thank you!</i></p>
		<table border="1">
			<thead>
				<th>Features</th>
				<th>Explanation</th>
			</thead>
			<tbody>
				<tr>
					<td><code>createPerlin(octaves, seed)</code></td>
					<td>Create a perlin noise texture (credit to the pip installation guide for the actual code here!)</td>
				</tr>
				<tr>
					<td><code>createVisualizationFile(file, multiplier)`</code></td>
					<td>Individually view the rows and columns of each Perlin generation. Multiplier is 200 by default.</td>
				</tr>
				<tr>
					<td><code>createTerrainFile(file)</code></td>
					<td>Creates the actual terrain file with pregenerated terrain types that I was using. Just go into the code and change it, but by default, there are 3 types of terrain as of now
					<table border="1">
						<thead>
							<th>Alias</th>
							<th>Explanation</th>
						</thead>
						<tbody>
							<tr>
								<td><strong>W</strong></td>
								<td>Water</td>
							</tr>
							<tr>
								<td><strong>T</strong></td>
								<td>Trees/Forest</td>
							</tr>
							<tr>
								<td><strong>G</strong></td>
								<td>Ground</td>
							</tr>
						</tbody>
					</table>
					</td>
				</tr>
			</tbody>
		</table>

	<h2>Future features that could be implemented (no promises)</h2>
	<ul>
		<li>Fixing the terrain generation to include more types of terrain</li>
		<li>More customization</li>
		<ul>
			<li>Choosing your own terrains</li>
			<li>Making every single coordinate have its own little explorable area (definitely need to map things out well)</li>
		</ul>
		<li>Putting this onto Github or maybe even <code>pip install</code>!</li>
	</ul>

	<h2>Credits to...</h2>
	<ul>
		<li><a href="https://www.github.com/huitingloke">Perlin Noise</a> - Doing the Perlin Math generation</li>
		<li><a href="https://www.github.com/huitingloke">Beth</a> - Developing the terrain generation</li>
		<li><a href="https://www.github.com/JustinCMH555">Justin</a> - Mentally stable tech support</li>
	</ul>

	<h2>Frequentky Asked Questions (FAQ)</h2>
	<p><i>Please don't ask me questions because I am scared of everyone</i></p>
	</body>
</html>

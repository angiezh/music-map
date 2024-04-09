<script lang="ts">
	import { infoOverlayVisible } from '../stores';
	import CloseButton from './CloseButton.svelte';
	import ActionButton from './ActionButton.svelte';

	function closeInfoOverlay() {
		infoOverlayVisible.update(() => false);
	}
</script>

<aside class="overlay overlay--info">
	<CloseButton functionOnClick={closeInfoOverlay}>close info overlay</CloseButton>
	<div class="overlay__outer">
		<div class="overlay__content">
			<section>
				<h2>About</h2>

				<div class="overlay__section-text">
					<p>
						<i>Music Map</i> is a community resource dedicated to giving people a social space to share music related to places that might feel special to them, and the stories they have with their favourite music.
					</p>
					<p>
						Click anywhere in the map to drop a music note, or click on a music note to get started. From there, you can see in the side bar the feed of music people may have posted in that area. You can also click “add song” to create your own post.
					</p>
				</div>
			</section>
		</div>
	</div>
</aside>

<style>
	.overlay {
		height: 100%;
		position: fixed;
		z-index: var(--overlay-z-index);
		top: 0;
		background-color: var(--color-pink);
		overflow-x: hidden;
	}

	.overlay__outer {
		width: 0;
		padding: 2em;
	}

	section {
		margin-top: 2em;
	}

	section:first-child {
		margin-top: -1.2em;
	}

	h2 {
		text-decoration: none;
		font-size: 1.2rem;
		color: var(--color-dark);
		display: block;
		font-weight: bold;
		text-transform: uppercase;
		padding-bottom: 4px;
		border-bottom: 2px solid var(--color-dark);
	}

	@media (min-width: 800px) {
		h2 {
			font-size: 1.4rem;
		}
	}

	.overlay__section-text {
		text-decoration: none;
		color: var(--color-dark);
		display: block;
		margin-top: 1em;
		font-size: 1.1rem;
	}

	.overlay__section-text > *:first-child {
		margin-top: 0;
	}

	.overlay__section-text > *:last-child {
		margin-bottom: 0;
	}

	a {
		text-decoration: underline;
		text-decoration-color: var(--color-pink-bright);
		color: var(--color-dark);
	}

	a:not(.closebtn):hover,
	a:not(.closebtn):focus {
		color: var(--color-pink-bright);
	}

	.overlay--info {
		left: 0;
	}

	@media (min-width: 800px) {
		.overlay__outer {
			width: calc(40vw - 2px);
		}

		.overlay--info {
			left: -2px;
			border-right: var(--color-dark) solid 2px;
			box-shadow: 4px 0px 6px 0px rgba(0, 0, 0, 0.5);
		}

		.overlay__content {
			margin: 0;
			height: 125%;
		}
	}
</style>

<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

	function handleClick() {
		dispatch('click');
	}
</script>

<div class="button-wrapper">
	<!-- Use an onClick handler instead of link -->
	<button class="button" on:click={handleClick}>
		<slot />
	</button>
</div>

<style>
	.button {
		display: inline-block;
		border: 2px solid var(--color-dark);
		background: var(--color-pink-bright);
		color: var(--color-pink-bright);
		box-shadow: 0 0 5px -1px rgba(0, 0, 0, 0.2);
		border-radius: 25px;
		cursor: pointer;
		padding: 5px 20px;
		text-align: center;
		font-size: 18px;
		color: var(--color-dark);
		text-transform: uppercase;
		text-decoration: none;
		transition-property: color, border-color, background-color;
		transition-duration: 300ms;
		transition-timing-function: ease;
	}

	.button:hover,
	.button:focus {
		color: var(--color-pink-bright);
		border: 2px solid var(--color-pink-bright);
		background: var(--color-dark);
		text-decoration: none;
	}

	.button-wrapper {
		text-align: center;
		margin-top: 1rem;
	}
</style>

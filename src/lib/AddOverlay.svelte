<script lang="ts">
	import {
		addOverlayVisible,
		filteredDataStore,
		descriptionDataStore,
		fullDataStore
	} from '../stores';
	import ActionButton from './ActionButton.svelte';
	import CloseButton from './CloseButton.svelte';

	function closeAddOverlay() {
		addOverlayVisible.update(() => false);
	}

	// Assuming moments is already defined and loaded with your JSON data
	let description = ''; // For binding to your textarea
	let song = '';

	async function addMoment() {

		// Assuming coordinates are obtained dynamically, for now they are hard-coded
		const coordinates = [-117.71319812050054, 34.11885457669316];

		// Construct the new moment data
		const newMomentData = {
			id: Date.now(),
			song: song,
			description: description,
			coordinates: coordinates
		};

		try {
            const response = await fetch('http://127.0.0.1:5000/moments', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newMomentData)
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            console.log('Success:', result);
            closeAddOverlay(); // close the overlay on success
        } catch (error) {
            console.error('Error:', error);
        }
	}
	


		


		// // adding data to the filtered_data_id_only.json
		// filteredDataStore.update((currentData) => {
		// 	const newFeature = {
		// 		type: 'Feature',
		// 		properties: { id: currentData.features.length + 1 },
		// 		geometry: {
		// 			type: 'Point',
		// 			coordinates: [-117.71319812050054, 34.11885457669316]
		// 		}
		// 	};
		// 	return { ...currentData, features: [...currentData.features, newFeature] };
		// });

		// // adding description pair to the id_description_pairs.json
		// descriptionDataStore.update((currentDescriptions) => {
		// 	const newDescriptionPair = {
		// 		id: currentDescriptions.length + 1,
		// 		song: song,
		// 		description: description
		// 	};
		// 	return [...currentDescriptions, newDescriptionPair];
		// });

		// // adding full data to filtered_data.json
		// fullDataStore.update((currentData) => {
		// 	const newData = {
		// 		type: 'Feature',
		// 		properties: { id: currentData.features.length + 1, song: song, description: description },
		// 		geometry: {
		// 			type: 'Point',
		// 			coordinates: [-117.71319812050054, 34.11885457669316]
		// 		}
		// 	};
		// 	return { ...currentData, features: [...currentData.features, newData] };
		// });

		// // print out updated
		// const unsubscribe1 = fullDataStore.subscribe((updatedItems) => {
		// 	console.log('Updated store items:', updatedItems);
		// });
		// unsubscribe1();

		// const unsubscribe2 = descriptionDataStore.subscribe((updatedItems) => {
		// 	console.log('Updated store items:', updatedItems);
		// });
		// unsubscribe2();
		// description = ''; // Reset the description for next input
		// song = '';
</script>

<aside class="overlay overlay--add">
	<div class="action-button-container">
		<CloseButton functionOnClick={closeAddOverlay} position="right">close add overlay</CloseButton>
	</div>
	<div class="overlay__outer">
		<div class="overlay__content">
			<section>
				<div class="overlay__section-text">What song connects you to this location?</div>

				<textarea bind:value={song} class="songform"></textarea>

				<div class="overlay__section-text">
					Write a note (optional)
					<textarea bind:value={description} class="subform"></textarea>
					<ActionButton on:click={addMoment}>Add</ActionButton>
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
		width: calc(40vw - 2px);
		padding: 2em;
	}

	.overlay__section-title {
		text-decoration: none;
		font-size: 1.2rem;
		color: var(--color-dark);
		display: block;
		font-weight: bold;
		text-transform: uppercase;
		padding-bottom: 4px;
		border-bottom: 2px solid var(--color-dark);
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

	@media (min-width: 800px) {
		.overlay__outer {
			width: calc(40vw - 2px);
		}

		.overlay--add {
			top: 0;
			right: -2px;
			border-top: none;
			border-left: var(--color-dark) solid 2px;
			height: 100%;
			box-shadow: -4px 0px 6px 0px rgba(0, 0, 0, 0.5);
		}

		.overlay__content {
			margin: 0;
			height: 125%;
		}
	}

	.songform {
		margin: auto;
		text-align: left;
		padding-left: 0;
		padding-top: 0;
		padding-bottom: 0.4em;
		padding-right: 0.4em;
		width: 100%;
		height: 1em;
		font-size: 12pt;
		background-color: #cee7ee;
		border: 2px solid var(--color-dark);
	}

	.subform {
		margin: auto;
		text-align: left;
		padding-left: 0;
		padding-top: 0;
		padding-bottom: 0.4em;
		padding-right: 0.4em;
		width: 100%;
		height: 18em;
		font-size: 12pt;
		background-color: #cee7ee;
		border: 2px solid var(--color-dark);
	}

	ol {
		text-align: left;
		padding-left: 1em;
	}

	ol li:not(:first-child) {
		margin-top: 0.5em;
	}

	textarea {
		font-family: 'Apfel Grotezk', sans-serif;
	}

	.action-button-container {
		right: 0;
	}
</style>

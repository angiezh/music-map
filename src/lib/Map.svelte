<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import { Map, NavigationControl, Popup, type LngLatLike } from 'maplibre-gl';
	import { getMomentText } from '$lib/getMomentText';
	import 'maplibre-gl/dist/maplibre-gl.css';
	import { filteredDataStore, fullDataStore, descriptionDataStore } from '../stores';

	import moments from '$lib/data/filtered_data_id_only.json';

	let map: Map;
	let mapContainer: HTMLDivElement;

	//const maptilerApiKey = 'SRfJh1CuGiISgDoqUg55';
	const maptilerApiKey = 'UHRJl9L3oK7bh3QT6De6';
	//const maptilerMapReference = 'd27741ff-e220-4106-a5a1-aedace679204';
	const maptilerMapReference = '99cf5fa2-3c1e-4adf-a1c1-fd879b417597';

	const initialState = { lng: -117.71319812050054, lat: 34.099885457669316, zoom: 16.5 };

	async function getMoment(id: number) {
		try {
			const response = await fetch(`/moment/${id}`);
			const data = await response.json();
			return data;
		} catch (error) {
			console.error('Error fetching moment:', error);
			return '';
		}
	}

	onMount(() => {
		map = new Map({
			container: mapContainer,
			style: `https://api.maptiler.com/maps/${maptilerMapReference}/style.json?key=${maptilerApiKey}`,
			center: [initialState.lng, initialState.lat],
			zoom: initialState.zoom,
			minZoom: 2,
			maxZoom: 18
		});
		map.addControl(new NavigationControl({ showCompass: false }), 'bottom-right');
		map.keyboard.enable();

		map.on('load', () => {
			map.addSource('moments', {
				type: 'geojson',
				data: moments
			});

			map.loadImage('src/lib/assets/Musicnotes.png', async function (error, image) {
				if (error) throw error;
				map.addImage('Musicnotes', image);
				console.log('image loaded');
			});

			// map.addLayer({
			// id: 'moments-layer',
			// type: 'circle',
			// source: 'moments',
			// paint: {
			// 'circle-radius': 8,
			// 'circle-color': 'black'
			// }
			// });

			map.addLayer({
				id: 'moments-layer',
				type: 'symbol',
				source: 'moments',
				layout: {
					'icon-image': 'Musicnotes',
					'icon-size': ['*', ['get', 'scalerank'], 0.001],
					'icon-allow-overlap': true
				},
				paint: {}
			});

			map.on('click', 'moments-layer', async function (e) {
				if (e.features && e.features.length > 0) {
					const feature = e.features[0];
					if (feature.geometry.type === 'Point') {
						const coordinates = feature.geometry.coordinates;
						const id = feature.properties.id; // Assuming `id` is stored in feature properties
						const description = await getMomentText(id); // Use await to get the description
						if (coordinates.length === 2) {
							new Popup()
								.setLngLat(coordinates as LngLatLike)
								.setHTML(description)
								.addTo(map);
						} else {
							console.error('Invalid coordinates format');
						}
					}
				}
			});

			// Change the cursor to a pointer when the mouse is over the moments layer.
			map.on('mouseenter', 'moments-layer', function () {
				map.getCanvas().style.cursor = 'pointer';
			});

			// Change it back to a pointer when it leaves.
			map.on('mouseleave', 'moments-layer', function () {
				map.getCanvas().style.cursor = '';
			});

			const unsubscribe = filteredDataStore.subscribe((updatedData) => {
				if (map.getSource('moments')) {
					map.getSource('moments').setData(updatedData);
				}
			});

			// Clean up the subscription when the component is destroyed
			onDestroy(unsubscribe);
		});
	});

	onDestroy(() => {
		if (map) {
			map.remove();
		}
	});
</script>

<div id="map" bind:this={mapContainer}></div>

<style>
	#map {
		position: absolute;
		width: 100%;
		height: 100%;
	}
</style>

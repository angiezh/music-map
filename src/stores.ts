import { writable } from 'svelte/store';
import initialFilteredData from '$lib/data/filtered_data_id_only.json';
import initialDescriptionData from '$lib/data/id_description_pairs.json';
import initialFullData from '$lib/data/filtered_data.json';

export const filteredDataStore = writable(initialFilteredData);
export const descriptionDataStore = writable(initialDescriptionData);
export const fullDataStore = writable(initialFullData);

export const infoOverlayVisible = writable(false);
export const addOverlayVisible = writable(false);

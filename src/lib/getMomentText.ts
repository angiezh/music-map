import { descriptionDataStore } from '../stores';

// Assuming each item in the descriptionDataStore looks something like this:
// { id: number, song: string, description: string }

// Adjusted to return an object containing both song and description
export async function getMomentText(id: number): Promise<{ song: string; description: string }> {
	return new Promise((resolve) => {
		const unsubscribe = descriptionDataStore.subscribe((data) => {
			const found = data.find((item) => item.id === id);
			if (found) {
				// If the item is found, resolve with both song and description
				resolve({ song: found.song, description: found.description });
			} else {
				// If not found, resolve with default values
				resolve({ song: 'Song not found', description: '' });
			}
			unsubscribe(); // Make sure to unsubscribe to avoid memory leaks
		});
	});
}

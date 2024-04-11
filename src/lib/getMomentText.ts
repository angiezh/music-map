import { descriptionDataStore } from '../stores';

// Adjusting getMomentText to work asynchronously
export async function getMomentText(id: number): Promise<string> {
	return new Promise((resolve) => {
		// Immediately-invoked function here to ensure cleanup
		const unsubscribe = descriptionDataStore.subscribe((data) => {
			const found = data.find((item) => item.id === id);
			resolve(found ? found.description : 'Description not found');
		});
		unsubscribe(); // Unsubscribe right after getting the data
	});
}

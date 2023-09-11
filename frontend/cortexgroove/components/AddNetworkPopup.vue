<template>
	<div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
		<div class="bg-white rounded-lg p-8 shadow-lg z-100 w-9/12">
			<!-- Add your content for the popup card here -->
			<slot>
				<div class="w-full bg-white">
					<h4 class="w-full text-3xl text-center font-bold">Create your band</h4>
					<div class="flex items-start justify-start w-full h-full p-4">
						<div class="relative w-full mt-4 space-y-8">
							<div class="relative">
								<label class="font-medium text-gray-900">Name</label>
								<input type="text"
									v-model="bandNameInput"
									class="block w-full px-4 py-2 mt-2 text-lg placeholder-gray-400 bg-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500 focus:ring-opacity-50"
									data-primary="blue-600" data-rounded="rounded-lg"
									placeholder="Band" />
							</div>
							<div class="relative">
								<label class="font-medium text-gray-900">Bio</label>
								<textarea
									v-model="bandBioInput"
									style="resize: none;"
									class="block w-full h-[20vh] px-4 py-2 mt-2 text-lg placeholder-gray-400 bg-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500 focus:ring-opacity-50"
									data-primary="blue-600" data-rounded="rounded-lg" placeholder="Bio"></textarea>
							</div>
							<div class="relative w-6/12">
								<label class="font-medium text-gray-900">Network</label>
								<ItemList :items="networks" key="Styles" class="w-4/12"></ItemList>
							</div>


							<div class="relative" @click="$emit('close')">
								<a href="#_"
									class="inline-block w-full px-5 py-4 text-lg font-medium text-center text-white transition duration-200 bg-violet-500 rounded-lg hover:bg-violet-700 ease"
									data-primary="violet-500" data-rounded="rounded-lg">Create</a>
							</div>
						</div>
					</div>
				</div>
			</slot>
			<!-- Add a close button or any other UI elements if needed -->
			<button @click="$emit('close')" class="mt-4 px-4 py-2 bg-violet-500 text-white rounded-lg">
				Close
			</button>
		</div>
  	</div>
</template>

<script setup lang="ts">


	const props = defineProps({
		isCreation: Boolean,
		isEdition: Boolean,
		bandId: Number,
	})

	let cortex = ref([[]]);

	let cortexes = ref([
		{
			name: `cortex 1`,
			structure: 
			[
				[ { name: `network 1`, data: `data 1` }, { name: `network 2`, data: `data 2` } ],
				[ { name: `network 3`, data: `data 3` }, { name: `network 4`, data: `data 4` }, { name: `network 5`, data: `data 5` } ],
				[ { name: `network 6`, data: `data 6` } ]
			]
		},
		{
			name: `cortex 2`,
			structure: 
			[
				[ { name: `network 7`, data: `data 7` }, { name: `network 8`, data: `data 8` } ],
				[ { name: `network 9`, data: `data 9` }, { name: `network 10`, data: `data 10` }, { name: `network 11`, data: `data 11` } ],
				[ { name: `network 12`, data: `data 12` } ]
			]
		},
	]);

	let networks = [
		{ name: `network 1`, data: `data 1` }, 
		{ name: `network 2`, data: `data 2` },
		{ name: `network 3`, data: `data 3` }, 
		{ name: `network 4`, data: `data 4` }, 
		{ name: `network 5`, data: `data 5` },
		{ name: `network 6`, data: `data 6` },
		{ name: `network 7`, data: `data 7` }, 
		{ name: `network 8`, data: `data 8` },
		{ name: `network 9`, data: `data 9` }, 
		{ name: `network 10`, data: `data 10` }, 
		{ name: `network 11`, data: `data 11` },
		{ name: `network 12`, data: `data 12` }
	]

	const areInputDisabbled = ref((!props.isCreation && !props.isEdition) ? false: true);
	const bandNameInput = ref('');
	const bandBioInput = ref('');

</script>
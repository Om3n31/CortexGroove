<template>
	<div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
		<div class="bg-slate-800 rounded-lg p-8 shadow-lg z-100 w-9/12">
			<!-- Add your content for the popup card here -->
			<slot>
				<div class="w-full">
					<h4 class="w-full text-3xl text-center font-bold">New layer</h4>
					<div class="flex items-start justify-start w-full h-full p-4">
						<div class="relative w-full mt-4">

							<label for="layerTypes" class="block font-medium dark:text-white mb-2">Layer type</label>
							<select v-model="selectedLayerType" @change="displayOptions()" id="layerTypes" class="appearance-none border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white">
								<option v-for="layerType in layerTypes" :value=layerType>{{ layerType.name }}</option>
							</select>
							
							<div class="border-t-2 mt-6 border-cortex-light-green border-dashed">
								<div v-for="option in selectedLayerTypeOptions">

								<div class="pt-4" v-if="option.possible_values.length && (option.type == 'boolean' || option.type == 'string')">
									<label :for="option.id.toString()" class="block font-medium dark:text-white mb-2">{{ option.name }}</label>
									<select :id="option.id.toString()" class="appearance-none border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white">
										<option v-for="value in option.possible_values" :value=value>{{ value }}</option>
									</select>
								</div>

								<div class="pt-4" v-if="!option.possible_values.length && option.type == 'integer'">
									<label :for="option.id.toString()" class="block font-medium dark:text-white mb-2">{{ option.name }}</label>
									<input type="number" :id="option.id.toString()" class="appearance-none border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white"/>
								</div>

								<div class="pt-4" v-if="option.type == 'float'">
									<label :for="option.id.toString()" class="block font-medium dark:text-white mb-2">{{ option.name }}</label>
									<input type="number" :id="option.id.toString()" min="0" max="1" class="appearance-none border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white"/>
								</div>

								</div>
							</div>

						</div>
					</div>
				</div>
			</slot>
			<!-- Add a close button or any other UI elements if needed -->
			<button @click="$emit('close')" class="border-2 border-red-700 mt-4 px-4 py-2 bg-slate-700 text-white rounded-lg hover:bg-red-500 hover:bg-opacity-30">
				Cancel
			</button>
		</div>
  	</div>
</template>

<script setup lang="ts">

	let layerTypes = ref(await useFetch<Layer[]>('http://localhost:8000/tflayertype/?format=json').data.value);
    let layerTypeOptions = ref(await useFetch<LayerOption[]>('http://localhost:8000/tflayertypeoption/?format=json').data.value);

	let selectedLayerType = ref<Layer>();
	let	selectedLayerTypeOptions = ref<LayerOption[]>([]);

	console.log(layerTypeOptions.value);

	function displayOptions() {

		let optionList = layerTypeOptions.value?.filter((option) => { return selectedLayerType.value?.options.includes(option.id) });
		
		if(!optionList)
			return;

		selectedLayerTypeOptions.value = optionList;
	}

	interface Layer {
		id: number,
		name: string,
		options: number[]
	}

	interface LayerOption {
		id: number,
		name: string,
		possible_values: string[],
		type: string
	}

</script>
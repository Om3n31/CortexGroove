<template>

    <button @click="addLayer()" class="bg-slate-800 hover:bg-slate-700 text-white py-1 px-2 rounded-lg w-max border-2 border-cortex-light-green cursor-pointer mt-6">+ Layer</button>
    <div class="p-2 border-2 border-cortex-green rounded-lg my-1 flex gap-2 border-dashed">
        <div class="w-2/12 cursor-pointer border-2 border-cortex-light-green p-2 rounded-lg" v-for="layer in cortex.metadata.layers">
            <div class="text-lg text-center py-2"> {{ layer.name }}</div>
            <div class="flex gap-2 justify-between border-b-2 border-cortex-light-green pb-2">
                <button @click="addNetwork(layer.name)" class="bg-slate-800 hover:bg-slate-700 text-white py-1 px-1 rounded-lg w-max border-2 border-cortex-light-green cursor-pointer">+ Neural Network</button>
                <button @click="removeLayer(layer.name)" class="bg-slate-800 hover:bg-red-700 text-white py-1 px-1 rounded-lg w-max border-2 border-red-500 cursor-pointer">Remove layer</button>
            </div>
            <div class="p-4 text-slate-500" v-if="cortex.metadata.layers.length"> Add neural networks to build your layers. Each neural network of this layers will be fully connected to all neural networks of the adjacents layers.</div>
            <div class="bg-gray-200 hover:bg-gray-400 active:bg-slate-500 cursor-pointer px-1" v-for="layer in cortex.metadata.layers">
            </div>
        </div>
    </div>
    <AddNetworkPopup v-show="showPopup" @close="closePopup()" :layerName="layerToEdit"></AddNetworkPopup>
</template>

<script setup lang="ts">

    import { ref } from 'vue';

    let showPopup = ref(false);
    let layerToEdit = ref('');

    let cortex = ref(
        {
            metadata: {
                layers: [] as { name: string, networks: { name: string, file: string } [] } []             
            }
        }
    );

    let counter = 1;

    function addLayer(): void {
        cortex.value.metadata.layers.push({ name: 'Layer ' + counter.toString(), networks: [] });
        counter++;
    }

    function removeLayer(layerName: string): void {
        for(let i = 0; i < cortex.value.metadata.layers.length; i++) {
            if(cortex.value.metadata.layers[i].name == layerName)
                cortex.value.metadata.layers.splice(i, 1);
        }
    }

    function addNetwork(layerName: string): void {
        showPopup.value = true;
        layerToEdit.value = layerName;
    }
    
	function closePopup() {
		showPopup.value = false;
	}

    /*
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
    */

</script>
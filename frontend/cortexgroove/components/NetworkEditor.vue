<template>

    <button @click="addLayer()" class="bg-slate-800 hover:bg-slate-700 text-white py-1 px-2 rounded-lg w-max border-2 border-cortex-light-green cursor-pointer mt-6">+ Layer</button>
    <div class="p-2 border-2 border-cortex-green rounded-lg my-1 flex gap-2 border-dashed">
        <div class="w-2/12 cursor-pointer border-2 border-cortex-light-green p-2 rounded-lg" v-for="i in network.layers.length">
            <button @click="removeLayer(i)" class="ml-auto bg-slate-800 hover:bg-red-700 text-white py-1 px-1 rounded-lg w-max border-2 border-red-500 cursor-pointer">Remove layer</button>
            <div class="text-lg text-center py-2"> layer {{ i }}</div>
            <div class="relative mb-3" data-te-input-wrapper-init>
                <input
                    type="number"
                    class="rounded-lg border-2 bg-transparent px-3 py-2 w-full"
                    id="exampleFormControlInputNumber"
                    placeholder="Example label" />
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">

    import { ref } from 'vue';

    let showPopup = ref(false);
    let layerToEdit = ref('');
    let network = ref(
        {
            name: String,
            layers: [] as number []
        }
    );

    function addLayer(): void {
        network.value.layers.push(1);
    }

    function removeLayer(index: number): void {
        network.value.layers.splice(index, 1);
    }
    function addNetwork(layerName: string): void {
        showPopup.value = true;
        layerToEdit.value = layerName;
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
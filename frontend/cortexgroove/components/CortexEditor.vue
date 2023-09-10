<template>

    <button @click="addLayer()" class="bg-slate-800 hover:bg-slate-700 text-white py-1 px-2 rounded-lg w-max border-2 border-cortex-light-green cursor-pointer mt-6">+ Layer</button>
    <div class="p-2 border-2 border-cortex-green rounded-lg my-1 flex gap-2 border-dashed">
        <div class="w-2/12 cursor-pointer border-2 border-cortex-light-green p-2 rounded-lg" v-for="layer in cortex.metadata.layers">
            <div class="text-lg text-center py-2"> {{ layer.name }}</div>
            <div class="flex gap-2 justify-between border-b-2 border-cortex-light-green pb-2">
                <button @click="addNetwork('')" class="bg-slate-800 hover:bg-slate-700 text-white py-1 px-1 rounded-lg w-max border-2 border-cortex-light-green cursor-pointer">+ Neural Network</button>
                <button @click="removeLayer(layer.name)" class="bg-slate-800 hover:bg-red-700 text-white py-1 px-1 rounded-lg w-max border-2 border-red-500 cursor-pointer">Remove layer</button>
            </div>
            <div class="p-4 text-slate-500" v-if="cortex.metadata.layers.length"> Add neural networks to build your layers. Each neural network of this layers will be fully connected to all neural networks of the adjacents layers.</div>
            <div class="bg-gray-200 hover:bg-gray-400 active:bg-slate-500 cursor-pointer px-1" v-for="layer in cortex.metadata.layers">
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

    import { ref } from 'vue';

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
        console.log('adding network...');
        
    }
</script>
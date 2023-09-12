<template>
    <button @click="addLayer()" class="bg-slate-800 hover:bg-slate-700 text-white py-1 px-2 rounded-lg w-max border-2 border-cortex-light-green cursor-pointer mt-6">+ Layer</button>
    <div class="p-2 border-2 border-cortex-green rounded-lg my-1 flex gap-2 border-dashed">
      <div class="w-2/12 cursor-pointer border-2 border-cortex-light-green p-2 rounded-lg" v-for="(layer, index) in network.layers" :key="`layer-${index}`">
        <button @click="removeLayer(index)" class="ml-auto bg-slate-800 hover:bg-red-700 text-white py-1 px-1 rounded-lg w-max border-2 border-red-500 cursor-pointer">Remove layer</button>
        <div class="text-lg text-center py-2"> layer {{ index + 1 }}</div>
        <div class="relative mb-3" data-te-input-wrapper-init>
          <AutocompleteInput :items="layerTypes" @autocomplete="displayOptions"></AutocompleteInput>
        </div>
      </div>
    </div>
  </template>
<script setup lang="ts">

    import { ref } from 'vue';

    let layerTypesQuery = await useFetch('http://localhost:8000/tflayertype/?format=json').data.value;

    let layerTypes = ref(layerTypesQuery as unknown []);
    let layerTypeOptions = ref(await useFetch('http://localhost:8000/tflayertypeoption/?format=json'));

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

    function displayOptions(item: any) {
        console.log('I now have to display the options correponding to', item);
    }
</script>
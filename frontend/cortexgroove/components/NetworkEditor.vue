<template>
			<div @click="openCreationPopup()" class="cursor-pointer inline-flex items-center justify-center px-4 py-2 text-base font-medium leading-6 text-white whitespace-no-wrap bg-slate-700 border-2 border-cortex-light-green rounded-md shadow-sm hover:opacity-70"> 
				+ Add a layer
			</div>
      <Transition>
				<AddLayerPopup v-show="showCreationPopup" @close="closeCreationPopup"></AddLayerPopup>
			</Transition>    
      <div class="p-2 border-2 border-cortex-green rounded-lg my-1 flex gap-2 border-dashed">
      <div class="w-2/12 cursor-pointer border-2 border-cortex-light-green p-2 rounded-lg" v-for="(layer, index) in network.layers" :key="`layer-${index}`">
        <button @click="removeLayer(index)" class="ml-auto bg-slate-800 hover:bg-red-700 text-white py-1 px-1 rounded-lg w-max border-2 border-red-500 cursor-pointer">Remove layer</button>
        <div class="text-lg text-center py-2"> layer {{ index + 1 }}</div>

      </div>
    </div>
  </template>
<script setup lang="ts">

    import { ref } from 'vue';


    let showCreationPopup = ref(false)

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

    function openCreationPopup() {
      showCreationPopup.value = true
    }

    function closeCreationPopup() {
      showCreationPopup.value = false
    }
</script>
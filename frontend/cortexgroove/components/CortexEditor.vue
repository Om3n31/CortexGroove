<template>
    <div class="p-2 border-2 border-cortex-green rounded-lg my-6" id="cortexEditor">
        <button @click="addLayer" class="bg-slate-800 hover:bg-slate-700 text-white py-1 px-2 rounded-lg w-max border-2 border-cortex-light-green cursor-pointer">+Layer</button>


    </div>
</template>

<script setup lang="ts">

    import { ref } from 'vue';

    function addLayer(): void {
        console.log('adding layer...');
        const cortexEditor = ref<HTMLElement | null>(document.getElementById('cortexEditor'));

        var layer = document.createElement("EditorLayer");
        cortexEditor.value?.append(layer);
    }

</script>
<template>
    <div>
        <p>Cortex #{{ id }}</p>
    </div>
</template>

<script setup>
    
    const { id } = useRoute().params

    let network = ref(await useFetch<Network[]>('http://localhost:8000/neuralnetwork/?format=json').data.value);

</script>
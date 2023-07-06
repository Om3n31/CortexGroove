<template>
    <div>
        <header class="shadow-sm bg-slate-800">
            <nav class="mx-auto p-8 flex justify-between text-white">
                <p class="font-bold text-cortex-light-green">Cortex Groove</p>

                <ul class="flex gap-20">
                    <li>
                        <NuxtLink to="/">Home</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink to="/cortex-database">Cortex Database</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink to="/create-cortex">Create Cortex</NuxtLink>
                    </li>

                </ul>
                <NuxtLink to="/account">Account</NuxtLink>

            </nav>
        </header>
    </div>
    <div class="px-8 mx-10 p-4 text-white">
        <slot/> 
    </div>
</template>

<style scoped>
    .router-link-exact-active {
        color: #C4F1BE;
    }
</style>
<script setup>
import { NCard, NCode } from 'naive-ui'
import { useImageStore } from '@/stores/useImageStore'

const imageStore = useImageStore()
</script>

<template>
    <div class="main-content" v-if="imageStore.hasResult">
        <NCard class="main-content-image">
            <template #header>Результат на изображении</template>
            <img v-if="imageStore.imageURL" :src="imageStore.imageURL" />
        </NCard>
        <NCard class="main-content-result">
            <template #header>Результаты</template>
        </NCard>
    </div>
    <NCard class="json-content" v-if="imageStore.hasResult">
        <template #header>Результат (json)</template>
        <NCode :code="imageStore.resultJSON" language="json" />
    </NCard>
</template>

<style>
.main-content {
    display: flex;

    flex-wrap: nowrap;

    gap: 20px;

    margin-bottom: 20px;
}

.main-content-image {
    width: auto;
}

.main-content-result {
    width: 100%;
}
</style>

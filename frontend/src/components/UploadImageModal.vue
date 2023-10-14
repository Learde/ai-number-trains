<script setup>
import { ref } from 'vue'
import { NModal, NCard, NUpload, NButton } from 'naive-ui'
import BaseLoader from '@/components/BaseLoader.vue'
import { useImageStore } from '@/stores/useImageStore'
import fakeAnswer from '@/assets/placeholder.json'

const isShown = ref(true)

const imageStore = useImageStore()

const handleUpload = async ({ file }) => {
    imageStore.startLoading()
    imageStore.setImage(file)

    const promise = new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                data: fakeAnswer
            })
        }, 3000)
    })

    const data = (await promise).data
    imageStore.setResult(data)

    imageStore.stopLoading()
}
</script>

<template>
    <NModal v-model:show="isShown" :close-on-esc="false" :mask-closable="false">
        <NCard
            style="width: 500px; height: 250px"
            title="Modal"
            :bordered="false"
            size="huge"
            role="dialog"
            aria-modal="true"
        >
            <template #header> Загрузите фотографию для распознавания </template>
            <template #default>
                <div class="upload-content">
                    <NUpload class="upload-component" :custom-request="handleUpload">
                        <NButton type="primary" size="large">Выбрать</NButton>
                    </NUpload>
                    <BaseLoader v-if="imageStore.isLoading" />
                </div>
            </template>
        </NCard>
    </NModal>
</template>

<style>
.upload-content {
    display: flex;

    align-items: center;

    justify-content: center;

    height: 100%;
}

.upload-component {
    display: inline-block;

    width: auto;
}

.n-upload-file-list {
    display: none;
}
</style>

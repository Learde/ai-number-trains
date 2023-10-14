import { ref, computed, warn } from 'vue'
import { defineStore } from 'pinia'

export const useImageStore = defineStore('image', () => {
    const image = ref(null)
    const imageURL = ref(null)
    const isLoading = ref(false)

    const hasImage = computed(() => {
        return Boolean(image.value)
    })

    const hasResult = computed(() => {
        return Boolean(imageURL.value) && !isLoading.value
    })

    function startLoading() {
        isLoading.value = true
    }

    function stopLoading() {
        isLoading.value = false
    }

    function setImage(img) {
        image.value = img
        renderImage(img.file)
    }

    function renderImage(file) {
        const fileReader = new FileReader()

        fileReader.onload = () => {
            imageURL.value = fileReader.result
        }

        fileReader.readAsDataURL(file)
    }

    return { image, imageURL, isLoading, hasResult, setImage, hasImage, startLoading, stopLoading }
})

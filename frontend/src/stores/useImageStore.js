import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useImageStore = defineStore('image', () => {
    const image = ref(null)
    const imageURL = ref(null)
    const result = ref(null)
    const isLoading = ref(false)

    const hasImage = computed(() => {
        return Boolean(image.value)
    })

    const hasResult = computed(() => {
        return Boolean(imageURL.value) && !isLoading.value && Boolean(result.value)
    })

    const resultJSON = computed(() => {
        if (!result.value) return ''
        return JSON.stringify(result.value, null, 4)
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

    function setResult(res) {
        result.value = res
    }

    function renderImage(file) {
        const fileReader = new FileReader()

        fileReader.onload = () => {
            imageURL.value = fileReader.result
        }

        fileReader.readAsDataURL(file)
    }

    return {
        image,
        imageURL,
        isLoading,
        hasResult,
        setImage,
        hasImage,
        startLoading,
        stopLoading,
        result,
        resultJSON,
        setResult
    }
})
<script setup>
import { NUpload, NConfigProvider, lightTheme, darkTheme } from "naive-ui";
import axios from "axios";

const customRequest = ({
    file,
    data,
    headers,
    withCredentials,
    action,
    onFinish,
    onError,
    onProgress
}) => {
    const formData = new FormData()
    if (data) {
        Object.keys(data).forEach((key) => {
            formData.append(
                key,
                data[key]
            )
        })
    }
    formData.append(file.name, file.file)
    axios.post(action, {
        withCredentials,  headers,
        body,
        onUploadProgress: ({ percent }) => {
            onProgress({ percent: Math.ceil(percent) })
        }
    })
    .then(({ json }) => {
        message.success(JSON.stringify(json))
        onFinish()
    })
    .catch((error) => {
        message.success(error.message)
        onError()
    })
};
</script>

<template>
    <main>
        <NUpload
            class="upload"
            list-type="image-card"
            :custom-request="customRequest"
         >
             Выберите изображение
         </NUpload>
        <div class="info-block">
            <div class="info">
                <span class="info-title">Распознанный номер:</span>
                <span class="info-value">12345678</span>
            </div>
            <div class="info">
                <span class="info-title">Координаты номера:</span>
                <span class="info-value">(400; 350)</span>
            </div>
            <div class="info">
                <span class="info-title">Координаты первой цифры:</span>
                <span class="info-value">(400; 350)</span>
            </div>
            <div class="info">
                <span class="info-title">Координаты второй цифры:</span>
                <span class="info-value">(400; 350)</span>
            </div>
            <div class="info">
                <span class="info-title">Координаты третьей цифры:</span>
                <span class="info-value">(400; 350)</span>
            </div>
            <div class="info">
                <span class="info-title">Координаты четвертой цифры:</span>
                <span class="info-value">(400; 350)</span>
            </div>
            <div class="info">
                <span class="info-title">Координаты пятой цифры:</span>
                <span class="info-value">(400; 350)</span>
            </div>
            <div class="info">
                <span class="info-title">Координаты шестой цифры:</span>
                <span class="info-value">(400; 350)</span>
            </div>
            <div class="info">
                <span class="info-title">Координаты седьмой цифры:</span>
                <span class="info-value">(400; 350)</span>
            </div>
            <div class="info">
                <span class="info-title">Координаты восьмой цифры:</span>
                <span class="info-value">(400; 350)</span>
            </div>
        </div>
    </main>
</template>

<style>

main {
    width: 100vw;
    height: 75vh;
}

.upload {
    width: 100%;
    height: 100%;
    
}

.n-upload-file-list {
    width: 100%;
    height: 100%;
    grid-template-columns: 1fr !important;
}

.n-upload-trigger, .n-upload-file {
    width: 100% !important;
    height: 100% !important;
}

.n-upload-file + .n-upload-trigger {
    display: none !important;
}

.info-block {
    margin: 20px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
}

.info-title {
    font-weight: bold;
}

.info {
    display: flex;
    gap: 10px;
}

.n-image img {
    object-fit: contain !important;
}
</style>

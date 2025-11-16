<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const fileInput = ref(null)
const fileName = ref('')
const filePreview = ref('')

const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    fileName.value = file.name

    if (file.type.startsWith('image/')) {
      const reader = new FileReader()
      reader.onload = (e) => {
        filePreview.value = e.target.result
      }
      reader.readAsDataURL(file)
    } else {
      filePreview.value = ''
    }
  }
}

const clearFile = () => {
  fileInput.value.value = ''
  fileName.value = ''
  filePreview.value = ''
}

const emit = defineEmits(['toggleOpenModal'])

const handleClose = () => {
  emit('toggleOpenModal')
}

const formData = ref({
  name: '',
  category: '',
  description: '',
  url: '',
})

const setName = (value) => {
  formData.value.name = value
}

const setCategory = (value) => {
  formData.value.category = value
}

const setDescription = (value) => {
  formData.value.description = value
}

const setUrls = (value) => {
  formData.value.url = value
}

const validateForm = (event) => {
  event.preventDefault()

  const isValid =
    formData.value.url !== '' &&
    formData.value.name !== '' &&
    formData.value.category !== '' &&
    formData.value.description !== ''

  if (isValid) {
    alert('Форма успешно отправлена!')
  } else {
    alert('Пожалуйста, заполните все обязательные поля.')
  }

  emit('toggleOpenModal')

  return isValid
}

// Управление скроллом body
onMounted(() => {
  document.body.classList.add('no-scroll')
})

onUnmounted(() => {
  document.body.classList.remove('no-scroll')
})
</script>

<template>
  <div class="overlay" @click="handleClose">
    <div class="popup-container" @click.stop>
      <div class="popup">
        <div class="popup-header">
          <h2 class="popup-title">Добавление НКО</h2>
          <button class="popup-close" @click="handleClose">
            <img src="/icons/close-button-2.png" alt="Close" />
          </button>
        </div>

        <div class="popup-scroll-container">
          <form class="popup-form" @submit="validateForm">
            <div class="form-group">
              <label class="popup-label" for="nko-name">Название</label>
              <input
                class="popup-input"
                @input="setName($event.target.value)"
                type="text"
                id="nko-name"
                name="nko-name"
                required
              />
            </div>

            <div class="form-group">
              <label class="popup-label" for="nko-category"
                >Категория/направление деятельности</label
              >
              <input
                class="popup-input"
                type="text"
                id="nko-category"
                name="nko-category"
                @input="setCategory($event.target.value)"
                required
              />
            </div>

            <div class="form-group">
              <label class="popup-label" for="nko-description">Описание деятельности</label>
              <textarea
                class="popup-textarea"
                id="nko-description"
                name="nko-description"
                @input="setDescription($event.target.value)"
                required
              ></textarea>
            </div>

            <div class="form-group">
              <label class="popup-label" for="nko-tel">Контактный телефон (если есть)</label>
              <input class="popup-input" type="tel" id="nko-tel" name="nko-tel" />
            </div>

            <div class="form-group">
              <label class="popup-label" for="nko-address">Адрес (если есть)</label>
              <input class="popup-input" type="text" id="nko-address" name="nko-address" />
            </div>

            <div class="form-group">
              <label class="popup-label">Фото организации (если есть)</label>
              <div class="file-upload-wrapper">
                <input
                  type="file"
                  id="nko-photo"
                  ref="fileInput"
                  @change="handleFileChange"
                  class="file-input"
                  accept="image/*"
                />
                <label for="nko-photo" class="file-label">
                  <span class="file-button">
                    <img src="/icons/folder.png" alt="" />
                    <span>Выберите файл</span>
                  </span>
                  <span class="file-name" :class="{ 'has-file': fileName }">
                    {{ fileName || 'Файл не выбран' }}
                  </span>
                </label>

                <div v-if="filePreview" class="file-preview">
                  <img :src="filePreview" alt="Preview" class="preview-image" />
                  <button type="button" class="clear-btn" @click="clearFile">
                    <img src="/icons/close-button.png" alt="" />
                  </button>
                </div>
              </div>
            </div>

            <div class="form-group">
              <label class="popup-label" for="nko-url">Ссылки на сайт и соцсети</label>
              <input
                class="popup-input"
                type="text"
                id="nko-url"
                name="nko-url"
                @input="setUrls($event.target.value)"
                required
              />
            </div>

            <button class="btn popup-button" type="submit">Отправить заявку</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" src="../assets/styles/components/nko-form-modal.scss" scoped></style>

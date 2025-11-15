<script setup>
import '../assets/styles/components/map.scss'
import nkoData from '../data/organizations.js'
import { onMounted, onUnmounted, ref, reactive } from 'vue'

const mapContainer = ref(null)
const organizations = reactive(nkoData)
let mapInstance = null

const coordinates = [
  // Обнинск (2)
  [55.095, 36.613],
  [55.092, 36.62],

  // Саров (3)
  [54.913, 43.328],
  [54.905, 43.34],
  [54.92, 43.315],

  // Северск (2)
  [56.607, 84.903],
  [56.615, 84.89],

  // Волгодонск (2)
  [47.52, 42.13],
  [47.53, 42.145],

  // Зеленогорск (2)
  [56.103, 94.58],
  [56.095, 94.595],

  // Балаково (2)
  [52.013, 47.72],
  [52.005, 47.735],

  // Димитровград (2)
  [54.215, 49.595],
  [54.225, 49.58],

  // Нововоронеж (2)
  [51.315, 39.185],
  [51.325, 39.17],

  // Озерск (2)
  [55.74, 60.68],
  [55.75, 60.665],

  // Сосновый Бор (2)
  [59.9, 28.84],
  [59.91, 28.855],

  // Электросталь (2)
  [55.795, 38.455],
  [55.805, 38.47],

  // Байкальск (2)
  [51.5, 104.49],
  [51.49, 104.505],

  // Ангарск (2)
  [52.525, 103.905],
  [52.535, 103.89],

  // Билибино (2)
  [68.055, 166.43],
  [68.065, 166.445],
]

const loadYandexMapsAPI = () => {
  return new Promise((resolve, reject) => {
    if (window.ymaps) {
      resolve(window.ymaps)
      return
    }

    const script = document.createElement('script')
    script.src =
      'https://api-maps.yandex.ru/2.1/?apikey=5511f06e-b789-4865-af76-eca1284883f7&lang=ru_RU'
    script.async = true

    script.onload = () => {
      window.ymaps.ready(() => {
        resolve(window.ymaps)
      })
    }
    script.onerror = () => reject(new Error('Не удалось загрузить Яндекс.Карты'))
    document.head.appendChild(script)
  })
}

onMounted(async () => {
  try {
    const ymaps = await loadYandexMapsAPI()
    mapInstance = new ymaps.Map(mapContainer.value, {
      center: [55.751574, 37.573856],
      zoom: 7,
      controls: ['zoomControl', 'typeSelector'],
    })

    const customBalloon = ymaps.templateLayoutFactory.createClass(
      `<div class="rosatom-balloon">
         <div class="balloon-header">
           <h3 class="org-name">{{ properties.balloonData.name }}</h3>
           <span class="org-category">{{ properties.balloonData.category }}</span>
           <button class="balloon-close-button" type="button" title="Закрыть"><img src="/icons/close-button.png"/></button>
         </div>
         <div class="balloon-content">
           <p class="org-description">{{ properties.balloonData.description }}</p>
           <div class="org-contacts">
             <strong>Контакты:</strong> {{ properties.balloonData.contacts }}
           </div>
         </div>
         {{#if properties.balloonData.website}}
         <div class="balloon-footer">
           <a href="{{ properties.balloonData.website }}" target="_blank" class="website-link">
             Перейти на сайт
           </a>
         </div>
         {{/if}}
       </div>`,
      {
        build: function () {
          customBalloon.superclass.build.call(this)

          const closeButton = this.getElement().querySelector('.balloon-close-button')
          if (closeButton) {
            closeButton.addEventListener('click', () => {
              this.getData().geoObject.balloon.close()
            })
          }
        },

        clear: function () {
          const closeButton = this.getElement().querySelector('.balloon-close-button')
          if (closeButton) {
            closeButton.removeEventListener('click', () => {})
          }
          customBalloon.superclass.clear.call(this)
        },
      },
    )

    organizations.forEach((org, index) => {
      if (!coordinates[index]) return

      const placemark = new ymaps.Placemark(
        coordinates[index],
        {
          balloonContentHeader: org.name,
          balloonContentBody: org.description,
          balloonContentFooter: org.contacts,
          balloonData: org,
        },
        {
          balloonLayout: customBalloon,
          preset: 'islands#blueIcon',
          iconColor: '#003274',
        },
      )

      mapInstance.geoObjects.add(placemark)
    })
  } catch (error) {
    console.error('Ошибка загрузки карты:', error)
  }
})

onUnmounted(() => {
  if (mapInstance) {
    mapInstance.destroy()
    mapInstance = null
  }
})
</script>

<template>
  <section class="map-wrapper">
    <div class="map-container" ref="mapContainer"></div>
  </section>
</template>

<style lang="scss" scoped></style>

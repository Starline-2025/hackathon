<script setup>
import { inject } from 'vue'
import '../assets/styles/components/map.scss'
import { onMounted, onUnmounted, ref } from 'vue'

const organizations = inject('organizations')

const mapContainer = ref(null)
let mapInstance = null

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
      center: [55.751574, 37.573856], // Центр по умолчанию
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

    // Перебираем каждую организацию
    organizations.forEach((org) => {
      // Проверяем, есть ли у организации координаты
      if (org.lat !== undefined && org.lng !== undefined) {
        // Создаём метку с координатами из org
        const placemark = new ymaps.Placemark(
          [org.lat, org.lng],
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
      } else {
        console.warn(`Организация "${org.name}" не имеет координат (lat/lng) и будет пропущена.`)
      }
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

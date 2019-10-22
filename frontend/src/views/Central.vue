<template>
  <div>
    <ImgBanner call="central" height="100vh">
      <div style="line-height:1.1em; font-weight:bold;text-align:center" slot="text" class="layout align-center justify-center row fill-height">
               
         <br/> WATCH THE DRONES
         <br/> FIND YOUR TARGET
      </div>
    </ImgBanner>
    <v-container grid-list-xs style="margin-top:50px">
        <v-text-field
            class="mx-3"
            flat
            label="Search"
            prepend-inner-icon="fa-search"
            solo-inverted
        ></v-text-field>
        <v-layout row wrap>
            <v-flex xs12 md4>
              <v-card>
                    <v-card-title primary-title class="justify-center">
                        Log Information
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-text>
                        <div>
                            <v-data-table
                            :headers="headers"
                            :items="desserts"
                            :pagination.sync="pagination"
                            :total-items="totalDesserts"
                            :loading="loading"
                            class="elevation-1"
                            >
                            <template v-slot:items="props">
                                <td>{{ props.item.name }}</td>
                                <td class="text-xs-right">{{ props.item.calories }}</td>
                                <td class="text-xs-right">{{ props.item.fat }}</td>
                                <td class="text-xs-right">{{ props.item.carbs }}</td>
                                <td class="text-xs-right">{{ props.item.protein }}</td>
                                <td class="text-xs-right">{{ props.item.iron }}</td>
                            </template>
                            </v-data-table>
                        </div>
                    </v-card-text>
                </v-card>
            </v-flex>

            <v-flex xs12 md8>
                <v-card>
                    <v-card-title primary-title class="justify-center">
                        Find Target (전체화면 : pin 찍어라!)
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-text>
                        핀 찍는 이미지 파일 전송하는 거 만들어줘요~ 플리즈~
                        <v-img
                        :src="getImgUrl('mappin.gif')"
                        height="200px"
                        >
                        </v-img>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>

        <v-layout row wrap>
              <v-flex v-for="(drone,index) in drones" :key="index" xs4>
                <v-card >
                    <v-card-title primary-title class="justify-center">
                        Drone - {{index+1}} 화면
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-text>
                        드론 {{index+1}}} 화면 보여줘요~
                        <v-img :src="getImgUrl(drone.src)">
                        </v-img>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
  </div>
</template>

<script>
import ImgBanner from '../components/ImgBanner'
import axios from 'axios'

  export default {
    name:"Central",
    components:{
      ImgBanner
    },
    data () {
      return {
        drones:[
          {
            src:'footerlogo.png',
            position:'',
          },
          {
            src:'footerlogo.png',
            position:'',
          },
          {
            src:'footerlogo.png',
            position:''
          }],

        totalDesserts: 0,
        desserts: [],
        loading: true,
        pagination: {},
        headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'left',
            sortable: false,
            value: 'name'
          },
          { text: 'Calories', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Iron (%)', value: 'iron' }
        ]
      }
    },
    watch: {
      pagination: {
        handler () {
          this.getDataFromApi()
            .then(data => {
              this.desserts = data.items
              this.totalDesserts = data.total
            })
        },
        deep: true
      }
    },
    mounted () {
      this.getDataFromApi()
        .then(data => {
          this.desserts = data.items
          this.totalDesserts = data.total
        })
    },
    methods: {
      getImgUrl(img){
        // axios.get('/drone/position',{
        //   params:{

        //   }
        // }).then(response => {

        // }).catch(error=>{
        //   console.error(e)
        // })
        return require('../assets/'+img)
      },

      getDataFromApi () {
        this.loading = true
        return new Promise((resolve, reject) => {
          const { sortBy, descending, page, rowsPerPage } = this.pagination

          let items = this.getDesserts()
          const total = items.length

          if (this.pagination.sortBy) {
            items = items.sort((a, b) => {
              const sortA = a[sortBy]
              const sortB = b[sortBy]

              if (descending) {
                if (sortA < sortB) return 1
                if (sortA > sortB) return -1
                return 0
              } else {
                if (sortA < sortB) return -1
                if (sortA > sortB) return 1
                return 0
              }
            })
          }

          if (rowsPerPage > 0) {
            items = items.slice((page - 1) * rowsPerPage, page * rowsPerPage)
          }

          setTimeout(() => {
            this.loading = false
            resolve({
              items,
              total
            })
          }, 1000)
        })
      },
      getDesserts () {
        return [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: '1%'
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: '1%'
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: '7%'
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: '8%'
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: '16%'
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: '0%'
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: '2%'
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: '45%'
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: '22%'
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: '6%'
          }
        ]
      }
    }
  }
</script>
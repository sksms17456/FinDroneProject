<template>
    <v-card style="height:100%;">
        <!-- <v-card-text> -->
            <template>
                <v-data-table
                  :headers="headers"
                  :items="target"
                  :rows-per-page-items="[10, 20, 30, 40]"
                  :pagination.sync="pagination"
                  class="elevation-1"
                  style="height:100vh"
                >
                    <template v-slot:items="props">
                        <td class="text-xs-right">{{ props.item.time }}</td>
                        <td class="text-xs-right">{{ props.item.posy }}</td>
                        <td class="text-xs-right">{{ props.item.posx }}</td>
                        <td class="text-xs-right">{{ props.item.posz }}</td>
                    </template>
                </v-data-table>
            </template>
        <!-- </v-card-text> -->
    </v-card>
</template>

<script>
export default {
  name: 'LogsMonitor',
  data () {
    return {
      rowsPerPageItems: [10, 20, 30, 40],
      pagination: {
          rowsPerPage: 10
      },
      headers:[
        // {
        //   text: 'Target',
        //   align: 'left',
        //   sortable: false,
        //   value: 'name'
        // },
        { text: '시간', value: 'time' },
        { text: 'Y좌표', value: 'posy' },
        { text: 'X좌표', value: 'posx' },
        { text: 'Z좌표', value: 'posz' }
      ],
      target:[
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },{
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },{
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },{
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },{
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        },
        {
          name:'Target',
          src:'footerlogo.png',
          time:'',
          posy:'1',
          posx:'2',
          posz:'3',
          state:''
        }
      ],
    }
  }
}
</script>

<style scoped>

</style>

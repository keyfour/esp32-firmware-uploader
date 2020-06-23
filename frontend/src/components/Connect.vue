<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
        <uploader-dropdown v-model="port" v-bind:items="ports"
          v-on:change="$emit('selected', port)"/>
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCol,
} from 'mdbvue';
import UploaderDropdown from './Dropdown.vue';

export default {
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    UploaderDropdown,
  },
  data() {
    return {
      port: 'Connection port',
    };
  },
  props: ['ports'],
};
</script>

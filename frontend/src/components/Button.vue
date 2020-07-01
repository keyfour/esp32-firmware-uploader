<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
        <mdb-btn color="primary" :disabled="!active" v-on:click="$emit('click')">{{name}}</mdb-btn>
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCol,
  mdbBtn,
} from 'mdbvue';

export default {
  name: 'UploaderButton',
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbBtn,
  },
  data() {
    return {
      state: 'disabled',
    };
  },
  props: ['name', 'active'],
};
</script>

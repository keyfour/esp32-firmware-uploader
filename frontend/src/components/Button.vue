<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
        <mdb-btn color="success">{{name}}</mdb-btn>
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
  props: ['name'],
};
</script>

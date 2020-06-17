<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
        <mdb-btn color="success">Start</mdb-btn>
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
  name: 'ButtonPage',
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbBtn,
  },
};
</script>

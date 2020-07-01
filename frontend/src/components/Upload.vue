<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
        <b-form-file
          multiple
          v-model="files"
          :state="null"
          placeholder="Choose a file or drop it here..."
          drop-placeholder="Drop file here..."
          v-on:input="uploadFiles"
         ></b-form-file>
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

export default {
  name: 'ButtonPage',
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
  },
  data() {
    return {
      files: [],
    };
  },
  methods: {
    uploadFiles() {
      this.$emit('changed', this.files);
    },
  },
};
</script>

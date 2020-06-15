<template>
  <div class="container">
    <div class="row align-itmes-center">
      <div class="col">
        <h1>{{header}}</h1>
      </div>
    </div>
    <div class="row align-items-start">
      <div class="col">
          <mdb-stepper simpleH :steps="steps" @input="nextStep"/>
      </div>
    </div>
    <div class="row align-items-center">
      <div class="col">
          <template v-if="1 === step"><platform></platform></template>
          <template v-if="2 === step"><connect></connect></template>
          <template v-if="3 === step"><upload></upload></template>
      </div>
    </div>
  </div>
</template>

<script>
import { mdbStepper } from 'mdbvue';
import Platform from './Platform.vue';
import Connect from './Connect.vue';
import Upload from './Upload.vue';

export default {
  name: 'Upload',
  step: 1,
  components: {
    mdbStepper,
    Platform,
    Connect,
    Upload,
  },
  data() {
    return {
      header: 'ESP32 Firmware Uploader',
      steps: [
        {
          name: 'Platform',
          content: 'Select board and framework',
        },
        {
          name: 'Connect',
          content: 'Select device interface',
        },
        {
          name: 'Upload',
          content: 'Start device programming',
        },
      ],
    };
  },
  methods: {
    nextStep(num) {
      console.warn(num);
      this.step = num;
    },
  },
};
</script>

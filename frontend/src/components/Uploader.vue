<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
        <h1>{{header}}</h1>
      </mdb-col>
    </mdb-row>
    <mdb-row>
      <mdb-col>
          <mdb-stepper simpleH :steps="steps" @input="nextStep" :value="step" />
      </mdb-col>
    </mdb-row>
    <mdb-row>
      <mdb-col>
        <transition enter-active-class="animated slideInLeft">
          <platform v-if="1 === step"></platform>
          <connect  v-else-if="2 === step"></connect>
          <upload   v-else-if="3 === step"></upload>
        </transition>
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCol,
  mdbStepper,
} from 'mdbvue';
import Platform from './Platform.vue';
import Connect from './Connect.vue';
import Upload from './Upload.vue';

export default {
  name: 'Uploader',
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbStepper,
    Platform,
    Connect,
    Upload,
  },
  data() {
    return {
      header: 'ESP32 Firmware Uploader',
      step: 1,
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
          content: 'Device programming',
        },
      ],
    };
  },
  methods: {
    nextStep(num) {
      this.step = num;
    },
  },
};
</script>

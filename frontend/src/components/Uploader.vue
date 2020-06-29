<template>
  <mdb-container fluid>
    <mdb-row class="pt-5">
      <mdb-col md="8" offsetMd="2">
          <h1>{{header}}</h1>
      </mdb-col>
    </mdb-row>
    <mdb-row class="pt-3">
      <mdb-col md="8" offsetMd="2">
        <transition enter-active-class="animated slideInLeft">
          <platform v-if="1 === step" v-bind:boards="boards"
            v-bind:frameworks="frameworks" v-on:selected="enableNext"/>
          <connect  v-else-if="2 === step" v-bind:ports="ports"
            v-on:selected="enableNext"/>
          <upload v-else-if="3 === step" v-on:changed="enableNext"></upload>
        </transition>
      </mdb-col>
    </mdb-row>
    <mdb-row style="pointer-events:none;" class="justify-content-center">
      <mdb-col md="6" offsetMd="1">
        <mdb-stepper simpleH :steps="steps" @input="nextStep" :value="step" />
      </mdb-col>
    </mdb-row>
    <mdb-row class="pb-5">
      <mdb-col>
        <uploader-button v-bind:name="buttonName" v-bind:active="buttonState"
          v-on:click="nextStep(step + 1)">
        </uploader-button>
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
import UploaderButton from './Button.vue';

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
    UploaderButton,
  },
  data() {
    return {
      headers: ['Choose platform', 'Connect to device', 'Choose firmware'],
      step: 1,
      header: '',
      buttonName: 'Next',
      buttonNames: ['Select', 'Open', 'Upload'],
      buttonState: false,
      boards: [
        {
          id: 0,
          name: 'ESP32-WROOM',
        },
        {
          id: 1,
          name: 'ESP32-CAM',
        },
        {
          id: 2,
          name: 'Heltec ESP32s',
        },
      ],
      boardID: undefined,
      frameworks: [
        {
          id: 0,
          name: 'Arduino',
        },
        {
          id: 1,
          name: 'ESP-IDF',
        },
      ],
      frameworkID: undefined,
      ports: [
        {
          id: 0,
          name: '/dev/ttyUSB0',
        },
        {
          id: 1,
          name: '/dev/ttyACM0',
        },
        {
          id: 2,
          name: '/dev/ttyS0',
        },
      ],
      portID: undefined,
      steps: [
        {
          name: 'Platform',
          // content: 'Select board and framework',
        },
        {
          name: 'Connect',
          // content: 'Select device interface',
        },
        {
          name: 'Upload',
          // content: 'Device programming',
        },
      ],
    };
  },
  methods: {
    nextStep(num) {
      if (num > 0 && num <= this.steps.length) {
        this.step = num;
        this.header = this.headers[this.step - 1];
        this.buttonName = this.buttonNames[this.step - 1];
        this.buttonState = false;
      }
    },
    enableNext() {
      this.buttonState = true;
    },
  },
  beforeMount() {
    this.nextStep(1);
  },
};
</script>

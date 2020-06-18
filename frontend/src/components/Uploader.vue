<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
          <h1>{{header}}</h1>
      </mdb-col>
    </mdb-row>
    <mdb-row>
      <mdb-col>
        <transition enter-active-class="animated slideInLeft">
          <platform v-if="1 === step" v-bind:boards="boards"
            v-bind:frameworks="frameworks"/>
          <connect  v-else-if="2 === step"></connect>
          <upload   v-else-if="3 === step"></upload>
        </transition>
      </mdb-col>
    </mdb-row>
    <mdb-row>
      <mdb-col>
          <mdb-stepper simpleH :steps="steps" @input="nextStep" :value="step" />
      </mdb-col>
    </mdb-row>
    <mdb-row>
      <mdb-col>
        <uploader-button v-bind:name="buttonName"></uploader-button>
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
      this.step = num;
      this.header = this.headers[this.step - 1];
      this.buttonName = this.buttonNames[this.step - 1];
    },
  },
  beforeMount() {
    this.nextStep(1);
  },
};
</script>

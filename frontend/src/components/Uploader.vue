<template>
  <div class="container">
    <div class="row align-itmes-center">
      <div class="col">
        <h1>{{header}}</h1>
      </div>
    </div>
    <div class="row align-items-start">
      <div class="col">
        <horizontal-stepper :steps="uploadSteps" @completed-step="uploadStep"
          @active-step="isStepActive" @stepper-finished="alert">
        </horizontal-stepper>
      </div>
    </div>
  </div>
</template>

<script>
import HorizontalStepper from 'vue-stepper';
import Platform from './Platform.vue';

export default {
  name: 'Upload',
  components: {
    HorizontalStepper,
  },
  data() {
    return {
      header: 'ESP32 Firmware Uploader',
      uploadSteps: [
        {
          icon: 'settings',
          name: 'platform',
          title: 'Platform',
          subtitle: 'Select board and framework',
          component: Platform,
          completed: false,
        },
      ],
      activeStep: 0,
    };
  },
  methods: {
    // Executed when @completed-step event is triggered
    uploadStep(payload) {
      this.uploadSteps.forEach((step) => {
        if (step.name === payload.name) {
          step.completed = true; // eslint-disable-line no-param-reassign
        }
      });
    },
    // Executed when @active-step event is triggered
    isStepActive(payload) {
      this.uploadSteps.forEach((step) => {
        if (step.name === payload.name) {
          if (step.completed === true) {
            step.completed = false; // eslint-disable-line no-param-reassign
          }
        }
      });
    },
    alert(payload) { // eslint-disable-line no-unused-vars
      alert('end');
    },
  },
};
</script>

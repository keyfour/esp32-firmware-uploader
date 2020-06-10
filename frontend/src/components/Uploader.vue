<template>
  <div class="bs-stepper">
  <div class="bs-stepper-header" role="tablist">
    <!-- your steps here -->
    <div class="step" data-target="#platform-part">
      <button type="button" class="step-trigger" role="tab"
        aria-controls="platform-part" id="platform-part-trigger">
        <span class="bs-stepper-circle">1</span>
        <span class="bs-stepper-label">Platform</span>
      </button>
    </div>
    <div class="line"></div>
    <div class="step" data-target="#connect-part">
      <button type="button" class="step-trigger" role="tab"
        aria-controls="connect-part" id="connect-part-trigger">
        <span class="bs-stepper-circle">2</span>
        <span class="bs-stepper-label">Connect</span>
      </button>
    </div>
    <div class="line"></div>
    <div class="step" data-target="#upload-part">
      <button type="button" class="step-trigger" role="tab"
        aria-controls="upload-part" id="upload-part-trigger">
        <span class="bs-stepper-circle">3</span>
        <span class="bs-stepper-label">Upload</span>
      </button>
    </div>
  </div>
  <div class="bs-stepper-content">
    <!-- your steps content here -->
    <div id="platform-part" class="content" role="tabpanel"
        aria-labelledby="platform-part-trigger">
        <div class="card">
        <div class="card-body">
        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button"
                id="dropdownMenuButton" data-toggle="dropdown"
                aria-haspopup="true" aria-expanded="false">
                Dropdown button
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <a class="dropdown-item" href="#">Something else here</a>
            </div>
        </div>
        </div>
        </div>
    </div>
    <div id="connect-part" class="content" role="tabpanel"
        aria-labelledby="connect-part-trigger"></div>
    <div id="upload-part" class="content" role="tabpanel"
        aria-labelledby="upload-part-trigger"></div>
  </div>
</div>
</template>

<script>
export default {
  name: 'Upload',
  data() {
    return {
      msg: 'Hello!',
    };
  },
};
</script>

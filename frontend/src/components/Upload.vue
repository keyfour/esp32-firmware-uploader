<template>
    <div class="container">
        <div class="row align-item-start">
            <div class="col">
                <mdb-btn color="success">Start</mdb-btn>
            </div>
        </div>
    </div>
</template>

<script>
import { mdbBtn } from 'mdbvue';

export default {
  name: 'ButtonPage',
  components: {
    mdbBtn,
  },
};
</script>

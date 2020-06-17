<template>
    <div class="container">
        <div class="row align-item-start">
            <div class="col">
                <mdb-dropdown>
                    <mdb-dropdown-toggle slot="toggle">Select Board</mdb-dropdown-toggle>
                    <mdb-dropdown-menu>
                        <mdb-dropdown-item>ESP32-WROOM</mdb-dropdown-item>
                        <mdb-dropdown-item>ESP32-CAM</mdb-dropdown-item>
                        <mdb-dropdown-item>Heletec ESP32s</mdb-dropdown-item>
                    </mdb-dropdown-menu>
                </mdb-dropdown>
            </div>
            <div class="col">
                <mdb-dropdown>
                    <mdb-dropdown-toggle slot="toggle">Select Framework</mdb-dropdown-toggle>
                    <mdb-dropdown-menu>
                        <mdb-dropdown-item>Arduino</mdb-dropdown-item>
                        <mdb-dropdown-item>ESP-IDF</mdb-dropdown-item>
                    </mdb-dropdown-menu>
                </mdb-dropdown>
            </div>
        </div>
    </div>
</template>

<script>
import {
  mdbDropdown,
  mdbDropdownToggle,
  mdbDropdownMenu,
  mdbDropdownItem,
} from 'mdbvue';

export default {
  components: {
    mdbDropdown,
    mdbDropdownToggle,
    mdbDropdownMenu,
    mdbDropdownItem,
  },
  data() {
    return {
      foo: 'foo',
    };
  },
};
</script>

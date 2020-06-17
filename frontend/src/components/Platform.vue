<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
        <mdb-dropdown>
          <mdb-dropdown-toggle slot="toggle">Select Board</mdb-dropdown-toggle>
          <mdb-dropdown-menu>
            <mdb-dropdown-item>ESP32-WROOM</mdb-dropdown-item>
              <mdb-dropdown-item>ESP32-CAM</mdb-dropdown-item>
              <mdb-dropdown-item>Heletec ESP32s</mdb-dropdown-item>
          </mdb-dropdown-menu>
        </mdb-dropdown>
      </mdb-col>
      <mdb-col>
        <mdb-dropdown>
          <mdb-dropdown-toggle slot="toggle">Select Framework</mdb-dropdown-toggle>
          <mdb-dropdown-menu>
            <mdb-dropdown-item>Arduino</mdb-dropdown-item>
            <mdb-dropdown-item>ESP-IDF</mdb-dropdown-item>
          </mdb-dropdown-menu>
        </mdb-dropdown>
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCol,
  mdbDropdown,
  mdbDropdownToggle,
  mdbDropdownMenu,
  mdbDropdownItem,
} from 'mdbvue';

export default {
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
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

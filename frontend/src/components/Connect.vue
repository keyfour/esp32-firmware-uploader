<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
        <mdb-dropdown>
          <mdb-dropdown-toggle slot="toggle">Connection port</mdb-dropdown-toggle>
            <mdb-dropdown-menu>
                <mdb-dropdown-item>/dev/ttyUSB0</mdb-dropdown-item>
                <mdb-dropdown-item>/dev/ttyACM0</mdb-dropdown-item>
                <mdb-dropdown-item>/dev/ttyS0</mdb-dropdown-item>
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
};
</script>

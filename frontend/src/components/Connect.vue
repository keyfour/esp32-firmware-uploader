<template>
    <div class="container">
        <div class="row align-item-start">
            <div class="col">
                <mdb-dropdown>
                    <mdb-dropdown-toggle slot="toggle">Connection port</mdb-dropdown-toggle>
                    <mdb-dropdown-menu>
                        <mdb-dropdown-item>/dev/ttyUSB0</mdb-dropdown-item>
                        <mdb-dropdown-item>/dev/ttyACM0</mdb-dropdown-item>
                        <mdb-dropdown-item>/dev/ttyS0</mdb-dropdown-item>
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
};
</script>

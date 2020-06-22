<template>
  <mdb-dropdown>
    <mdb-dropdown-toggle
      slot="toggle">{{selected.name ? selected.name : selected}}
    </mdb-dropdown-toggle>
    <mdb-dropdown-menu>
      <mdb-dropdown-item v-for="item in items"
        v-bind:key="item.id"  v-on:click="selectItem(item)">
          {{ item.name }}
      </mdb-dropdown-item>
    </mdb-dropdown-menu>
  </mdb-dropdown>
</template>

<script>
import {
  mdbDropdown,
  mdbDropdownToggle,
  mdbDropdownMenu,
  mdbDropdownItem,
} from 'mdbvue';

export default {
  name: 'UploaderDropdown',
  components: {
    mdbDropdown,
    mdbDropdownToggle,
    mdbDropdownMenu,
    mdbDropdownItem,
  },
  props: ['selected', 'items'],
  methods: {
    selectItem(item) {
      this.value = item.name;
      this.$emit('change', item);
    },
  },
  model: {
    prop: 'selected',
    event: 'change',
  },
};
</script>

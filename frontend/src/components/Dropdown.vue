<template>
  <mdb-dropdown>
    <mdb-dropdown-toggle slot="toggle">{{selected}}</mdb-dropdown-toggle>
    <mdb-dropdown-menu>
      <mdb-dropdown-item v-for="item in items"
        v-bind:key="item.id" @click="selected = item.name">
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
  data() {
    return {
      selected: '',
    };
  },
  props: ['default', 'items'],
  methods: {
    selectItem(item) {
      this.selected = item.name;
      this.$emit('selected');
    },
  },
  beforeMount() {
    this.selectItem({ id: -1, name: this.default });
  },
};
</script>

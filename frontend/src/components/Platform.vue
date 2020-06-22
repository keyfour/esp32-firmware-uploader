<template>
  <mdb-container>
    <mdb-row>
      <mdb-col>
        <uploader-dropdown v-model="board" v-bind:items="boards"
          v-on:change="selected.board = board; isSelected.board = true; select()"/>
      </mdb-col>
      <mdb-col>
        <uploader-dropdown v-model="framework" v-bind:items="frameworks"
          v-on:change="selected.framework = framework; isSelected.framework = true; select()"/>
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCol,
} from 'mdbvue';
import UploaderDropdown from './Dropdown.vue';


export default {
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    UploaderDropdown,
  },
  data() {
    return {
      board: 'Board',
      framework: 'Framework',
      selected: {
        board: undefined,
        framework: undefined,
      },
      isSelected: {
        board: false,
        framework: false,
      },
    };
  },
  props: ['boards', 'frameworks'],
  methods: {
    select() {
      if (this.isSelected.board && this.isSelected.framework) {
        this.$emit('selected', this.selected);
      }
    },
  },
};
</script>

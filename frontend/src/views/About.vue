<template>
  <div class="home">
    <div class="grid grid-cols-4 gap-4">
      <div
        class="shadow-md m-1 bg-white"
        v-for="peli in allPeliculas.edges"
        v-bind:key="peli.node.id"
      >
        <img :src="peli.node.portada" />
        <div class="p-8">
          <div class="flex flex-row items-center">
            <p class="text-xl font-bold">{{ peli.node.titulo }}</p>
            <p class="ml-2 font-sans text-red-400">{{ peli.node.estreno }}</p>
          </div>
          <div class="my-2">
            <label class="text-sm bg-blue-100 px-4 py-2 rounded-full">{{
              peli.node.genero
            }}</label>
          </div>
          <p class="">{{ peli.node.descripcion }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { peliculas } from '../graphql/getPeliculas.gql'

export default {
  name: "About",
  data() {
    return {
      peliculas: [],
    };
  },
  apollo: {
    allPeliculas: peliculas
  },
  mounted() {
  },
};
</script>

<style lang="scss">
img {
  width: 100%;
  min-height: 20rem;
  background-attachment: scroll;
}

.select,
select {
  width: 100%;
}

.card {
  margin-bottom: 20px;
}

.done {
  opacity: 0.3;
}

img {
  max-height: 12rem;
}
</style>

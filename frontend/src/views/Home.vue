<template>
  <div class="home">
    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="addPelicula">
          <h2 class="subtitle">Nueva pelicula</h2>

          <div class="field">
            <label class="label">Titulo</label>
            <div class="control">
              <input class="input" type="text" v-model="titulo" />
            </div>
          </div>

          <div class="field">
            <label class="label">año de estreno</label>
            <div class="control">
              <input class="input" type="number" v-model="estreno" />
            </div>
          </div>

          <div class="field">
            <label class="label">Descripcion</label>
            <div class="control">
              <input class="input" type="text" v-model="descripcion" />
            </div>
          </div>

          <div class="field">
            <label class="label">Link imagen de portada</label>
            <div class="control">
              <input class="input" type="text" v-model="portada" />
            </div>
          </div>

          <div class="field">
            <label class="label">Genero</label>
            <div class="control">
              <div class="select">
                <select v-model="genero">
                  <option value="romance">romance</option>
                  <option value="accion">accion</option>
                  <option value="comedia">comedia</option>
                  <option value="terror">terror</option>
                  <option value="sifi">sifi</option>
                  <option value="animacion">animacion</option>
                  <option value="musical">musical</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Guardar</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
const API_URL = "http://127.0.0.1:8000";

import axios from "axios";
import gql from 'graphql-tag'

export default {
  name: "Home",
  data() {
    return {
      descripcion: "",
      genero: "romance",
      titulo: "",
      estreno: "",
      portada: "",
    };
  },
  methods: {

    addPelicula() {
      if (this.descripcion) {
        axios({
          method: "post",
          url: `${API_URL}/peliculas/`,
          data: {
            descripcion: this.descripcion,
            genero: this.genero,
            titulo: this.titulo,
            estreno: this.estreno,
            portada: this.portada,
          },
          auth: {
            username: "juan",
            password: "mycatisadog",
          },
        })
          .then((response) => {
            console.log(response);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style lang="scss">
.textinput {
  border: solid 1px grey;
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
</style>

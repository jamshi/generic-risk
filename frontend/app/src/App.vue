<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <h2>Available Risk Register Forms</h2>
    <ul>
      <li v-for="item in risks" :key="item.risk_code">
        <a v-on:click="selected=item">{{item.risk_type}}</a>
      </li>
    </ul>
    <div v-if="selected!=null">
      <h4>{{selected.risk_type}}</h4>
      <form>

      <ul>
        <li class="form-elem" v-for="item in selected.attrs" :key="item.field_name">
        <div class='label'>
        <label>{{item.display_title}}</label>
        </div>
        <div class='input'>
        <input type="text" v-if="item.field_type=='text'"/>
        <input type="date" v-if="item.field_type=='date'"/>
        <input type="number" v-if="item.field_type=='number'"/>
        <select v-if="item.field_type=='enum'">
          <option v-for="option in item.choices" v-bind:value="option">
            {{ option }}
          </option>
        </select>
        </div>
        </li>
      </ul>
      <input type="submit" value="Submit"/>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'BriteCore Screening (Jamsheed BP)',
      risks: [],
      selected: null
    }
  },
  mounted() {
      this.$nextTick( () => {
          this.fetchData();
      })
  },
  methods: {
      fetchData() {
          this.$http.get('/risk/all/')
              .then(result => { 
              this.risks = result.data
              })
      }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}
li.form-elem{
  display: block !important;
  margin:10px;
}

li.form-elem > .label{
  display:inline-block;
  width:150px;
  text-align:left;
}
li.form-elem > .input{
  display:inline-block;
  width:70px;
}

a {
  color: #42b983;
  cursor:pointer;
}
</style>

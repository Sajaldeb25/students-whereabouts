<template>
  <!-- <div id="app"> -->

    {{msg}}

    <table class="table">
      <thead>
        <th>Name</th>
        <th>Course</th>
        <th>Rating</th>
      </thead>

      <tbody>
        <tr v-for="student in students" :key="student.id">
          <td>{{ student.name }}</td>
          <td>{{ student.course }}</td>
          <td>{{ student.ratings }}</td>
        </tr>
      </tbody>

    </table>
  
  
  <!-- </div> -->
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  // components: {
  //   HelloWorld
  // }
  data(){
    return{
      // msg:'Hello Vue js'[]
      students: []
    }
  },
  async created(){
    var response = await fetch('http://127.0.0.1:8000/students/');
    this.students = await response.json();  
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

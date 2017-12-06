<template>
  <div id="app"> 
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="24" :md="24" :lg="10" :xl="10">  
        <el-container> 
          <pannel/>
          <el-footer> 
            <p>本网站仅作技术研究，请勿用于商业用途。</p> 
            <p>By Xichao Geng</p>
            <p>
              <iframe src="https://ghbtns.com/github-btn.html?user=gengxichao&amp;type=follow&amp;count=false" frameborder="0" scrolling="0" width="170px" height="20px"></iframe>
              <wb:follow-button uid="1739492152" type="red_1" width="67" height="24" style="display:inline-block;"></wb:follow-button>
            </p> 
            <p>Github repo</p>
            <p>
              <iframe src="https://ghbtns.com/github-btn.html?user=gengxichao&amp;repo=mianliao_counselor&amp;type=star&amp;count=true" frameborder="0" scrolling="0" width="72px" height="20px"></iframe>
            </p> 
          </el-footer> 
        </el-container>
      </el-col>
   </el-row>
  </div>
</template>

<script>
import Pannel from './Pannel.vue'
export default {
  name: 'app',
  components: {
    Pannel
  }
}
</script>

<style>
html, body {
  width: 100%;
  height: 100%;
}
#app {
  width: 100%;
  height: 100%;
}
.el-header, .el-footer {
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-footer p{
  line-height: 30px;
}
</style>

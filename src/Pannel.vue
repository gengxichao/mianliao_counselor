<template>
  <div id="pannel">
  <el-header>
    UESTC 辅导员测评
    </el-header> 
    <el-main> 
      <el-form ref="form" :rules="rules" :model="form" label-width="80px" v-loading="loading" element-loading-text="拼命生成中" element-loading-spinner="el-icon-loading"> 
        <el-form-item label="用户名" prop="username"> 
          <el-input v-model="form.username" placeholder="通常为学号或者录取通知书号" clearable=""></el-input> 
        </el-form-item> 
        <el-form-item label="密码" prop="password"> 
          <el-input type="password" v-model="form.password" placeholder="通常和你的门户密码相同" clearable=""></el-input> 
        </el-form-item> 
        <el-form-item> 
          <el-button type="primary" @click="submitForm">
            进入评价系统
          </el-button> 
          <el-button @click="resetForm">
            清空
          </el-button> 
        </el-form-item> 
      </el-form> 
    </el-main>
  </div> 
</template>

<script>
export default {
  name: 'pannel',
  data () {
    return {
      form: {
        username: '',
        password: ''
      },
      rules:{
        username:[{required: true, message: "请填写用户名", trigger: 'blur'}],
        password:[{required:true, message: "请填写密码", trigger: 'blur'}]
      },
      loading: false,
      alertInfo: "",
      showAlert: false
    }
  },
  methods: {
    submitForm() {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          this.loading = true
          this.$http.post("/api/login", this.form).then((resp)=>{
            const user = resp.body
            if(user.code == 1){
              const uid = user.response.uid
              const token = user.response.token
              const url = `http://dev.tjut.cc:92/?uid=${uid}&token=${token}&source=ml`
              this.loading = false
              this.$message({
                dangerouslyUseHTMLString: true,
                message: `成功生成链接，即将自动跳转，<a href="${url}">可以点击这里手动跳转</a>`,
                type: 'success',
                duration: 0});
              setTimeout(`location.href='${url}'`,3000)
            }else{
              this.$notify.error({
                title: `无法登陆，错误代码${user.code}`,
                message: '一般情况下为用户名或者密码错误～',
                duration: 0
              });
              this.loading = false
            }
          })
        } else {
          return false;
        }
      });
    },
    resetForm() {
      this.$refs['form'].resetFields();
    },
    closeAlert() {
      this.$refs['form'].resetFields();
    }
  }
}
</script>


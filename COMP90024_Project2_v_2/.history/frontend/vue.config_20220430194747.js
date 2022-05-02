module.exports = {
  publicPath: './',
  devServer: {
    open: process.platform === "darwin",
    host: "localhost",
    port: 8081,
    https: false,
    hotOnly: false,
    overlay: {
      warnings: false,
      errors: false
    },
    proxy: {
      "/api": {
        // 目标 API 地址
        target: process.env.VUE_APP_URL,
        // target:'http://127.0.0.1:5000/',
        // 如果要代理 websockets
        // ws: false,
        changeOrigin: true, // 允许websockets跨域
        pathRewrite: {
          // 正则匹配，把到/devapi之前的所有替换成空
          "^/api": ""
        }
      }
    },
    // 代理转发配置，用于调试环境
    disableHostCheck: true
  }
}
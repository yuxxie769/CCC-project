module.exports = {
  publicPath: './',
  devServer: {
    proxy: {
      "/api": {
        // 目标 API 地址
        target: process.env.VUE_APP_URL,
        // target:'http://127.0.0.1:5000/',
        // 如果要代理 websockets
        // ws: false,
        changeOrigin: true, // 允许websockets跨域
      }
    },
  }
}
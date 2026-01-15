export default {
  content: [
    './templates/**/*.html',
    './apps/*/templates/**/*.html',
    './static/js/**/*.js',
    './node_modules/flowbite/**/*.js',  // ← TAMBAH INI
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')  // ← TAMBAH INI
  ],
}
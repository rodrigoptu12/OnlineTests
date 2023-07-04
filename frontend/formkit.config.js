
// formkit.config.js
import { defaultConfig } from '@formkit/vue'
import { createMultiStepPlugin } from '@formkit/addons'

const config = defaultConfig({
  plugins: [createMultiStepPlugin()],
  theme: 'genesis'
})

export default config
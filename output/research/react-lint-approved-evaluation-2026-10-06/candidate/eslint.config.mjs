import reactHooks from 'eslint-plugin-react-hooks';
import parser from '@typescript-eslint/parser';
import {defineConfig} from 'eslint/config';
export default defineConfig([
  reactHooks.configs.flat.recommended,
  {files:['**/*.tsx'], languageOptions:{parser,parserOptions:{ecmaVersion:'latest',sourceType:'module',ecmaFeatures:{jsx:true}}}, settings:{'react-hooks':{additionalEffectHooks:'(useSpecialEffect)'}}}
]);

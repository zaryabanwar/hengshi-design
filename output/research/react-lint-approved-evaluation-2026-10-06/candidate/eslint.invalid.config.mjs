import reactHooks from 'eslint-plugin-react-hooks';
import parser from '@typescript-eslint/parser';
import {defineConfig} from 'eslint/config';
export default defineConfig([
  reactHooks.configs.flat.recommended,
  {rules:{'react-hooks/not-a-real-rule':'error'}},
  {rules:{'no-restricted-syntax':['error',{selector:"ImportDeclaration[source.value='react'] > ImportSpecifier[imported.name=/^use[A-Z0-9]/][local.name!=/^use[A-Z0-9]/]",message:'Keep React Hook import aliases named use followed by an uppercase letter or digit so Hook checks remain enforceable.'}]}},
  {files:['**/*.tsx'], languageOptions:{parser,parserOptions:{ecmaVersion:'latest',sourceType:'module',ecmaFeatures:{jsx:true}}}, settings:{'react-hooks':{additionalEffectHooks:'(useSpecialEffect)'}}}
]);

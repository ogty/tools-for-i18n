# Sample App

## Create app and install package

```zsh
$ npx create-react-app sample --template typescript
$ cd sample
$ npm install react-i18next i18next i18next-http-backend --save
$ npm start
```

**sample/src/i18n.ts**

```ts
import i18n from 'i18next';
import Backend from 'i18next-http-backend';
import { initReactI18next } from 'react-i18next';

i18n
  .use(Backend)
  .use(initReactI18next)
  .init({
    ns: ['translations'],
    fallbackLng: window.navigator.language.split('-')[0],
    defaultNS: 'translations',
    debug: false,
    interpolation: {
      escapeValue: false,
    },
  });

export default i18n;
```

> **Note**  
> Internationalization support can be confirmed by changing the language from the browser settings.

**sample/src/index.tsx**

```diff
  ...
  import App from './App';
  import reportWebVitals from './reportWebVitals';
+ import './i18n';

  const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
  );
  ...
```

**sample/src/App.tsx**

```ts
import './App.css';
import { useTranslation } from "react-i18next";

function App() {
  const { t } = useTranslation();
  return <h1>{t("hello")}</h1>;
}

export default App;
```

## Creation of data for internationalization

**sample/public/locales/sample.yaml**

```yaml
hello:
  ja: "こんにちは世界"
  en: "Hello, world!"
```

**tools-for-internationalization/main.py**

```python
...
if __name__ == "__main__":
    languages = ["ja", "en"]
    segmenter = LanguageSegmenter(
        import_file_name="./sample/public/locales/sample.yaml",
        languages=languages
    )
    segmenter.write("./sample/public/locales")
    segmenter.output_table(languages)
```

### Execute program

```zsh
$ python3 main.py
```

### Execution Result

<table>
<tr align="center">
<td>Path</td>
<td>JA</td>
<td>EN</td>
</tr><tr></tr>
<tr></tr><tr>
<td>

```
hello
```

</td>

<td>

```js
"こんにちは世界"
```

</td>
<td>

```js
"Hello, world!"
```

</td>

</tr>
</table>

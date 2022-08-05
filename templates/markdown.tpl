<table>
<tr>
{% for column in columns -%}
<td>{{ column }}</td>
{% endfor -%}
</tr>

{%- for path, element in data.items() %}
<tr>
<td>

```
{{ path }}
```

</td>
{%+ for language in languages -%}
<td>

```js
{{ element[language] }}
```

</td>
{% endfor -%}
</tr><tr></tr>
{% endfor -%}
</table>

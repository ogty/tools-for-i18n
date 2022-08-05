<table border="1">
    <thead>
        <tr>
        {% for column in columns -%}
            <th>{{ column }}</th>
        {% endfor -%}
        </tr>
    </thead>

    <tbody>
    {%- for path, element in data.items() %}
        <tr>
        <td>{{ path }}</td>
        {%+ for language in languages -%}
        <td>

<pre>
<code>
{{ element[language] }}
</code>
</pre>

        </td>
        {% endfor -%}
        </tr>
    {% endfor -%}
    </tbody>
</table>

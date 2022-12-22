<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>i18n table</title>
    <link href="http://fonts.cdnfonts.com/css/menlo" rel="stylesheet">
</head>
<body>

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
<code class="data">
{{ element[language] }}
</code>
</pre>

        </td>
        {% endfor -%}
        </tr>
    {% endfor -%}
    </tbody>
</table>

<style>
    body {
        margin: 0;
    }
    table {
        color: white;
        width: 100%;
        font-size: 12px;
        font-family: Menlo, monospace;
        border-spacing: 0;
        border-collapse: collapse;
        background-color: #22262f;
    }
    td {
        padding: 10px;
    }
    code {
        font-family: Menlo, monospace;

    }
    pre {
        color: #ADBAC7;
        white-space: pre-wrap;
        font-family: Menlo, monospace;
        background-color: #22262f;
    }
    .string {
        color: #96D0FF;
    }
    .number {
        color: #6CB6FF;
    }
    .boolean {
        color: #6CB6FF;
    }
    .null {
        color: #6CB6FF;
    }
    .key {
        color: #8DDB8C;
    }
</style>

<script>
    const element = document.getElementsByClassName('data');
    for (let i = 0; i < element.length; i += 1) {
        console.log(element[i]);
        element[i].innerHTML = syntaxHighlight(element[i].innerText);
    }

    function syntaxHighlight(json) {
        json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
            let className = 'number';
            if (/^"/.test(match)) {
                if (/:$/.test(match)) {
                    className = 'key';
                } else {
                    className = 'string';
                }
            } else if (/true|false/.test(match)) {
                className = 'boolean';
            } else if (/null/.test(match)) {
                className = 'null';
            }
            if (/:/.test(match)) {
                return `<span class="${className}">${match.replace(':', '')}</span>:`;
            }
            return `<span class="${className}">${match}</span>`;
        });
    }
</script>
</body>
</html>
